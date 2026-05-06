import streamlit as st
import NaverNewsCrawler as nnc 
import pandas as pd

st.title('네이버 뉴스 크롤링')
keyword = st.text_input('검색할 키워드를 입력하세요:')

if st.button('데이터 가져오기'):
    if keyword:
        with st.spinner('데이터를 가져오는 중...'):
            corpus = nnc.crawl_naver_news_all(keyword)
            
            if corpus:
                st.success(f"'{keyword}' 검색 완료! 총 {len(corpus)}건의 데이터를 확보했습니다.")
                
                df_raw = pd.DataFrame(corpus)
                
                csv_data = df_raw.to_csv(index=False, encoding='utf-8-sig')
                
                st.download_button(
                    label="CSV 다운로드",
                    data=csv_data,
                    file_name=f"naver_news_{keyword}.csv",
                    mime="text/csv"
                )

                with st.expander("데이터 전체 보기"):
                    st.json(corpus)
                    
            else:
                st.error("데이터를 불러오는 데 실패했습니다.")
    else:
        st.warning("키워드를 입력해 주세요.")