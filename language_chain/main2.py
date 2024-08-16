# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
# from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import ctransformers


# chat_model = ChatOpenAI()  # 모델을 llama로 변경하기 위해 주석 처리
llm = ctransformers(
    model = 'llama-2-7b-chat.ggmlv3.q4_0.bin',
    model_type='llama'
)

st.title('Make a poem for only you')  # 원하는 제목 입력

content = st.text_input('Please write the concept the poem you want to make!')

if st.button('Make a poem!'):
    with st.spinner('Wait for it....'):
        result = llm.predict('please make a poem about the ' + content)
        st.write(result)
