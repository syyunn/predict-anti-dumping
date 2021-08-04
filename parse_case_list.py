import pandas as pd
from tqdm import tqdm

path = "./data/case_list_20200911.xlsx"
df = pd.read_excel(path)

fname = 'antidumping_us_itc_case_list'
df.to_csv(f"./{fname}.csv", sep=",", index=False)


if __name__ == "__main__":
    pass

