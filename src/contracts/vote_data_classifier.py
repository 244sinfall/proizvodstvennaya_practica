"""Interface for vote data classifiers"""
from abc import ABC, abstractmethod

class VoteDataClassifier(ABC):
    """Interface for VoteData classifiers. Return class value"""
    @abstractmethod
    def get_class(self, value: int | float | str) -> int | float | str:
        """Pick winner from vote data list"""
