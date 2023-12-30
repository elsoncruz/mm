import streamlit as st
from index import ask
#with st.chat_message("assistant"):
#    st.write("Hello world")

#prompt=st.chat_input("say something")
#if prompt:
#    st.chat_message("user").markdown(prompt)
#    response = ask(prompt)
#    st.chat_message("assistant").markdown(response)
st.title("ChatBoT")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"]) 

if prompt := st.chat_input("say"):
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append({"role":"user","content": prompt})

    response=ask(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role":"assistant","content":response})    