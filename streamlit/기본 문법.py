import streamlit as st

# 실행
#streamlit run app.py

# 텍스트 표시
st.title("제목")
st.header("헤더")
st.subheader("서브헤더")
st.text("일반 텍스트")
st.markdown("**굵은 글씨**")
st.write("만능 출력 함수")

# ---

# 사용자 입력 받기
# 텍스트 입력
name = st.text_input("이름을 입력하세요")

# 숫자 입력
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)

# 슬라이더
value = st.slider("값을 선택하세요", 0, 100, 50)

# 선택 박스
option = st.selectbox("선택하세요", ['옵션1', '옵션2', '옵션3'])

# 버튼
if st.button("클릭"):
    st.write("버튼이 클릭되었습니다!")

# ---

# 레이아웃 구성
# 컬럼 나누기
col1, col2 = st.columns(2)

with col1:
    st.header("왼쪽 컬럼")
    st.write("내용1")

with col2:
    st.header("오른쪽 컬럼")
    st.write("내용2")

# 사이드바
st.sidebar.title("사이드바")
option = st.sidebar.selectbox("메뉴", ['홈', '설정', '정보'])

# ---

# 데이터 시각화
# 데이터 표시
import pandas as pd

df = pd.DataFrame({
    '이름': ['철수', '영희', '민수'],
    '나이': [25, 30, 35]
})

st.dataframe(df)  # 인터랙티브 테이블
st.table(df)      # 정적 테이블

# 차트 그리기
import numpy as np

# 라인 차트
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

# 막대 차트
st.bar_chart(chart_data)
