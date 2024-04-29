import streamlit as st
import pandas as pd
import time

st.write("안녕하세요, Streamlit!")

df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
st.dataframe(df)

chart_data = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=["a", "b", "c"])
st.line_chart(chart_data)

map_data = pd.DataFrame({"lat": [37.7749, 38.7749], "lon": [-122.4194, -123.4194]})
st.map(map_data)

age = st.slider("나이", 0, 130, 25)
st.write("선택한 나이는", age, "살입니다.")

option = st.sidebar.selectbox("좋아하는 숫자를 선택하세요.", ["1", "2", "3"])
st.write("선택한 숫자:", option)

progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress_bar.progress(i + 1)

uploaded_file = st.file_uploader("파일을 선택하세요", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

if st.button("안녕하세요 버튼"):
    st.write("버튼이 클릭되었습니다.")

color = st.color_picker("색상을 선택하세요")
st.write("선택한 색상:", color)

genre = st.radio("좋아하는 음악 장르는 무엇인가요?", ("팝", "록", "재즈"))
st.write("선택한 장르:", genre)

agree = st.checkbox("이용 약관에 동의합니다.")
if agree:
    st.write("동의하셨습니다.")

option = st.selectbox("좋아하는 숫자를 선택하세요:", [1, 2, 3, 4, 5])
st.write("선택한 숫자:", option)

options = st.multiselect(
    "좋아하는 색상을 선택하세요:",
    ["녹색", "빨간색", "파란색", "노란색"],
    ["녹색", "빨간색"],
)
st.write("선택한 색상:", options)

st.download_button(
    label="Download data as CSV",
    data="example,csv,data",
    file_name="data.csv",
    mime="text/csv",
)

st.video("https://www.youtube.com/watch?v=J---aiyznGQ")

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/2/2c/Rotating_earth_%28large%29.gif"
)

code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language="python")

st.markdown("Streamlit is **_really_ cool**.")

st.balloons()
