from transformers import DistilBertTokenizer, DistilBertForQuestionAnswering

from transformers import BertTokenizer, BertForQuestionAnswering
import torch


class QuestionAnsweringModel:
    def __init__(self):
        # self.tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased', return_token_type_ids=True)
        # self.model = DistilBertForQuestionAnswering.from_pretrained('distilbert-base-uncased-distilled-squad')

        self.tokenizer = BertTokenizer.from_pretrained('bert-large-cased-whole-word-masking', return_token_type_ids=True)
        self.model = BertForQuestionAnswering.from_pretrained('bert-large-cased-whole-word-masking-finetuned-squad')


    def encode(self, question, context):
        encoded = self.tokenizer.encode_plus(question, context)
        return encoded["input_ids"], encoded["attention_mask"]

    def decode(self, token):
        answer_tokens = self.tokenizer.convert_ids_to_tokens(token, skip_special_tokens=True)
        return self.tokenizer.convert_tokens_to_string(answer_tokens)

    def predict(self, question, context):
        input_ids, attention_mask = self.encode(question, context)
        start_scores, end_scores = self.model(torch.tensor([input_ids]), attention_mask=torch.tensor([attention_mask]))
        ans_tokens = input_ids[torch.argmax(start_scores): torch.argmax(end_scores) + 1]
        answer = self.decode(ans_tokens)
        return answer

