"""Version object form experiment data"""
from pydantic import BaseModel
from contracts.confidence_based_vote_data import ConfidenceBaseVoteData


class Version(ConfidenceBaseVoteData, BaseModel):
    """Version object form experiment data"""
    id: int
    version_id: int
    version_name: str
    version_reliability: float
    version_common_coordinates: str
    version_answer: float
    correct_answer: float
    module_id: int
    module_name: str
    module_connectivity_matrix: str
    module_iteration_num: int
    experiment_name: str

    def get_identifier(self) -> str:
        return self.version_name

    def get_confidence(self) -> float:
        return self.version_reliability

    def __str__(self) -> str:
        return f"Version ID: {self.version_id}, Version Name: {self.version_name}"