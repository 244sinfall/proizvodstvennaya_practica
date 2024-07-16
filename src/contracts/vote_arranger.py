"""VoteArranger is an entity that describes vote arranging strategy"""
from contracts.vote_alg import VoteAlg
from contracts.vote_data import VoteData


class DefaultVoteArranger:
    """Entity to prepare and run vote for a dataset"""
    def arrange(self, alg: VoteAlg, data: list[VoteData]) -> list[VoteData]:
        """Run vote(s) for data and returns winner"""
        return [alg.run_vote(data)]
