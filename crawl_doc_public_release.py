import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame()

last_page = 30

for page in range(last_page):
    url = f"https://www.commerce.gov/index.php/news/61?q=/index.php/news/61&issues%5B52%5D=52&page={page}"
    req = requests.get(url)
    bs = BeautifulSoup(req.text)
    h2s = bs.findAll("h2")
    for h2 in h2s:
        try:
            headline = h2.find("a").find("span").text.strip()
            print(headline)
            pass
            date = (
                h2.find_next("div")
                .find("div")
                .find("time")
                .text.replace('"', "")
                .strip()
            )
            print(date)
            pass
            data = {"headline": headline, "date": date}
            df = df.append(data, ignore_index=True)
        except AttributeError:
            pass

fname = "doc_public_release_headlines"
df.to_csv(f"./{fname}.csv", sep=",", index=False)

if __name__ == "__main__":
    pass
