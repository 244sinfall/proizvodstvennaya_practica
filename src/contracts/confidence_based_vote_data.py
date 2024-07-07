"""Interface for VoteData objects with confidence applicable"""
from abc import abstractmethod

from contracts.vote_data import VoteData


class ConfidenceBaseVoteData(VoteData):
    """Interface for VoteData objects with confidence applicable"""
    @abstractmethod
    def get_confidence(self) -> float:
        """Return referenced / calculate confidence"""
