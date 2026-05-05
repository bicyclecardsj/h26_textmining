import streamlit as st
import pandas as pd
import time

st.title("Hello, Streamlit World")

name = "Jonghee"
st.title(f"Hello, {name}~~~~ Welcome to Streamlit World!!!")

# Streamlit 기본 API 살펴보기
# Wite, Magic Command
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
})

df # st.write()없어도 출력

# Text 출력
@st.cache_data
def change_text2():
    text = st.title('텍스트가 변할 겁니다.')
    time.sleep(2)
    text = text.info('2초가 지났습니다.')

change_text2()

st.success('와우성공')
st.warning('비이이사아앙')
st.error('심각한 오류')
st.header('이건 뭐지')
st.subheader('더 작네')
st.text('일반이네')

# Input widgets
if st.button('버튼'):
    st.success('clicked button')

choice_radio = st.radio('머신러닝 방법1', ['신경망', '랜덤포레스트', 'SVM'])
st.info(f'나의 선택 : {choice_radio}')

st.checkbox('토큰화')

choice_selectbox = st.selectbox('머신러닝 방법2', ['신경망', '랜덤포레스트', 'SVM'])
st.info(f'{choice_selectbox}')

choice_mul_selectbox = st.multiselect('머신러닝 방법3', ['신경망', '랜덤포레스트', 'SVM'])
st.info(choice_mul_selectbox)

num_slider = st.slider('가중치', 0, 10, 1)
st.info(f'가중치 : {num_slider}')

st.text_input('텍스트입력')

st.number_input('숫자입력')

# 사용자 입력 폼 만들기
st.header('사용자 입력 폼')
with st.form('regist'):
    name = st.text_input('이름')
    age = st.number_input('나이', min_value=1, max_value=100)
    agree = st.checkbox('약관에 동의합니다.')
    
    submitted = st.form_submit_button('제출')

if submitted:
    if agree:
        st.text(f'이름:{name}, 나이:{age}') 
        st.success('약관에 동의했습니다.')
    else: st.error('약관에 동의하세요')

# sidebar 입력 폼 만들기
st.sidebar.header("설정")
name = st.sidebar.text_input("이름을 입력하세요.")
age = st.sidebar.slider('나이', 0, 120, 1)
color = st.sidebar.selectbox('좋아하는 색상을 선택하세요.', ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라'])

# streamlit의 code 실행 방식 (Data Flow) decorater - 함수가 어떤건지 알려주는것
@st.cache_data
def change_text():
    text = st.title('텍스트가 변할 겁니다.')
    time.sleep(3)
    text = text.info('3초가 지났습니다.')

change_text()

# Streamlit에서 matplotlib, wordcloud 사용
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "c:/Windows/Fonts/malgun.ttf" # 한글 연결 해야함
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# matplotlib 이용해서 그래프 만들기
x = ['John', 'Mary', 'Chris', 'Steven', 'Evans']
y = [80, 72, 55, 90, 60]

fig1, ax1 = plt.subplots()
ax1.barh(x[::-1], y[::-1])
plt.title('수학점수')
plt.xlabel('점수')
plt.ylabel('이름')

st.pyplot(fig1)

# wordcloud 사용해보기
from wordcloud import WordCloud
st.title('워드클라우드')

text = "파이썬 스트림릿 데이터 분석 시각화 머신러닝 워드클라우드 파이썬 시각화 파이썬 스트림릿 워드클라우드 맷플롯 스트림릿"

wc = WordCloud(
    font_path=font_path,
    background_color="ivory",
    width=800,
    height=400
).generate(text)

fig2, ax2 = plt.subplots()
ax2.imshow(wc)
ax2.axis('off')

st.pyplot(fig2)