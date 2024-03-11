import numpy as np
from copy import deepcopy
import logging

logger = logging.basicConfig(level=logging.DEBUG)


class aStarNode:
    def __init__(self, state: list[list[int]] | np.ndarray, h, g, parent=None) -> None:
        self.state = np.array(state)
        self.parent = parent
        self.h = 0
        self.g = g
        self.f = h + g

    def update_f(self):
        # self.f = self.h + self.g
        self.f = self.h

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other: np.ndarray):
        return np.array_equal(self.state, other)

    def __hash__(self):
        return hash(self.state.tobytes())

    def __str__(self) -> str:
        return f"{str(self.state)} -> g: {self.g}; h: {self.h}; f: {self.f}"

    def get_tile(self, tile: int) -> tuple[int, int]:
        """Get coordinates of empty tile

        Returns:
            tuple[int, int]: (x, y)
        """
        coordinates = np.where(self.state == tile)
        return coordinates[1][0], coordinates[0][0]

    def get_children_nodes(self, goal_state) -> list["aStarNode"]:
        x, y = self.get_tile(0)

        possible_transformations = [
            (x + 1, y),  # Right
            (x - 1, y),  # Left
            (x, y + 1),  # Down
            (x, y - 1),  # Up
        ]

        children_nodes = []
        for transformation in possible_transformations:
            new_state = self.swap((x, y), transformation)

            if new_state is not None:
                new_state.h = new_state.heuristic(goal_state)
                new_state.update_f()

                new_state.parent = self
                children_nodes.append(new_state)

        return children_nodes

    def swap(
        self, base_position: tuple[int, int], target_position: tuple[int, int]
    ) -> "aStarNode | None":
        """Swap two tiles in the puzzle

        Args:
            base_position (tuple[int, int]): (x, y)
            target_position (tuple[int, int]): (x, y)

        Returns:
            PuzzleNode: The new node with swapped tiles
        """

        base_x, base_y = base_position
        target_x, target_y = target_position

        # raise Exception("Position cannot be negative or greater than 2.")
        if not all(0 <= pos <= 2 for pos in base_position + target_position):
            return None

        # raise Exception("Positions cannot be the same.")
        if base_x == target_x and base_y == target_y:
            return None

        # raise Exception("Positions must be adjacent.")
        if abs(base_x - target_x) != 1 and abs(base_y - target_y) != 1:
            return None

        new_state = np.copy(self.state)

        # Set tile in base position as target position of the current state
        new_state[base_y, base_x] = self.state[target_y, target_x]
        # Set state in target position as base position of the current state
        new_state[target_y, target_x] = self.state[base_y, base_x]

        new_child = aStarNode(new_state, self.h, self.g + 1)

        return new_child

    # def heuristic(self, goal:np.ndarray) -> int:
    #   distance = 0
    #   for i in range(3):
    #     for j in range(3):
    #       if self.state[i][j] != goal[i][j]:
    #         distance += 1

    #   return distance

    def heuristic(self, goal: np.ndarray):
        """Manhattan distance

        Returns:
          Number: Heuristic value
        """
        distance = 0
        for y in range(len(self.state)):
            for x in range(len(self.state[y])):
                if self.state[y][x] == goal[y][x]:
                    continue  

                coordinates = np.where(self.state == goal[y][x])
                goal_coordinates = coordinates[1][0], coordinates[0][0]

                goal_tile_position = goal_coordinates

                distance += abs(goal_tile_position[1] - x) + abs(
                    goal_tile_position[0] - y
                )
        return distance

    def get_all_parents(self, start_node: "aStarNode") -> list["aStarNode"]:
        parents = []
        if (
            self.parent is not None
            and self.parent not in parents
            and self.parent != start_node
        ):
            parents.append(self.parent)
            parents += self.parent.get_all_parents(start_node)

        return parents
    
    def deepcopy(self):
        copy = aStarNode(self.state, -1, -1, None)
        copy.f = -1
        return copy


class aStar:
    def __init__(self, start: aStarNode, goal: list[list[int]]) -> None:
        self.start_state = start
        self.goal_state = np.array(goal)
        self.open_states = [self.start_state]
        self.closed_states = set()

    def solve(self, max_iterations: int = 1000):
        open_state = self.open_states[0]
        iteration = 0
        while open_state != self.goal_state and iteration < max_iterations:
            iteration += 1

            self.open_states.remove(open_state)
            self.closed_states.add(open_state.deepcopy())

            children = open_state.get_children_nodes(self.goal_state)
            for child in children:
                child_copy = child.deepcopy()

                if child_copy in self.closed_states:
                    continue
                if child in self.open_states:
                    continue
                
                if (child_copy not in self.closed_states and child.g < 25):
                    self.open_states.append(child)
                self.closed_states.add(child_copy)

            # self.get_best_nodes()
            
            self.open_states = sorted(self.open_states, key=lambda x: x.f)
            # print(len(self.open_states))
            open_state = self.open_states[0]

        print(len(self.open_states))
        self.open_states = sorted(self.open_states, key=lambda x: x.f)
        final_states = open_state.get_all_parents(self.start_state)
        final_states.insert(0, open_state)
        return final_states

    def test(self):
        print(self.open_states[0])
        print(self.open_states[0].get_children_nodes(self.goal_state))
        
        self.open_states.extend(self.open_states[0].get_children_nodes(self.goal_state))
        self.open_states.sort()
        
        for child in self.open_states:
            print(child)
            print("----")
            
        self.open_states = sorted(self.open_states, key=lambda x: x.f)
        
        print("----------------")
        
        for child in self.open_states:
            print(child)
            print("----")

    def get_best_nodes(self):
        highest_value = min(self.open_states)
        best_nodes = [item for item in self.open_states if item.f == highest_value.f]

        for item in self.open_states:
            if item.f != highest_value.f:
                self.closed_states.add(item.deepcopy().__hash__)
            
        self.open_states = best_nodes


if __name__ == "__main__":
    # start = [[1, 2, 3], [4, 6, 0], [7, 5, 8]]
    start = [[3, 7, 8], [1, 0, 4], [6, 5, 2]]
    # start = [[1, 2, 3], [4, 8, 5], [7, 6, 0]]
    # start = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]

    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    start_node = aStarNode(start, 0, 0)
    start_node.h = start_node.heuristic(np.array(goal))
    start_node.update_f()

    goal_node = goal
    a_star = aStar(start_node, goal_node)
    # final_states = a_star.test()
    final_states = a_star.solve(1200)
    final_states.reverse()

    for state in final_states:
        print(state)
        print("----")
