import streamlit as st


# 버튼 사용 예시
btn = st.button("클릭")
if btn:
    st.write("버튼이 클릭되었습니다!")

# 텍스트 입력 예시
text_input = st.text_input("텍스트 입력")
if text_input:
    st.write(f"입력된 텍스트: {text_input}")

# 셀렉트박스 예시
option = st.selectbox("하나를 선택해주세요~", ["1번", "2번", "3번"])
st.write(f"선택된 옵션: {option}")

# 멀티 셀렉트박스 예시
options = st.multiselect("여러 개 선택 가능", ["A", "B", "C"])
if options:
    st.write(f"선택된 옵션들: {', '.join(options)}") # join() 메서드: 리스트의 요소들을 하나의 문자열로 합치는 메서드

# 파일 업로드
uploaded_file = st.file_uploader("파일을 업로드해주세요")
if uploaded_file:
    content = uploaded_file.read().decode("utf-8")
    st.write("업로드된 파일 내용:")
    st.text_area("File Content", content, height=200)
    st.write(f"파일 크기: {len(content)} bytes")

# 다운로드 버튼
data = """다운로드 할 데이터입니다.
이 내용이 파일로 다운로드 됩니다!
테스트~~~"""
st.download_button("다운로드", data=data, file_name="result.txt")
                   
