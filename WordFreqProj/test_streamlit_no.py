import streamlit as st

st.header("사용자 입력 폼")

name = st.text_input("이름", placeholder="이름을 입력하세요")
age = st.number_input("나이", 1, 100, 1, 1)
agree = st.checkbox("약관에 동의합니다")

if st.button("제출"): 
    st.write(f"이름: {name}, 나이: {age}")
    
    if agree:
        st.success("약관에 동의했습니다.")
    else:
        st.warning("약관 동의가 필요합니다.")
