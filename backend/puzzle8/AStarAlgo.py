import heapq
import math
import queue
import numpy as np
from backend.logger.custom_logger import logger
from backend.puzzle8.AStarNode import AStarNode

logger = logger.getChild("newaStar")

class AStarAlgo:
    def __init__(self, start: AStarNode, goal: list[list[int]]) -> None:
        self.start_state = start
        self.goal_state = np.array(goal)
        
        self.open_list = []
        self.closed_list = set()

    def solve(self, depth: int = 15):
        logger.info("Solving...")
        final_node: AStarNode = AStarNode(self.start_state.state, -1, -1, None)

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

        final_states = final_node.get_all_parents(self.start_state)
        final_states.insert(0, final_node)
        logger.info("Solved!")
        return final_states
    
if __name__ == "__main__":
    # start = [[1, 2, 3], [4, 6, 0], [7, 5, 8]]
    start = [[2, 8, 0], [5, 1, 4], [7, 6, 3]]
    # start = [[0, 4, 3], [2, 1, 6], [7, 5, 8]]
    
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    start_node = AStarNode(start, 0, 0)
    start_node.h = start_node.heuristic(np.array(goal))
    start_node.update_f()

    goal_node = goal
    a_star = AStarAlgo(start_node, goal_node)
    
    final_states = a_star.solve(30)
    final_states.reverse()

    for state in final_states:
        print(state)
        print("----")
