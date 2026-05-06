import streamlit as st
import mylib.myTextAnalyzer as ta
import mylib.myStreamlitVisulalizer as sv
from konlpy.tag import Okt

# 다음 영화 리뷰
datafile = r"D:\Lecture\TextMining26\Apps\WordFreqProj\data\daum_movie_review.csv"

# 1. 데이터 준비
corpus = ta.load_corpus(datafile, 'review')

# 2. 빈도수 만들기
my_tags = ['Noun', 'Verb', 'Adjective']
my_stopwords = ['영화', '하는', '정말', '진짜', '보고', '있는',  
                '보는', '입니다', '그냥', '정도', '봤는데', '봤습니다',
                '같은', '합니다', '봤어요','한번', '없는', '해서', '이런',
                '보면']
counter = ta.count_word_freq(corpus, Okt().pos, my_tags, my_stopwords)

# 3. 수평 막대그래프
sv.visualize_barh_graph(counter, 20)

# 4. 워드클라우드
sv.visualize_wordcloud(counter, 50)