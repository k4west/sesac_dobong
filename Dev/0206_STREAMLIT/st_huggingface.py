from transformers import pipeline
import streamlit as st

st.title("감성분류기")

input = st.text_input("당신의 기분을 입력하세요.")
st.button("클릭")

sentiment_analysis = pipeline(
    "sentiment-analysis", model="monologg/koelectra-base-finetuned-nsmc"
)
result = sentiment_analysis(input)
percent = str(round(result[0]["score"], 3) * 100) + "%"
result = result[0]["label"]

with st.spinner():
    if result == "positive":
        st.write("---" * 30)
        st.write(input, percent)
        st.write("건강한 청년이구만")
    else:
        st.write("---" * 30)
        st.write(input, percent)
        st.write("위험하구만")
