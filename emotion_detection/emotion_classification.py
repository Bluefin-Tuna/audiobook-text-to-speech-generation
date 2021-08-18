from transformers import BertTokenizer
from model import BertForMultiLabelClassification
from multilabel_pipeline import MultiLabelPipeline
from pprint import pprint
from sentence_splitter import SentenceSplitter

class EmotionInformation():

    def __init__(self):

        tokenizer = BertTokenizer.from_pretrained("monologg/bert-base-cased-goemotions-ekman")
        model = BertForMultiLabelClassification.from_pretrained("monologg/bert-base-cased-goemotions-ekman")
        self.goemotions = MultiLabelPipeline(
            model=model,
            tokenizer=tokenizer,
            threshold=0.3
        )

    @classmethod
    def preprocess(cls, text) -> list(str):

        splitter = SentenceSplitter(language = 'en')
        text = splitter.split(text)

    def retrieve_emotions(self, text, only_quotations):

        emotions = []
        sentences = preprocess(text = text, only_quotations = only_quotations)
        raw_emotions = self.goemotions(sentences)
        for sentence_index in range(len(raw_emotions)):
            index = raw_emotions[sentence_index].index(max(raw_emotions[sentence_index]['scores']))
            emotions.append(raw_emotions[sentence_index]['labels'][index])

        return emotions