from contracts.vote_data_classifier import VoteDataClassifier
from exceptions.classifier_exception import ClassifierException


class TensClassifier(VoteDataClassifier):
    """Classifies values by tens, so 121 is 120, 127 is 130 """
    def get_class(self, value: int | float | str) -> int | float | str:
        if isinstance(value, str):
            raise ClassifierException('TensClassifer does not support str value')
        return round(int(value)/10)*10
