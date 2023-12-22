"""
This app answers questions based on custom data using vector search and openai

    Packages:
        pip install langchain pymongo bs4 openai tiktoken gradio requests lxml argparse unstructured
"""

from pymongo import MongoClient
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.document_loaders import DirectoryLoader
from langchain.llms import OpenAI
from langchain.chains import RetrievelQA
import gradio as gr
from gradio.themes.base import Base
import key_param

client = MongoClient(key_param.MONGODB_URI)
dbName = "langchain_demo"
collectionName = "collection_of_text_blobs"
collection = client[dbName][collectionName]

# Initialize the directory loader 
loader  = DirectoryLoader('./Sample_Files', glob="./*.txt", show_progress=True)
data = loader.load()

embeddings = OpenAIEmbeddings(openai_api_key = key_param.openai_api_key)
# store the data to mongodb collection
vectorStore = MongoDBAtlasVectorSearch.from_documents(data, embeddings, collection=collection)


# 2. Second step
embeddings = OpenAIEmbeddings(openai_api_key = key_param.openai_api_key)
vectorStore = MongoDBAtlasVectorSearch(collection, embeddings)

def query_data(query):
    docs = vectorStore.similarity_search(query, K=1)
    as_output = docs[0].page_content

    llm = OpenAI(openai_api_key=key_param.openai_api_key, temperature=0)
    retriever = vectorStore.as_retriever()
    qa = RetrievelQA.from_chain_type(llm, chain_type="stuff", retriever=retriever)
    retriever_output = qa.run(query)

    return as_output, retriever_output


with gr.Blocks(theme=Base(), title="Question answering app using vector search + RAG") as demo:
    gr.Markdown(
        """
        # Question Answering App using atlas Vector search + RAG architecture
        """)
    textbox = gr.Textbox(label="Enter your question: ")
    with gr.Row():
        button = gr.button("Submit", variant="Primary")
    with gr.Column():
        output1 = gr.Textbox(lines=1, max_lines=10, label= "Output with just Atlas Vector Search (return text field as is)")
        output2 = gr.Textbox(lines=1, max_lines=10, label= "Output generated by chaining Atlas Vector Search to langchain's RetrieverQA + OpenAI LLM:")
    button.click(query_data, textbox, outputs=p[output1, output2])

demo.launch()