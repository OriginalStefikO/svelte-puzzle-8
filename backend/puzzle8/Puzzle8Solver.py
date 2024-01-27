from backend.puzzle8.PuzzleNode import PuzzleNode


class Puzzle8Solver:
  def __init__(self, initial_state: PuzzleNode, goal_state: PuzzleNode):
    self.initial_state = initial_state
    self.goal_state = goal_state
    
    self.closed_states = []
    self.open_states = []    
    
  def heuristic(self, node: PuzzleNode, goal: PuzzleNode) -> int:
    """Count of misplaced tiles or Manhatton distance

    Returns:
      Number: Heuristic value
    """
    misplaced_tiles = 0
    
    for i in range(len(node.data)):
      for j in range(len(node.data[i])):
        if (node.data[i][j] != goal.data[i][j]):
          if (node.data[i][j] == 0): continue # Empty tile does not count
          misplaced_tiles += 1
          
    return misplaced_tiles
      
if __name__ == "__main__":
  initial_state = PuzzleNode([
    [1, 2, 3],
    [4, 5, 6],
    [7, 0, 8]
  ])

  goal_state = PuzzleNode([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
  ])
  
  solver = Puzzle8Solver(initial_state, goal_state)
  
  print(solver.heuristic(initial_state, goal_state))