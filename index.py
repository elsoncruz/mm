#from langchain.document_loaders import PyPDFLoader
import streamlit as st
#loader= PyPDFLoader("python.pdf")
#pages_content=loader.load_and_split()
#print(len(pages_content),pages_content)

pass={
    "authorization":st.secrets["api_key"],
    "content-type":"application/jason"
}

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

embeddings=OpenAIEmbeddings(api_key=pass)
#db=FAISS.from_documents(pages_content,embeddings)

#db.save_local("faiss_index")

new_db=FAISS.load_local("faiss_index",embeddings)


from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
llm= ChatOpenAI(api_key=pass)

qa_chain=RetrievalQA.from_chain_type(llm,retriever=new_db.as_retriever())
def ask(user_query):
    res=qa_chain({"query":user_query})
    return res["result"]
