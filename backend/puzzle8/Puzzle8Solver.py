from backend.puzzle8.PuzzleNode import PuzzleNode


class Puzzle8Solver:
  def __init__(self, initial_state: PuzzleNode, goal_state: PuzzleNode):
    self.initial_state = initial_state
    self.goal_state = goal_state
    
    self.closed_states:list[PuzzleNode] = [self.initial_state]
    self.open_states:list[PuzzleNode] = []
    
  def heuristic(self, state: PuzzleNode, goal: PuzzleNode) -> PuzzleNode:
    """Count of misplaced tiles or Manhatton distance

    Returns:
      Number: Heuristic value
    """
    
    for i in range(len(state.data)):
      for j in range(len(state.data[i])):
        if (state.data[i][j] != goal.data[i][j]):
          if (state.data[i][j] == 0): continue # Empty tile does not count
          state.h += 1
    state.update_f()
    return state
      
  def get_open_states(self, state: PuzzleNode) -> list[PuzzleNode]:
    empty_tile_position = state.get_empty_tile()
    
    possible_transformations = [
      (empty_tile_position[0] + 1, empty_tile_position[1]), # Right
      (empty_tile_position[0] - 1, empty_tile_position[1]), # Left
      (empty_tile_position[0], empty_tile_position[1] + 1), # Down
      (empty_tile_position[0], empty_tile_position[1] - 1), # Up
    ]
    
    for transformation in possible_transformations:
      new_state = state.swap(empty_tile_position, transformation)
      
      if (new_state is not None):
        self.open_states.append(self.heuristic(new_state, self.goal_state))
    
    return self.open_states
  
  def get_best_state(self):
    best_state = self.open_states[0]
    for state in self.open_states:
      if state < best_state:
        best_state = state
    return best_state
      
  
  def solve(self) -> list[PuzzleNode]:
    current_state = self.initial_state
    
    while current_state != self.goal_state:
      self.get_open_states(current_state)
      current_state = self.get_best_state()
      self.closed_states.append(current_state)
      self.open_states = []
    
    print("Success!")
    print(current_state)
    return self.closed_states  
              
      
if __name__ == "__main__":
  initial_state = PuzzleNode([
    [1, 2, 3],
    [4, 5, 6],
    [0, 7, 8]
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