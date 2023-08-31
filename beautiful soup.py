import requests
from bs4 import BeautifulSoup

url = "https://map.naver.com/p/search/%EB%8C%80%EC%A0%84%20%EC%9C%A1%ED%98%95%EC%A0%9C/place/1323045327?placePath=?entry=pll&from=nx&fromNxList=true&c=15.00,0,0,0,dh"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

review_element = soup.select_one('.zPfVt')
if review_element:
    review_text = review_element.get_text(strip=True)
    print("추출된 리뷰 내용:")
    print(review_text)
else:
    print("리뷰를 찾을 수 없습니다.")