"""Interface to compose objects to participate in vote"""
from abc import ABC, abstractmethod

from contracts.vote_data import VoteData


class VoteDataComposer(ABC):
    """Interface to compose objects to participate in vote"""
    @abstractmethod
    def compose(self, data: tuple) -> VoteData:
        """Should return concrete VoteData impl"""
