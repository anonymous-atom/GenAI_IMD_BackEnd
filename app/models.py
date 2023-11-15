import os

print("Importing libraries...")
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationSummaryMemory
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chat_models import ChatOpenAI

print("Imported libraries.")


# Function to check internet connection


def gen_content(pdf_file):
    # Create environment variable for API key
    os.environ['OPENAI_API_KEY'] = "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"

    llm = ChatOpenAI()

    loader = UnstructuredPDFLoader(
        pdf_file, strategy="fast",
    )
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    all_splits = text_splitter.split_documents(data)

    vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())

    ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(
                "You are a smart instructor to help student in any subject/topic as an expert."
            ),
            # The `variable_name` here is what must align with memory
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{question}"),
        ]
    )

    memory = ConversationSummaryMemory(
        llm=llm, memory_key="chat_history", return_messages=True
    )

    retriever = vectorstore.as_retriever()

    qa = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)

    return qa


def ask_from_pdf(pdf_file, question):
    print("Initializing pdf bot...")
    qa = gen_content(pdf_file)
    print("Initialized pdf bot.")
    print("Asking question...")
    response = qa(question)
    print("Response received.")
    return response


ask_from_pdf('pdf-test.pdf', "Summarize the topic of this pdf file.")
