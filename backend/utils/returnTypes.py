from typing_extensions import TypedDict


class ISolverPostResponse(TypedDict):
    status_code: int
    message: str
    time_taken: float
    requested_puzzle: str
    desired_output: str
    total_nodes_expanded: int
    time_taken: float
    solution: list[dict[str, str | float]]