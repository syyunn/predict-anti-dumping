import pandas as pd
from tqdm import tqdm

path = "./data/us_imposed_ads.xlsx"
df = pd.read_excel(path)
df_result = pd.DataFrame()

for index, row in tqdm(df.iterrows()):
    hs_codes = str(row["HS"]).split(",")
    for i, code in enumerate(hs_codes):
        data = {
            "measure_description": row["Measure description"].strip(),
            "member_imposing": row["Member imposing"].strip(),
            "partner_affected": row["Partner affected"].strip(),
            "product_description": row["Product description"].strip(),
            "hs_ordi": i + 1,
            "hs": code.strip(),
            "initiation_year": row["Initiation"].year,
            "initiation_month": row["Initiation"].month,
            "initiation_date": row["Initiation"].day,
        }
        df_result = df_result.append(data, ignore_index=True)
        # break
        pass
    # break
# change types to integer
df_result = df_result.fillna(0)
df_result["hs_ordi"] = pd.to_numeric(df_result["hs_ordi"], downcast='integer')
df_result["initiation_year"] = pd.to_numeric(df_result["initiation_year"], downcast='integer')
df_result["initiation_date"] = pd.to_numeric(df_result["initiation_date"], downcast='integer')
df_result["initiation_month"] = pd.to_numeric(df_result["initiation_month"], downcast='integer')
dtypes = df_result.dtypes


fname = 'us-imposed-anti-dumpings'
df_result.to_csv(f"./{fname}.csv", sep=",", index=False)


if __name__ == "__main__":
    pass
