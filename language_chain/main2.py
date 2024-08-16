# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
# from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import CTransformers


# chat_model = ChatOpenAI()  # 모델을 llama로 변경하기 위해 주석 처리
llm = CTransformers(
    model = 'llama-2-7b-chat.ggmlv3.q4_0.bin',
    model_type='llama'
)

st.title('달무티 화이팅')  # 원하는 제목 입력

content = st.text_input('시를 작성할 주제를 작성해주세요!')

if st.button('시 만들어보기!'):
    with st.spinner('Wait for it....'):
        result = llm.predict(content + '에 대한 시를 써줘 ')
        st.write(result)
