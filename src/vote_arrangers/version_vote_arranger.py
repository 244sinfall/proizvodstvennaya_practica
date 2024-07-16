"""VersionVoteArranger is splits data by module and iteration and runs a bunch of votes"""
from contracts.vote_alg import VoteAlg
from contracts.vote_arranger import DefaultVoteArranger
from contracts.vote_data import VoteData
from exceptions.vote_exception import VoteException
from vote_data.version import Version


class VersionVoteArranger(DefaultVoteArranger):
    """Runs vote on Version data by iteration / module"""
    def arrange(self, alg: VoteAlg, data: list[Version]) -> list[VoteData]:
        """Prints every iteration per module winner and returns list of all winners"""
        #  dict[module_id[iteration_num, VoteData]]
        mapped_data: dict[int, dict[int, list[VoteData]]] = {}
        winners: list[VoteData] = []
        for entity in data:
            if entity.module_id not in mapped_data:
                mapped_data[entity.module_id] = {}
            if entity.module_iteration_num not in mapped_data[entity.module_id]:
                mapped_data[entity.module_id][entity.module_iteration_num] = []
            mapped_data[entity.module_id][entity.module_iteration_num].append(entity)
        for module in mapped_data.values():
            for iteration in module.values():
                try:
                    winner = alg.run_vote(iteration)
                    print(f'Winner: {winner}')
                    winners.append(winner)
                except VoteException as e:
                    print(e)
                    continue
        return winners
