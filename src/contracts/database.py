"""Interface for database to export vote data"""
from abc import ABC, abstractmethod


class VoteDatabase(ABC):
    """Interface for database to export vote data"""
    @abstractmethod
    def get_data(self) -> list[tuple]:
        """Should return raw tuple with table values, 
        so VoteDataComposer will be able to work with them"""
