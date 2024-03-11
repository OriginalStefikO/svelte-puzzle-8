import random

from backend.puzzle8.PuzzleNode import PuzzleNode


class Puzzle8Solver:
  def __init__(self, initial_state: PuzzleNode, goal_state: PuzzleNode):
    self.initial_state = initial_state
    self.goal_state = goal_state
    
    self.closed_states:list[PuzzleNode] = [self.initial_state]
    self.open_states:list[PuzzleNode] = []
    
  def heuristic_misplacedTiles(self, state: PuzzleNode, goal: PuzzleNode) -> PuzzleNode:
    """Count of misplaced tiles

    Returns:
      Number: Heuristic value
    """
    
    for y in range(len(state.data)):
      for x in range(len(state.data[y])):
        if (state.data[y][x] != goal.data[y][x]):
          if (state.data[y][x] == 0): continue # Empty tile does not count
          state.h += 1
    state.update_f()
    return state
    
  def heuristic_manhattanDistance(self, state: PuzzleNode, goal: PuzzleNode) -> PuzzleNode:
    """ Manhattan distance

    Returns:
      Number: Heuristic value
    """
    
    for y in range(len(state.data)):
      for x in range(len(state.data[y])):
        if (state.data[y][x] == goal.data[y][x]): continue # Tile is in the right place
        if (state.data[y][x] == 0): continue # Empty tile does not count
          
        goal_tile_position = goal.get_tile(state.data[y][x])
        
        distance = abs(goal_tile_position[1] - x) + abs(goal_tile_position[0] - y)
        state.h += distance
          
    state.update_f()
    return state    
      
  def get_open_states(self, state: PuzzleNode) -> list[PuzzleNode]:
    empty_tile_position = state.get_tile(0)
    
    possible_transformations = [
      (empty_tile_position[0] + 1, empty_tile_position[1]), # Right
      (empty_tile_position[0] - 1, empty_tile_position[1]), # Left
      (empty_tile_position[0], empty_tile_position[1] + 1), # Down
      (empty_tile_position[0], empty_tile_position[1] - 1), # Up
    ]
    
    # random.shuffle(possible_transformations)
    
    for transformation in possible_transformations:
      new_state = state.swap(empty_tile_position, transformation)
      
      if (new_state is not None):
        self.open_states.append(self.heuristic_misplacedTiles(new_state, self.goal_state))
        # self.open_states.append(self.heuristic_manhattanDistance(new_state, self.goal_state))
    return self.open_states
  
  def sort_open_states(self):
    self.open_states = sorted(self.open_states, key=lambda state: (state.f, state.h))
  
  def solve(self) -> list[PuzzleNode]:
    current_state = self.initial_state
    
    while current_state != self.goal_state:
      self.get_open_states(current_state)

      self.sort_open_states()
      
      current_state = self.open_states[0]
      while current_state in self.closed_states:
        self.open_states.pop(0)
        current_state = self.open_states[0]
        if (len(self.open_states) == 1):
          break
      
      self.closed_states.append(current_state)
      self.open_states = []
      
      if (len(self.closed_states) > 69):
        # raise Exception("Too many iterations")
        break
    
    if (current_state != self.goal_state):
      print("Failed!")
      return []
    print("Success!")
    print(current_state)
    return self.closed_states  
              
      
if __name__ == "__main__":
  initial_state = PuzzleNode([
    [6, 3, 4],
    [2, 0, 1],
    [7, 8, 5]
  ])

  goal_state = PuzzleNode([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
  ])
  
  solver = Puzzle8Solver(initial_state, goal_state)  
  print(solver.solve())
  
  for state in solver.closed_states:
    print(state)
    print("-----")