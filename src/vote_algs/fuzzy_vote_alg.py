"""Vote algorithm that calculates weight map based on 
unique entity confidence. The entity with max total weight wins"""
from contracts.confidence_based_vote_data import ConfidenceBaseVoteData
from contracts.vote_alg import VoteAlg
from exceptions.vote_exception import VoteException

class FuzzyVoteAlg(VoteAlg):
    """Vote algorithm that calculates weight map based on 
unique entity confidence. The entity with max total weight wins"""
    def run_vote(self, data: list[ConfidenceBaseVoteData]) -> ConfidenceBaseVoteData:
        # Dictionary to store cumulative weights for each target identifier
        weight_map: dict[str | int, float] = {}
        # Dictionary to store options based on their target identifier
        options_map: dict[str | int, ConfidenceBaseVoteData] = {}
        # Iterate over each option
        for entity in data:
            identifier = entity.get_identifier()
            # Initialize weight to 0 if not already present
            if weight_map.get(identifier) is None:
                weight_map[identifier] = 0.0
            weight_map[identifier] += entity.get_confidence()
            options_map[identifier] = entity
        max_weight = -float('inf')
        winning_option: ConfidenceBaseVoteData | None = None
        for weight_identifier, weight in weight_map.items():
            if weight > max_weight:
                max_weight = weight
                winning_option = options_map[weight_identifier]
        if winning_option is None:
            raise VoteException('No winner')
        return winning_option
