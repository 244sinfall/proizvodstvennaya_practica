"""Vote algorithm that calculates weight map based on 
unique entity confidence. The entity with max weight relative to others wins"""

from contracts.confidence_based_vote_data import ConfidenceBaseVoteData
from contracts.vote_alg import VoteAlg
from exceptions.vote_exception import VoteException


class FuzzyRelativeWeightVoteAlg(VoteAlg):
    """Vote algorithm that calculates weight map based on 
unique entity confidence. The entity with max weight relative to others wins"""
    def run_vote(self, data: list[ConfidenceBaseVoteData]) -> ConfidenceBaseVoteData:
        """Vote algorithm that calculates selects a winner relatively keeping in mind confidence
        Example Data: [1, 1, 2, 2, 2, 3, 3, 4, 4]
        Example Confidence: [0.95, 0.95, 0.2, 0.2, 0.2, 0.35, 0.35, 0.4, 0.4]
        Winner: 1, as it meets most relative to others.
        """
        confidence_map: dict[str | int | float, float] = {}
        # Iterate over each option
        max_confidence: float = -1
        winner: ConfidenceBaseVoteData | None = None
        for entity in data:
            confidence = entity.get_confidence()
            val = entity.get_value()
            if val not in confidence_map:
                confidence_map[val] = confidence
            else:
                confidence_map[val] += confidence
            if confidence_map[val] > max_confidence:
                max_confidence = confidence_map[val]
                winner = entity
        if not winner:
            raise VoteException(f"No winner for {data}")
        return winner
