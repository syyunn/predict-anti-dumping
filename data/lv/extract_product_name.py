import pandas as pd
from data.lv.bert_utils import QuestionAnsweringModel
from random import shuffle

path = "./dumping_keyworded_issue_text.csv"
df = pd.read_csv(path)

question_regarding_dumped_product = (
    "Which product matters regarding dumping or anti-dumping?"
)
question_regarding_dumping_country = (
    "Which country produced with a relation to dumping, antidumping or anti-dumping?"
)

issue_texts = df['issue_text'].drop_duplicates().to_list()
shuffle(issue_texts)

model = QuestionAnsweringModel()

for issue_text in issue_texts:
    # issue_text_fragments = []
    # issue_text_fragments_semicolon = issue_text.split(';')
    # for fragment in issue_text_fragments_semicolon:
    #     issue_text_fragments += fragment.split('\n')
    # products = []
    # countries = []
    # for fragment in issue_text_fragments:
    #     products = model.predict(
    #         "Which product(s) are related to dumping, anti-dumping or antidumping?", fragment
    #     )
    #     countries = model.predict(f"Which countries are producer of the {products}?", fragment,)
    #     for_or_against = model.predict(
    #         f"Is it for or against antidumping duties levied for {products}", fragment
    #     )
    try:
        # products = model.predict(
        #     "Is it containing information related to dumping, antidumping or anti-dumping", issue_text
        # )
        #
        products = model.predict(
            "Which products are related to dumping, anti-dumping or antidumping?", issue_text
        )
        countries = model.predict(f"From which country {products} are produced?", issue_text, )
        for_or_against = model.predict(
            f"Is it for or against antidumping duties levied for {products}", issue_text
        )
        pass
    except RuntimeError:
        print(RuntimeError)
        pass

if __name__ == "__main__":
    pass
