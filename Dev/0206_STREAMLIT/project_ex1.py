import streamlit as st

# 사용자에게 옵션 선택 요청
option = st.selectbox(
    "어떤 작업을 수행할까요?", ["풍선 표시", "인사말 표시", "숫자 표시"]
)

# 선택에 따른 동작
if option == "풍선 표시":
    st.balloons()
elif option == "인사말 표시":
    st.markdown("### 안녕하세요! Streamlit을 사용해주셔서 감사합니다!")
elif option == "나이 표시":
    number = st.slider("나이를 선택하세요", 0, 100, 50)
    st.write("선택한 나이:", number)
