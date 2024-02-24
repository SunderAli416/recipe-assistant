from langchain import FAISS
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter,CharacterTextSplitter
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from helper_functions import get_text
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
chat_history=' '
def get_vector_store(text,embeddings):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1500,
        chunk_overlap=10,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    knowledgeBase = FAISS.from_texts(chunks, embeddings)
    return knowledgeBase


embeddings = OpenAIEmbeddings()
llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0)
# llm=ChatOpenAI(temperature=0)
text=get_text('data/')
vector=get_vector_store(text,embeddings)
prompt = ChatPromptTemplate.from_template("""You are a Chef Named Leo.Your job is to continue a conversation.You will continue the conversation from the 
                                          chat history provided.The context is recipes in your arsenal and you can tell recipes if someone asks for it in question
                                           or if someone lists ingredients tell them recipe best fit for them from your arsenal. and if you dont have the recipe or
                                           if you understand the query you can say so. If you tell any recipe out of the recipe context then there may be serious health issues 
                                           faces by the user.


Recipe Context:
{context}

Chat History:
{history}                                          

                                          
Based on the recipe context above,
Question: {input}

""")


document_chain = create_stuff_documents_chain(llm, prompt)
retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)


def query_assistant(input):
    global chat_history
    response = retrieval_chain.invoke({"input": input,'history':chat_history})
    chat_history=chat_history+f"User Said:{input}\nYou Said:{response['answer']}\n"
    return response["answer"]
