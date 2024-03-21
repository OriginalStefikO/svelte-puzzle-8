import numpy as np

from backend.puzzle8.AStarNode import AStarNode

def string_to_matrix(puzzle_state: str) -> list[list[int]]:
    """
    Convert string representation of puzzle state to list format.
    Example:
    Input: "123456780"
    Output: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    """
    state = [list(map(int, puzzle_state[i:i+3])) for i in range(0, len(puzzle_state), 3)]
    return state
        
def matrix_to_string(matrix: list[list[int]]) -> str:
    return "".join([str(num) for row in matrix for num in row])


def convert_astar_nodes(nodes: list[AStarNode]) -> list[dict[str, str | float]]:
    puzzle_objects = []
    for node in nodes:
        state_str = matrix_to_string(node.state.tolist())
        puzzle_object = {
            "state": node.state.tolist(),
            "f": int(round(node.f, 1)),
            "g": int(round(node.g, 1)),
            "h": int(round(node.h, 1)),
        }
        puzzle_objects.append(puzzle_object)
    return puzzle_objects

def getInvCount(arr):
    inv_count = 0
    arr = arr.flatten()
    empty_value = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

def isSolvable(puzzle):
    inv_count = getInvCount(np.array(puzzle))
    return (inv_count % 2 == 0)

if __name__ == "__main__":    
    from backend.logger.custom_logger import logger
    
    logger.debug(isSolvable([[7, 3, 1], [4, 2, 6], [5, 0, 8]]))
    logger.debug(isSolvable([[7, 3, 1], [2, 4, 6], [5, 0, 8]]))
    logger.debug(isSolvable([[7, 3, 6], [4, 2, 1], [5, 0, 8]]))