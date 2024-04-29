import streamlit as st

# 체크박스로 사용자 피드백 받기
feedback = st.checkbox("이 앱이 마음에 드나요?")

# 피드백에 따른 메시지 표시
if feedback:
    st.write("감사합니다! 😊")
    genre = st.radio("좋아하는 음악 장르는 무엇인가요?", ("팝", "록", "재즈"))
    st.write("선택한 장르:", genre)
else:
    st.write("피드백을 주셔서 감사합니다. 더 개선할 수 있도록 노력하겠습니다. 😢")
