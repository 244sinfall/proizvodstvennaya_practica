"""General interface for any vote data"""
from abc import ABC, abstractmethod

from pydantic import BaseModel


class VoteData(ABC, BaseModel):
    """General interface for any vote data"""
    @abstractmethod
    def get_value(self) -> str | int | float:
        """Value to vote on"""
