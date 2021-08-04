import pandas as pd
from collections import defaultdict

csv = "./caselist_w_petition_date.csv"
df = pd.read_csv(csv)

clusters = []
curr_clusters_case_title = None
curr_cluster = []
for i, row in df.iterrows():
    case_number = row["case_number"]
    title = row["case_title"]
    petition_date = row["petition_date"]
    title_wo_country_name = title.split("From")[0].strip()

    if i == 0:
        curr_clusters_case_title = title_wo_country_name
        curr_cluster.append((case_number, title, petition_date))
    else:
        if curr_clusters_case_title == title_wo_country_name:
            curr_cluster.append((case_number, title, petition_date))
        else:
            clusters.append(curr_cluster)
            curr_clusters_case_title = title_wo_country_name
            curr_cluster = []
            curr_cluster.append((case_number, title, petition_date))

    pass

years = []
for cluster in clusters:
    year = cluster[0][2][:4]
    years.append(year)

years_non_clustered = []
for i, row in df.iterrows():
    year = row['petition_date'][:4]
    years_non_clustered.append(year)


from collections import Counter

# petitions
years_keys = Counter(years).keys()  # equals to list(set(words))
years_counts = list(Counter(years).values()) # counts the elements' frequency

# petitions_non_clustered
years_keys_nc = Counter(years_non_clustered).keys()  # equals to list(set(words))
years_counts_nc = list(Counter(years_non_clustered).values()) # counts the elements' frequency


# ld2 w/ dumping
ld2_years = years_keys
ld2_counts = [152, 143, 165, 160, 192, 142, 148, 204, 212, 141]

import matplotlib.pyplot as plt

plt.plot(years_keys_nc, years_counts_nc)
plt.plot(years_keys, years_counts)
# plt.plot(ld2_years, ld2_counts)

plt.show()

import numpy as np
from scipy import stats
# data = np.array([years_counts, ld2_counts])
corr = np.corrcoef(x=np.array(years_counts), y=np.array(ld2_counts))
spearmanr = stats.spearmanr(a=np.array(years_counts), b= np.array(ld2_counts))
if __name__ == "__main__":
    pass
