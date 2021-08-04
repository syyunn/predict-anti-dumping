"""
Check whether the saved file name equals to its case_number included in the crawled html.
"""
petitions_dir_path = '../data/petitions'

from os import listdir
from os.path import isfile, join

from tqdm import tqdm
from bs4 import BeautifulSoup

petitions_dir = '../data/petitions'
html_paths = [join(petitions_dir, f) for f in listdir(petitions_dir) if isfile(join(petitions_dir, f))]


wrong_paths = []
for html_path in tqdm(html_paths):
    if '.DS_Store' not in html_path:
        try:
            with open(html_path, "r", encoding="utf-8") as f:
                html = f.read()
                bs = BeautifulSoup(html)
                span_with_casenumber = bs.find("span", {"id": "ctl00_ctl00_ContentPlaceHolder1_maincontent1_lblSearchQuery"})
                case_number = span_with_casenumber.text.replace('Case Number=', "").replace("Document Type=Petition", "")
                actual_case_number = html_path.split("/")[-1].replace(".htm", "")
                if case_number != actual_case_number:
                    wrong_paths.append(html_path)
        except:
            wrong_paths.append(html_path)

print(wrong_paths)


if __name__ == "__main__":
    pass

