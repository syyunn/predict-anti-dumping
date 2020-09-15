"""
Extract all symbol and corresponding names from crawled htmls
"""
import os
from os import listdir
from os.path import isfile, join

from tqdm import tqdm
from bs4 import BeautifulSoup
import pandas as pd

nyse_listings_dir = "/Users/suyeol/Downloads/nyse"

nyse_symbol_name_df = pd.DataFrame()
for page in tqdm(range(1, 656)):
    html_path = os.path.join(nyse_listings_dir, str(page) + ".htm")
    print(html_path)
    with open(html_path) as f:
        crawled_page_info = html_path.split("/")[-1].replace(".htm", "")
        bs = BeautifulSoup(f)
        paginated_as = bs.findAll("li", {"class": "disabled"})[0].text
        if page == 1:
            paginated_as = "1"
        if crawled_page_info != str(1):
            assert paginated_as == str(crawled_page_info), "page order broken"

        table = bs.find("table", {"class": "table"})
        trs = table.findAll("tr")
        for tr in trs:
            if len(tr.findAll("th")) > 0:
                pass
            else:
                tds = tr.findAll("td")
                assert len(tds) == 2, "something went wrong for len(2) validation"
                symbol = None
                name = None
                for idx, td in enumerate(tds):
                    if idx == 0:
                        symbol = td.text
                    elif idx == 1:
                        name = td.text
                data = {"symbol": symbol, "name": name, "page": paginated_as}
                print(data)
                nyse_symbol_name_df = nyse_symbol_name_df.append(
                    data, ignore_index=True
                )
nyse_symbol_name_df = nyse_symbol_name_df[['symbol', 'name', 'page']]
nyse_symbol_name_df.to_csv(f"./nyse_symbol_name_match_list.csv", sep=",", index=False)


if __name__ == "__main__":
    pass
