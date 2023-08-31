import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

reviews = soup.select('.api_txt_lines')
if reviews:
    first_review = reviews[0].text
    print("첫 번째 리뷰:", first_review)
else:
    print("리뷰를 찾을 수 없습니다.")