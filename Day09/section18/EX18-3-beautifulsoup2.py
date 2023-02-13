import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
param = {}
response = requests.get(url, params=param)
html = response.text
print(html)

# soup = BeautifulSoup(html, 'html.parser')
#
# review_list = soup.find_all('div', class_='score_reple')
#
# for review in review_list:
#     print(review.find('p').text.strip())
