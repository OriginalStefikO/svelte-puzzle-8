import math
import numpy as np

class AStarNode:
    def __init__(self, state: list[list[int]] | np.ndarray, h, g, parent=None) -> None:
        self.state = np.array(state)
        self.parent = parent
        self.h: int | float = 0
        self.g = g
        self.f = h + g
        
        self.depth_weight = 1

    def update_f(self):
        self.f = self.h + self.g

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other: np.ndarray):
        return np.array_equal(self.state, other)
    
    def __str__(self) -> str:
        depth = math.ceil(round(self.g, 1) / self.depth_weight)
        return f"{str(self.state)} -> g: {depth}; h: {self.h}; f: {round(self.f, 1)}"

    def get_tile(self, tile: int) -> tuple[int, int]:
        """Get coordinates of empty tile

        Returns:
            tuple[int, int]: (x, y)
        """
        y, x = np.where(self.state == tile)
        return x[0], y[0]

    def get_children_nodes(self, goal_state) -> list["AStarNode"]:
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
                new_state.parent = self
                children_nodes.append(new_state)

        return children_nodes

    def swap(
        self, base_position: tuple[int, int], target_position: tuple[int, int]
    ) -> "AStarNode | None":
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
        # Set state in target position as base position of the current state
        new_state[base_y, base_x] = self.state[target_y, target_x]
        new_state[target_y, target_x] = self.state[base_y, base_x]

        new_child = AStarNode(new_state, 0, self.g + self.depth_weight)

        return new_child
   
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

                goal_tile_position = np.argwhere(self.state == goal[y][x])[0]

                distance += np.abs(goal_tile_position[1] - x) + np.abs(goal_tile_position[0] - y)

        return distance

    def get_all_parents(self, start_node: "AStarNode") -> list["AStarNode"]:
        parents = []
        if (
            self.parent is not None
            and self.parent not in parents
            and self.parent != start_node
        ):
            parents.append(self.parent)
            parents += self.parent.get_all_parents(start_node)

        return parents
