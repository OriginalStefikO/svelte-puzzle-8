import math
import numpy as np
from backend.logger.custom_logger import logger
from backend.puzzle8.AStarNode import AStarNode

logger = logger.getChild("newaStar")

class AStarAlgo:
    def __init__(self, start: AStarNode, goal: list[list[int]]) -> None:
        self.start_state = start
        self.goal_state = np.array(goal)
        self.open_list = [self.start_state]
        self.closed_list = []

    def solve(self, depth: int = 15):
        logger.debug("Solving...")
        final_node:AStarNode = AStarNode(self.start_state.state, -1, -1, None)
        while self.open_list and final_node != self.goal_state:            
            self.open_list = sorted(self.open_list, key=lambda x: x.f)
            q = self.open_list.pop(0)
            
            for child in q.get_children_nodes(self.goal_state):
                if child == self.goal_state:
                    final_node = child
                    break
                
                if child.g >= depth:
                    continue
                
                is_in_open_list = False
                for node in self.open_list:
                    if child == node.state and child.f >= node.f:
                        is_in_open_list = True
                        break
                
                if is_in_open_list:
                    continue
                
                is_in_closed_list = False
                for node in self.closed_list:
                    if child == node.state and child.f >= node.f:
                        is_in_closed_list = True
                        break
                
                if is_in_closed_list:
                    continue
                
                self.open_list.append(child)
                self.closed_list.append(q)
                    

        print(len(self.open_list))
        self.open_list = sorted(self.open_list, key=lambda x: x.f)
        
        final_states = final_node.get_all_parents(self.start_state)
        final_states.insert(0, final_node)
        logger.debug("Solved")
        return final_states

if __name__ == "__main__":
    # start = [[1, 2, 3], [4, 6, 0], [7, 5, 8]]
    start = [[2, 8, 0], [5, 1, 4], [7, 6, 3]]
    
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    start_node = AStarNode(start, 0, 0)
    start_node.h = start_node.heuristic(np.array(goal))
    start_node.update_f()

    goal_node = goal
    a_star = AStarAlgo(start_node, goal_node)
    
    final_states = a_star.solve(18)
    final_states.reverse()

    for state in final_states:
        print(state)
        print("----")
