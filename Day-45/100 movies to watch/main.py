import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")

movies = []

for tag in soup.find_all(name="h3", class_="title"):
    movies.append(tag.get_text())

movies.reverse()

with open("movies.txt", mode="w", encoding="UTF-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")