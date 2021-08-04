import pandas as pd
from collections import defaultdict
from team_trump.itc_code_desc import desc

csv = "./edis_orders_itc.csv"
df = pd.read_csv(csv)

prod_codes = list(set(df["Product Group"].tolist())) + ['IS']
prod_codes_to_plot = ["IS"]

years = []
prods = defaultdict(list)
for i, row in df.iterrows():
    year_cands = str(row["Order date"]).split("/")
    prdgrp = row["Product Group"]
    for cand in year_cands:
        if len(cand) == 4:
            years.append(cand[2:])
            prods[cand[2:]].append(prdgrp)

from collections import Counter

# petitions
years_keys = Counter(years).keys()  # equals to list(set(words))
years_counts = list(Counter(years).values())  # counts the elements' frequency

prod_code_counts = defaultdict(list)
for key in prods.keys():
    for code in prod_codes:
        prod_code_counts[code].append(prods[key].count(code))

IS = [
    sum(i)
    for i in zip(
        prod_code_counts["ISP"], prod_code_counts["ISM"], prod_code_counts["ISO"]
    )
]

prod_code_counts["IS"] = IS

# plotting
import matplotlib.pyplot as plt

plt.figure(1, figsize=(10, 6))
plt.plot(years_keys, years_counts, label="ITC AD/CVD orders")
for code in prod_codes:
    if str(code) in list(desc.keys()):
        plt.plot(
            years_keys,
            prod_code_counts[code],
            label=str(code) + " : " + desc[str(code)],
        )
    else:
        # plt.plot(years_keys, prod_code_counts[code], label=code)
        pass

plt.xlabel("Year")
plt.ylabel("Number of ITC's AD/CVD Orders")
plt.title(" USITC's AD/CVD Orders by Product Group")

plt.legend(loc="upper left")

plt.show()

plt.close()

# per industry plotting
# prod_codes_to_plot = ["IS", "CH", "AG", "MM", "ME", "TX"]
prod_codes_to_plot = prod_codes
for code in prod_codes_to_plot:
    if str(code) != 'nan':
        plt.figure(1, figsize=(10, 6))
        plt.plot(years_keys, years_counts, label="ITC AD/CVD orders")
        try:
            plt.plot(
                years_keys, prod_code_counts[code], label=str(code) + " : " + desc[str(code)]
            )
        except KeyError:
            plt.plot(
                years_keys, prod_code_counts[code], label=str(code)
            )

        if code == "IS":
            plt.plot(
                years_keys,
                [0 for i in range(17)]
                + [
                    1,
                    2,
                    2,
                    1,
                    1,
                    2,
                    14,
                    62,
                    42,
                    20,
                    21,
                    30,
                    28,
                    32,
                    25,
                    26,
                    25,
                    39,
                    38,
                    36,
                ],
                label="Number of LD2 Reports",
            )
        # x coordinates for the lines
        xcoords = ["01", "09", "17", "2020"]
        # colors for the lines
        colors = ["r", "k", "b"]

        for xc, c in zip(xcoords, colors):
            plt.axvline(x=xc, c="gray", linestyle="--")
        # plt.axvline(x="07", c="red", linestyle="--")

        # plt.arrow('08', 40, -6, 0, head_width=1, head_length=0.5, linewidth=1, color='black', length_includes_head=True)
        # plt.arrow('08', 40, 0.5, 0, head_width=1, head_length=0.5, linewidth=1, color='black', length_includes_head=True)

        plt.xlabel("Year")
        plt.ylabel("Number of ITC's AD/CVD Orders")
        plt.title(" USITC's AD/CVD Orders by Product Group")

        plt.legend(loc="upper left")

        plt.show()

        plt.close()

# granger causality
import statsmodels.api as sm
from statsmodels.tsa.stattools import grangercausalitytests
import numpy as np

data = sm.datasets.macrodata.load_pandas()
data = data.data[["realgdp", "realcons"]].pct_change().dropna()

ld2_steel_reports = [0 for i in range(17)] + [
    1,
    2,
    2,
    1,
    1,
    2,
    14,
    62,
    42,
    20,
    21,
    30,
    28,
    32,
    25,
    26,
    25,
    39,
    38,
    36,
]

df = pd.DataFrame()
df['IS'] = IS[21:]
df['LD2'] = ld2_steel_reports[21:]

gc_res = grangercausalitytests(df, 4)

if __name__ == "__main__":
    pass
