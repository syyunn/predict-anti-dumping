import pandas as pd
from collections import defaultdict
from itc_code_desc import desc

csv = "team_trump/edis_orders_itc.csv"
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

fig, ax1 = plt.subplots()
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
            # SQL results
            sql_results = {
                '99': 17174,
                '00': 30997,
                '01': 31999,
                '02': 36515,
                '03': 39986,
                '04': 45805,
                '05': 46735,
                '06': 49235,
                '07': 50699,
                '08': 92451,
                '09': 97880,
                '10': 91836,
                '11': 86045,
                '12': 80089,
                '13': 76064,
                '14': 74260,
                '15': 73801,
                '16': 72878,
                '17': 75615,
                '18': 79289,
                '19': 79448,
                '20': 83658,
            }

            # Convert the keys and values to lists for plotting
            sql_years = list(sql_results.keys())
            sql_counts = list(sql_results.values())

             # Plotting the SQL data
            plt.plot(sql_years, sql_counts, label="Total Number of LD2 Reports")
            plt.gca().secondary_yaxis('right')  # Create a secondary y-axis on the right


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
                label="Number of LD2 Reports w/ Relevant Keywords)",
            )
        else:
            continue
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
