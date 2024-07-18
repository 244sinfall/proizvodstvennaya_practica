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
        #  dict[module_id[iteration_num, correct_answer]]
        correct_answers: dict[int, dict[int, float]] = {}
        #  dict[module_id, correct_answers]
        correct_answers_amount: dict[int, int] = {}
        winners: list[VoteData] = []
        for entity in data:
            if entity.module_id not in mapped_data:
                mapped_data[entity.module_id] = {}
                correct_answers[entity.module_id] = {}
            if entity.module_iteration_num not in mapped_data[entity.module_id]:
                mapped_data[entity.module_id][entity.module_iteration_num] = []
                correct_answers[entity.module_id][entity.module_iteration_num] = entity.correct_answer
            mapped_data[entity.module_id][entity.module_iteration_num].append(entity)

        for module_id, module in mapped_data.items():
            module_correct_answers = 0
            for iteration_id, iteration in module.items():
                try:
                    winner = alg.run_vote(iteration)
                    print(f'Winner: {winner}')
                    if winner.get_value() == correct_answers[module_id][iteration_id]:
                        module_correct_answers += 1
                    winners.append(winner)
                except VoteException as e:
                    print(e)
                    continue
            correct_answers_amount[module_id] = module_correct_answers
        print("RESULTS:\n")
        for module_id, module in mapped_data.items():
            print(f"Module {module_id} | Total iterations: {len(module)} | Iterations with winner having a correct version: {correct_answers_amount[module_id]}.\n")
        return winners
