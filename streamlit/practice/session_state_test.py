import streamlit as st

# ! counter 변수는 매 실행마다 초기화되기 때문에 클릭 수가 1에서 증가하지 않음
# couter = 0
# button = st.button("클릭")

# if button:
#     couter += 1

# st.write(f"버튼 클릭 수: {couter}")

# session_state에 'counter'가 없으면 0으로 초기화
if 'counter' not in st.session_state:
    st.session_state.counter = 0

button = st.button("클릭")

if button:
    st.session_state.counter += 1

st.write(f"버튼 클릭 수: {st.session_state.counter}")