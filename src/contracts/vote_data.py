"""General interface for any vote data"""
from abc import ABC, abstractmethod

from pydantic import BaseModel


class VoteData(ABC, BaseModel):
    """General interface for any vote data"""
    @abstractmethod
    def get_identifier(self) -> str | int:
        """Must return unique entity identifier,
          as it is needed to choose winner"""
