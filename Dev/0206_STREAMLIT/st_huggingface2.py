from transformers import pipeline
import streamlit as st

st.title("텍스트 요약기")

input = st.text_input("요약하고 싶은 원문을 넣으세요.")
st.button("클릭")

summarizer = pipeline("summarization", model="ainize/kobart-news")

# percent = str(round(result[0]["score"], 3) * 100) + "%"
# result = result[0]["label"]

with st.spinner("요약기가 원문을 요약중입니다."):
    result = summarizer(input, max_length=80, min_length=30)[0]["summary_text"]
    print(result)
    st.write("---" * 30)
    st.write("입력값:", input)
    st.write("요약문:")
    st.write(result)
