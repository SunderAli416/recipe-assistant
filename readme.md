# Recipe Assistant Project

The Recipe Assistant is a conversational AI application designed to provide users with recipes based on their requests or ingredients mentioned. Utilizing advanced natural language processing and machine learning techniques, this assistant can extract recipes from a given set of PDF documents, understand user queries, and provide relevant recipe suggestions.

## Features

- Extracts text from PDF files containing recipes.
- Processes and understands natural language queries about recipes.
- Provides recipe suggestions based on ingredients or recipe requests.
- Maintains a conversational context to enhance user interaction.

## File Structure

```plaintext
.
├── data/                   # Directory containing recipe PDFs
├── helper_functions.py     # Utility functions for text extraction from PDFs
├── langchain_helper_functions.py  # Core functionality including text processing and response generation
└── streamlit_ui.py         # Streamlit application for the user interface       # Streamlit application for the user interface



## Methodology and Technologies

### Text Extraction

- **PDF Processing**: The `fitz` library (PyMuPDF) is used to read and extract text from PDF files located in the `data/` directory. This process converts the content of each page into a string format for further processing.

### Natural Language Processing

- **LangChain**: A powerful library for building language model-based applications. It is used to structure and process the text data extracted from PDFs and to handle user queries.
- **FAISS & Chroma**: These components from LangChain are utilized for efficient similarity search and storage of text chunks. They help in quickly retrieving relevant recipe information based on the user's query.
- **OpenAI Embeddings**: Leveraged for converting text into high-dimensional vectors that capture semantic meaning, enabling effective search and retrieval.
- **RecursiveCharacterTextSplitter**: A text splitting strategy used to divide the recipe text into manageable chunks for processing and vector storage.

### Conversational AI

- **Generative Models**: The application supports the use of Google Generative AI (`ChatGoogleGenerativeAI`) and OpenAI's models as the backbone for generating conversational responses. These models are fine-tuned to provide contextually relevant recipe suggestions.
- **Retrieval and Document Chains**: These LangChain constructs are employed to integrate the recipe context with the conversational model, ensuring that the AI's responses are informed by the actual recipes extracted from the PDFs.

### User Interface

- **Streamlit**: An open-source app framework used to create a simple and interactive UI for the Recipe Assistant. Users can enter their queries, and the application maintains a chat history for a seamless conversational experience.

## Getting Started

1. **Setup**: Ensure you have Python installed and clone this repository.
2. **Dependencies**: Install the required libraries using `pip install -r requirements.txt`.
3. **Data Preparation**: Place your recipe PDFs in the `data/` directory.
4. **Running the Application**: Launch the Streamlit UI with `streamlit run streamlit_ui.py`.

## Usage

- Start a conversation by asking for a recipe or mentioning some ingredients.
- The assistant, leveraging the conversational AI model and the recipe context extracted from your PDFs, will provide you with a suitable recipe.

## Contributing

- Contributions are welcome! Please fork the repository and submit a pull request with your improvements or suggestions.

