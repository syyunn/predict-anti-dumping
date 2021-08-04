"""
Cluster AD cases with common target products
"""

import pandas as pd

case_list = "../antidumping_us_itc_case_list.csv"
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





if __name__ == "__main__":
    pass
