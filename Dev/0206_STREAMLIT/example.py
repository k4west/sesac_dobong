import streamlit as st
import pandas as pd

st.title("hello, ssac")

table_data = {"Column 1": [1, 2], "Column 2": [3, 4]}

placeholder = st.empty()
isclick = st.button("delete button")
if isclick:
    placeholder = st.empty()
    placeholder.write(pd.DataFrame(data=table_data))
else:
    placeholder.empty()

# 여기서 커맨드라인에 실행
# streamlit run example.py
