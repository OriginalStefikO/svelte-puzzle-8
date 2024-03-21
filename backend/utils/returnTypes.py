from typing_extensions import TypedDict

from backend.puzzle8.AStarNode import AStarNode


class ISolverPostResponse(TypedDict):
    status_code: int
    message: str
    time_taken: float
    requested_puzzle: str
    desired_output: str
    total_nodes_expanded: int
    solution: list[dict[str, str | float]]
    

class IAStarAlgoSolve(TypedDict):
    time_taken: float
    total_nodes_expanded: int
    final_states: list[AStarNode]
    status_code: int
    message: str