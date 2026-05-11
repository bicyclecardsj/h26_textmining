import urllib.request
import json

def crawl_naver_news(url, start=0, display=10):
    client_id = ""
    client_secret = ""
    url += f'&start={start}&display={display}'
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # news_data = json.load(response_body.decode('utf-8'))['item']
        json_str=response_body.decode('utf-8')
        py_data = json.loads(json_str)
        news_data = py_data['items']
        # print(news_data)
        return news_data, None
    else:
        # print("Error Code:" + rescode)
        return None, rescode

def crawl_naver_news_all(keyword):
    encText = urllib.parse.quote(keyword)
    start = 1
    display = 10
    url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과
    corpus = []
    while start <= 100: # 예시로 100까지 크롤링
        crawled_news, status = crawl_naver_news(url, start, display)
        if crawled_news:
            corpus += crawled_news
            start += display
        else:
            print("Error Code:" + status)
            break
    return corpus
