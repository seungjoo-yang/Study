# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title('인공지능 시인')  # 원하는 제목 입력

content = st.text_input('시를 작성할 주제를 작성해주세요!')

if st.button('시 만들어보기!'):
    with st.spinner('Wait for it....'):
        result = chat_model.predict(content + '에 대한 시를 써줘 ')
        st.write(result)
