# Sample Files

This project includes a set of Python scripts for extracting information and demonstrating a question-answering application using Atlas Vector Search and RAG architecture.

## Project Structure

- `README.md`: Project documentation providing an overview of the project and usage instructions.
- `extract_information.py`: Python script for extracting information using Atlas Vector Search.
- `key_param.py`: Configuration file containing key parameters and dependencies.
- `load_data.py`: Python script for loading data into MongoDB Atlas.
- `Sample_Files/`: Directory containing sample text files for demonstration.

## `key_param.py` - Configuration File

The `key_param.py` file serves as a configuration file for setting up key parameters and dependencies required for the project. It includes the following functionality:

1. Imports necessary libraries and modules.
2. Connects to MongoDB Atlas using the specified URI and sets up a database and collection.
3. Initializes a directory loader to load data from text files in the `Sample_Files` directory.
4. Creates OpenAI embeddings and stores data in the MongoDB collection.
5. Defines a function (`query_data`) for performing similarity search and question-answering using vector search and RAG architecture.
6. Utilizes Gradio to create a user interface for interacting with the question-answering application.

### Usage

1. Run the script to configure key parameters and load data into MongoDB Atlas.
2. Utilize the `query_data` function to perform similarity search and question-answering.
3. Launch the Gradio user interface for a user-friendly experience.

**Note:** Ensure to replace placeholder values with actual keys and URIs for proper functionality.

## Usage Instructions

1. Refer to `README.md` for project-specific instructions and details.
2. Execute individual scripts (`extract_information.py`, `load_data.py`) based on the desired functionality.
3. Interact with the question-answering application through the Gradio user interface.

## Dependencies

- `pymongo`: MongoDB Python driver for interacting with MongoDB Atlas.
- `langchain`: A library for natural language processing tasks.
- `gradio`: A library for creating interactive user interfaces for machine learning models.

## Sample Files

The `Sample_Files` directory contains text files used for demonstration purposes. Users can customize and replace these files with their own data.

## Note

This documentation provides a high-level overview of the project structure, key files, and usage instructions. For detailed information on each script's functionality, refer to the code and comments within each file.


