import streamlit as st

video = open("1041554251-preview.mp4", "rb")
video_bytes = video.read()

with st.form("form"):
    st.title("수영배우기")
    st.info("영상제목 : 시원한 수영")
    st.video(video_bytes)
    user_input = st.text_input("영상을 보신 소감은 어떠신가요?")
    submit = st.form_submit_button("클릭")
st.sidebar.selectbox("사이드바", ("자유영", "배영", "접영"))
