"""Vote algorithm that calculates weight map based on 
unique entity confidence. The entity with max weight relative to others wins"""

from contracts.confidence_based_vote_data import ConfidenceBaseVoteData
from contracts.vote_alg import VoteAlg
from exceptions.vote_exception import VoteException


class FuzzyRelativeVoteAlg(VoteAlg):
    """Vote algorithm that calculates weight map based on 
unique entity confidence. The entity with max weight relative to others wins"""
    def run_vote(self, data: list[ConfidenceBaseVoteData]) -> ConfidenceBaseVoteData:
        # Dictionary to store cumulative weights for each target identifier
        weight_map: dict[str | int, float] = {}
        options: dict[str | int, ConfidenceBaseVoteData] = {}
        # Iterate over each option
        for entity in data:
            identifier = entity.get_identifier()
            # Initialize weight to 0 if not already present
            if weight_map.get(identifier) is None:
                weight_map[identifier] = 0.0
                options[identifier] = entity
            # Add weight to a candidate
            weight_map[identifier] += entity.get_confidence()
        max_weight = 0
        winning_identifier: str | int | None = None
        for weight_identifier, weight in weight_map.items():
            if weight == max_weight and weight != 0:
                raise VoteException('Multiple winner candidates')
            if weight > max_weight:
                max_weight = weight
                winning_identifier = weight_identifier
        if winning_identifier is None:
            raise VoteException('No winner')
        return options[winning_identifier]
