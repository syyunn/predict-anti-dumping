import pandas as pd
from tqdm import tqdm

path = "./data/dumping_issue_text.csv"
df = pd.read_csv(path)

import spacy

nlp = spacy.load("en_core_web_sm")
#  "Fraudulent claims made regarding the anti-dumping order on fresh garlic from China"


def collect_country_product(issue_text):
    nnps = []
    nns = []
    doc = nlp(
        issue_text
    )
    for token in doc:
        # print(
        #     token.text,
        #     token.lemma_,
        #     token.pos_,
        #     token.tag_,
        #     token.dep_,
        #     token.shape_,
        #     token.is_alpha,
        #     token.is_stop,
        # )

        if token.tag_ == 'NNP':
            nnps.append(token.text)
        if token.tag_ == 'NN':
            nns.append(token.text)
    if len(nns) == 1 and len(nnps) == 1:
        print(issue_text)
        print(nns[0], nnps[0])

df['issue_text'].apply(lambda x: collect_country_product(x))


if __name__ == "__main__":
    pass
