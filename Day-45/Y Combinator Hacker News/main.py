from bs4 import *
import requests

URL = "https://news.ycombinator.com/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

articles_id = soup.find_all(name='tr', class_='athing')
max_score = 0
max_score_title = ""
for article in articles_id:
    sel_id = f"{article.get('id')}"
    news_title = soup.find(id=sel_id).select_one(selector=".titleline a").string
    news_link = soup.find(id=sel_id).select_one(selector=".titleline a").get("href")
    article_score = soup.find(name='span', id=f"score_{article.get('id')}")
    try:
        a = list(str(article_score.get_text()).split())
        if int(a[0]) > max_score:
            max_score = int(a[0])
            max_score_title = news_title
            max_score_href = news_link

    except AttributeError:
        print()

print("Highest Ranking News:")
print(f"News Title: '{max_score_title}'\nScore Point: '{max_score}'\nLink: {max_score_href}")