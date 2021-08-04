"""
Check whether the saved file name equals to its case_number included in the crawled html.
"""
import pandas as pd

df = pd.DataFrame()

petitions_dir_path = "../data/petitions"

from os import listdir
from os.path import isfile, join

from tqdm import tqdm
from bs4 import BeautifulSoup

petitions_dir = "../data/petitions"
htmls_path = [
    join(petitions_dir, f)
    for f in listdir(petitions_dir)
    if isfile(join(petitions_dir, f))
]


import datetime


def make_result_dict_and_its_reverse(case_list="../antidumping_us_itc_case_list.csv"):
    import pandas as pd

    df = pd.read_csv(case_list)

    from collections import defaultdict

    result_dict = defaultdict(list)
    reverse_result_dict = defaultdict()

    for index, row in df.iterrows():
        case_number = row["Case Number"]
        case_title = row["Case Title"].split("From")[0].strip()
        result_dict[case_title].append(case_number)

    for key, values in result_dict.items():
        for value in values:
            reverse_result_dict[value] = key
    return result_dict, reverse_result_dict


result_dict, reverse_result_dict = make_result_dict_and_its_reverse()
case_cluster = reverse_result_dict["A-570-928"]
linked_cases = result_dict[case_cluster]

# for html_path in tqdm(htmls_path):
date_unknown_cases = []
for html_path in htmls_path:
    # html_path = '/Users/suyeol/predict-anti-dumping/data/petitions/C-570-076.htm'
    if ".DS_Store" not in html_path:
        with open(html_path, "r", encoding="utf-8") as f:
            html = f.read()
            bs = BeautifulSoup(html)
            tds = bs.findAll("td")
            if len(tds) >= 10:
                case_number = html_path.split("/")[-1].replace(".htm", "").strip()
                petition_date_str = tds[10].text.replace("\n", "").strip()
                petition_date = datetime.datetime.strptime(
                    petition_date_str, "%m/%d/%y"
                )
                print(case_number, petition_date)
                data = {"case_number": case_number, "petition_date": petition_date}
                df = df.append(data, ignore_index=True)
            else:
                case_number = html_path.split("/")[-1].replace(".htm", "").strip()
                data = {"case_number": case_number, "petition_date": None}
                df = df.append(data, ignore_index=True)
                date_unknown_cases.append(case_number)

print(len(date_unknown_cases))

# for case in date_unknown_cases:
#     case_cluster = reverse_result_dict[case]
#     linked_cases = result_dict[case_cluster]
#     for linked_case in linked_cases:
#         found = df.loc[df["case_number"] == linked_case]
#         if found.shape[0] == 1:
#             petition_date = found["petition_date"].iloc[0]
#             data = {"case_number": case, "petition_date": petition_date}
#             df = df.append(data, ignore_index=True)
#             date_unknown_cases.remove(case)
#             break
# print(len(date_unknown_cases))

# for case in date_unknown_cases:
#     data = {"case_number": case, "petition_date": None}
#     df = df.append(data, ignore_index=True)

fname = "petition_date"
df.to_csv(f"./{fname}.csv", sep=",", index=False)
if __name__ == "__main__":
    pass
