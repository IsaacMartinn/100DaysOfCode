from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

web_page = response.text

soup = BeautifulSoup(web_page,"html.parser")
articles = [article.getText() for article in soup.find_all(name="h3",class_="title")[::-1]]

for article in articles:
    with open("movies.txt",mode="a") as file: 
        file.write(f"{article}\n") 
