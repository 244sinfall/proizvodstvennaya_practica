"""Composes Version object"""
from contracts.composer import VoteDataComposer
from vote_data.version import Version


class VersionComposer(VoteDataComposer):
    """Composes Version object"""
    def compose(self, data: tuple) -> Version:
        return Version(
            id=data[0],
            version_id=data[1],
            version_name=data[2],
            version_reliability=data[3],
            version_common_coordinates=data[4],
            version_answer=data[5],
            correct_answer=data[6],
            module_id=data[7],
            module_name=data[8],
            module_connectivity_matrix=data[9],
            module_iteration_num=data[10],
            experiment_name=data[11]
        )
