import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
url="https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response=requests.get(url=url)
content=response.text
soup=BeautifulSoup(content,"html.parser")
number=soup.select(".listicleItem_listicle-item__title__BfenH")
text=[number.getText() for number in number]
text=text[::-1]
with open("movies.txt",mode='w') as file:
    for text in text:
        file.write(f"{text}\n")



