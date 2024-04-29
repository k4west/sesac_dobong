import streamlit as st
import pandas as pd

# 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")
if uploaded_file is not None:
    # 데이터프레임으로 변환
    df = pd.read_csv(uploaded_file)

    # 데이터프레임 표시
    st.write("업로드된 데이터:")
    st.dataframe(df)

    # 데이터 요약 정보 표시
    st.write("데이터 요약:")
    st.write(df.describe())

    # 데이터 시각화
    st.line_chart(df, y=df.columns[1])
    st.line_chart(df, y=df.columns[2])
