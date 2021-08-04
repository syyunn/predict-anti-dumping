import pandas as pd
from tqdm import tqdm

path = "./data/us_imposed_ads.xlsx"
df = pd.read_excel(path)
df = df.astype(object).where(pd.notnull(df), None)

fname = 'us-imposed-anti-dumpings_ver2'
df.to_csv(f"./{fname}.csv", sep=",", index=False)


if __name__ == "__main__":
    pass
