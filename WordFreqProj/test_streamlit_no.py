import streamlit as st

with st.form('my_from'):
    st.subheader("사용자 입력 폼")

    name = st.text_input("이름")
    age = st.number_input("나이", min_value=1, step=1)
    agree = st.checkbox("약관에 동의합니다")

    submitted = st.form_submit_button('submit')

if submitted: 
    st.write(f"이름: {name}, 나이: {age}")
    
    if not name:
        st.warning('이름을 작성해주세요')
    else:
        if agree:
            st.success("약관에 동의했습니다.")
        else:
            st.warning("약관 동의가 필요합니다.")