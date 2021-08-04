
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

if __name__ == "__main__":
    pass
