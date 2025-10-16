import streamlit as st

# 실행
# streamlit run app.py

# 텍스트 표시
st.title("제목")
st.header("헤더")
st.subheader("서브헤더")
st.text("일반 텍스트")
st.markdown("마크다운 적용 *이텔릭체*, **굵은 글씨**")
st.caption("캡션 텍스트")
st.code("print('Hello, Streamlit!')", language='python')
st.latex(r''' e^{i\pi} + 1 = 0 ''')  # 수식 표시

# write 함수만으로도 다양하게 표현 가능
st.write("일반적인 텍스트입니다")
st.write("이건 마크다운 **강조**")
st.write("# 제목1")
st.write("## 제목 2")
st.write("### 제목 3")

test1 = 123
test2 = [
    1,
    2,
    3
]

test3 ={"이름": "홍길동", "나이": 29}

st.write(test1)
st.write(test2)
st.write(test3)

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


# ---
# 위젯

# 입력 위젯
st.text_input("텍스트")
st.text_area("긴 텍스트")
st.number_input("숫자", min_value=0, max_value=100)
st.slider("슬라이더", 0, 100, 50)
st.select_slider("선택 슬라이더", options=[1, 2, 3, 4, 5])

# 선택 위젯
st.selectbox("드롭다운", ["A", "B", "C"])
st.multiselect("다중 선택", ["A", "B", "C"])
st.radio("라디오 버튼", ["옵션1", "옵션2"])
st.checkbox("체크박스")

# 날짜/시간
st.date_input("날짜 선택")
st.time_input("시간 선택")

# 파일
st.file_uploader("파일 업로드")
st.camera_input("카메라 입력")

# 버튼
st.button("일반 버튼")
st.link_button("링크 버튼", url="https://www.example.com")
st.form_submit_button("폼 제출")
st.download_button("다운로드", data="내용", file_name="file.txt")

# 기타
st.color_picker("색상 선택")