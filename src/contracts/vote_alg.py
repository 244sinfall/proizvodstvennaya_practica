"""Interface for vote algorithms"""
from abc import ABC, abstractmethod

from contracts.vote_data import VoteData

class VoteAlg(ABC):
    """Interface for VoteData objects with confidence applicable"""
    @abstractmethod
    def run_vote(self, data: list[VoteData]) -> VoteData:
        """Pick winner from vote data list"""
