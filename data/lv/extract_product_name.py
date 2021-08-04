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

issue_texts = df["issue_text"].to_list()
client_names = df["client_name"].to_list()
dates_received = df["date_received"].to_list()

# shuffle(issue_texts)
import pandas as pd
from data.lv.bert_utils import QuestionAnsweringModel
from random import shuffle
model = QuestionAnsweringModel()
#
# for issue_text, client_name, date_received in zip(issue_texts, client_names, dates_received):
#     # issue_text_fragments = []
#     # issue_text_fragments_semicolon = issue_text.split(';')
#     # for fragment in issue_text_fragments_semicolon:
#     #     issue_text_fragments += fragment.split('\n')
#     # products = []
#     # countries = []
#     # for fragment in issue_text_fragments:
#     #     products = model.predict(
#     #         "Which product(s) are related to dumping, anti-dumping or antidumping?", fragment
#     #     )
#     #     countries = model.predict(f"Which countries are producer of the {products}?", fragment,)
#     #     for_or_against = model.predict(
#     #         f"Is it for or against antidumping duties levied for {products}", fragment
#     #     )
#     try:
#         # products = model.predict(
#         #     "Is it containing information related to dumping, antidumping or anti-dumping", issue_text
#         # )
#         #
#         products = model.predict(
#             "Which products are related to dumping, anti-dumping or antidumping?", issue_text
#         )
#         countries = model.predict(f"From which country {products} are produced?", issue_text, )
#         for_or_against = model.predict(
#             f"Is it for or against antidumping duties levied for {products}", issue_text
#         )
#         pass
#     except RuntimeError:
#         print(RuntimeError)
#         pass

if __name__ == "__main__":
    import pandas as pd
    from data.lv.bert_utils import QuestionAnsweringModel

    model = QuestionAnsweringModel()

    issue_text = "Fraudulent claims made regarding the anti-dumping order on fresh garlic from China"
    products = model.predict(
        "Which products are related?",
        issue_text,
    )
    countries = model.predict(
        f"From which country {products} are produced?", issue_text,
    )

    print(products)
    print(countries)
