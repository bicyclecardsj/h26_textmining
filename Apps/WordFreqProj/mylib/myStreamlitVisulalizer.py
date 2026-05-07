import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from matplotlib import font_manager, rc

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

def visualize_barh_graph(counter, num_word):
    top_words = counter.most_common(num_word)
    word_list = [word for word, _ in top_words]
    count_list = [count for _, count in top_words]
    fig, ax = plt.subplots()
    ax.barh(word_list[::-1], count_list[::-1])  
    ax.set_title('빈도수 그래프')
    ax.set_xlabel('빈도수')
    ax.set_ylabel('단어')
    st.pyplot(fig)

def visualize_wordcloud(counter, num_word):
    wc = WordCloud(
        font_path=font_path,
        background_color='ivory',
        max_words = num_word,
        width=800,
        height=400
    ).generate_from_frequencies(counter)
    fig, ax = plt.subplots()
    ax.imshow(wc)
    ax.axis('off')
    st.pyplot(fig)