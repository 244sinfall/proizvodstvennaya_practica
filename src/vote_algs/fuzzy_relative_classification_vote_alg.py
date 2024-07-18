"""Vote algorithm that classifies data and selects winner 
based on relative class members amount"""

from contracts.vote_alg import VoteAlg
from contracts.vote_data import VoteData
from contracts.vote_data_classifier import VoteDataClassifier
from exceptions.vote_exception import VoteException


class FuzzyRelativeClassificationVoteAlg(VoteAlg):
    """Vote algorithm that classifies data and selects winner 
    based on relative class members amount"""
    def __init__(self, classifier: VoteDataClassifier) -> None:
        self.classifier = classifier

    def run_vote(self, data: list[VoteData]) -> VoteData:
        """Vote algorithm that calculates selects a winner relatively using classification
        Example Data: [0.12, 0.11, 0.50, 0.38, 0.76]
        Winner: 1 or 2, as it is in most popular class.
        """
        class_map: dict[str | int | float, list[VoteData]] = {}
        class_members: dict[str | int | float, int] = {}

        for entity in data:
            # Create a class map
            class_value = self.classifier.get_class(entity.get_value())
            if class_value not in class_map:
                class_map[class_value] = []
            class_map[class_value].append(entity)
            # Calculate each class members
            class_members[class_value] = len(class_map[class_value])
        # Exclude no winner situation
        sorted_class_members_count = sorted(class_members.values(), reverse=True)
        # in case of len(sorted_class_members_count) != 1 
        # we have only one class and winner somewhere in it.
        if len(sorted_class_members_count) != 1 \
            and sorted_class_members_count[0] == sorted_class_members_count[1]:
            raise VoteException('No winner')
        # find winner
        winner_list: list[VoteData] | None = None
        max_length = 0
        for candidate_list in class_map.values():
            if len(candidate_list) > max_length:
                winner_list = candidate_list
        if winner_list is None or len(winner_list) == 0:
            raise VoteException('No winner')
        return winner_list[0]
