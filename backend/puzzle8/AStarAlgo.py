import heapq
import time
import numpy as np
from backend.logger.custom_logger import logger
from backend.puzzle8.AStarNode import AStarNode
from backend.utils.returnTypes import IAStarAlgoSolve
from backend.utils.utils import isSolvable

logger = logger.getChild("newaStar")

class AStarAlgo:
    def __init__(self, start: list[list[int]], goal: list[list[int]]) -> None:
        self.start_state = AStarNode(start, 0, 0)
        self.goal_state = np.array(goal)
        
        self.open_list = []
        self.closed_list = set()
        
        self.start_state.h = self.start_state.heuristic(self.goal_state)
        self.start_state.update_f()

    def solve(self, depth: int = 30, max_open_nodes: int = 5000) -> IAStarAlgoSolve:
        logger.info("Solving...")
        
        start_time = time.time()
        final_node: AStarNode = self.start_state
        
        if isSolvable(self.start_state.state) != True:
            logger.error("Puzzle is not solvable")
            
            return {
                "time_taken": time.time() - start_time,
                "total_nodes_expanded": len(self.closed_list) + 1,
                "final_states": [],
                "status_code": 400,
                "message": "Puzzle is not solvable"
            }

        # Push the start node into the open list
        heapq.heappush(self.open_list, (self.start_state.f, self.start_state))

        while self.open_list and final_node != self.goal_state:
            _, q = heapq.heappop(self.open_list) # q is the best node

            for child in q.get_children_nodes(self.goal_state):
                if child == self.goal_state:
                    final_node = child
                    break

                if child.g >= depth:
                    continue

                child_state_tuple = tuple(map(tuple, child.state))
                if child_state_tuple in (state for _, state in self.open_list):
                    continue
                
                if child_state_tuple in self.closed_list:
                    continue

                child.h = child.heuristic(self.goal_state)
                child.update_f()

                heapq.heappush(self.open_list, (child.f, child))
                self.closed_list.add(child_state_tuple)
                
            if len(self.closed_list) > max_open_nodes:
                logger.error("Open list is too large")
                
                return {
                    "time_taken": time.time() - start_time,
                    "total_nodes_expanded": len(self.closed_list) + 1,
                    "final_states": [],
                    "status_code": 500,
                    "message": f"Cannot find solution even after {max_open_nodes} nodes expanded"
                }

        time_taken = time.time() - start_time
        total_nodes_expanded = len(self.closed_list) + 1
        
        logger.debug("Time taken: " + str(time_taken))
        logger.debug("Total nodes expanded: " + str(total_nodes_expanded))
        
        final_states = final_node.get_all_parents(self.start_state)
        final_states.insert(0, final_node)
        logger.info("Solved!")
        
        return {
            "time_taken": time_taken,
            "total_nodes_expanded": total_nodes_expanded,
            "final_states": final_states,
            "status_code": 200,
            "message": "Success"
        }
    
if __name__ == "__main__":
    # start = [[1, 2, 3], [4, 6, 0], [7, 5, 8]]
    # start = [[2, 8, 0], [5, 1, 4], [7, 6, 3]]
    # start = [[0, 4, 3], [2, 1, 6], [7, 5, 8]]
    # start = [[1, 2, 0], [6, 8, 7], [5, 3, 4]]
    start = [[7, 3, 1], [4, 2, 6], [5, 0, 8]]
    # start = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    # goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    a_star = AStarAlgo(start, goal)
    
    final_states = a_star.solve(30)
    final_states["final_states"].reverse()

    for state in final_states["final_states"]:
        print(state)
        print("----")
