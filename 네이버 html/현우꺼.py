import requests
from bs4 import BeautifulSoup

review = {}
list_a = []
list_b = []

url = "<https://wwww.mangoplate.com/restaurants/aX2RxVCZYj>"
response = requests.get(url)

if response.status_code == 200:
	html = response.text
	soup = BeautifulSoap(html, 'html.parser')
	ul = soup.select_one('ul.RestaurantReviewList_ReviewList')
	con = ul.selct('li>a>div>p')

else:
	print(resonse.status_code)
