# 다음뉴스 목록 페이지에서 여러건의 뉴스(제목+본문) 수집
import requests
from bs4 import BeautifulSoup

url = "https://news.daum.net/breakingnews/digital"  # 뉴스 목록 URl

# 1.뉴스 목록 URl에서 1건의 뉴스 URl 추출
result = requests.get(url)  # 해당 URL의 전체 소스코드 get
soup = BeautifulSoup(result.text, "html.parser") # 전체소스코드 BS4 읽기!

title_list = soup.select("ul.list_news2 a.link_txt") # BS4로 뉴스제목 목록 추출

for i, title in enumerate(title_list):
    print(i, title)


    # TODO: 태그 목록에서 URL 추출 + 단건뉴스 수집