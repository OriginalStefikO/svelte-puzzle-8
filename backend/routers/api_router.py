from fastapi import APIRouter
from fastapi.responses import JSONResponse

from backend.puzzle8.AStarAlgo import AStarAlgo
from backend.utils.returnTypes import ISolverPostResponse
from backend.utils.utils import convert_astar_nodes, matrix_to_string, string_to_matrix
from backend.logger.custom_logger import logger

logger = logger.getChild("api_router")


api_router = APIRouter(prefix="/v1")

@api_router.post("/solver", response_model=None)
async def solver(start_state: str, goal_state: str) -> ISolverPostResponse:
    
    start_node = string_to_matrix(start_state)
    goal_node = string_to_matrix(goal_state)
    
    logger.debug(f"Start node: {start_node}")
    logger.debug(f"Goal node: {goal_node}")
    
    solution = AStarAlgo(start_node, goal_node).solve(depth=30)
    solution["final_states"] = convert_astar_nodes(solution["final_states"])
    
    logger.debug(f"Solution: {solution}")
    
    return {
        "status_code": 200,
        "message": "Success",
        "requested_puzzle": start_state,
        "desired_output": goal_state,
        "time_taken": solution["time_taken"],
        "total_nodes_expanded": solution["total_nodes_expanded"],
        "solution": solution["final_states"]
    }

@api_router.post("/test")
async def test() -> JSONResponse:
    return JSONResponse(content={"message": "Hello, World!"})