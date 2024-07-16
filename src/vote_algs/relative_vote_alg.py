"""Vote algorithm that calculates weight map based on 
unique entity confidence. The entity with max weight relative to others wins"""

from contracts.vote_alg import VoteAlg
from contracts.vote_data import VoteData
from exceptions.vote_exception import VoteException


class RelativeVoteAlg(VoteAlg):
    """Vote algorithm that calculates selects a winner relatively
    Example: [1, 1, 2, 3, 4, 5, 6, 7]
    Winner: 1, as it meets most relative to others.
    """
    def run_vote(self, data: list[VoteData]) -> VoteData:
        count_map: dict[str | int | float, int] = {}
        # Iterate over each option
        max_count = 0
        winner: VoteData | None
        for entity in data:
            val = entity.get_value()
            if val not in count_map:
                count_map[val] = 1
            else:
                count_map[val] += 1
                if count_map[val] > max_count:
                    max_count = count_map[val]
                    winner = entity
        if not winner:
            raise VoteException("No winner")
        return winner
