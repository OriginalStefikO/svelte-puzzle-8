class PuzzleNode:
  def __init__(self, data: list[list[int]]):
    """
    
    Args:
        State (list[list[int]]): The node state of the puzzle
        Level (int): The level of the node in the tree
        Goal (list[list[int]]): The goal state of the puzzle
    """
    self.data = data
    
    self.f = 0
    self.g = 0
    self.h = 0
    
  def set_f(self, f):
    self.f = f
    
  def set_g(self, g):
    self.g = g
    
  def set_h(self, h):
    self.h = h   