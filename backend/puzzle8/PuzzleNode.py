from copy import copy
import numpy as np


class PuzzleNode:
  def __init__(self, data: list[list[int]], name: str = "Root node"):
    """
    
    Args:
        State (list[list[int]]): The node state of the puzzle
        Level (int): The level of the node in the tree
        Goal (list[list[int]]): The goal state of the puzzle
    """
    
    
    self.data = data
    self.name = name
    
    self.g = 0
    self.h = 0
    self.f = self.g + self.h
    
    if (not self.validate_data()):
      raise Exception("Data is not valid.")
    
  def __eq__(self, other) -> bool:
    # return self.data == other.data
    base = np.array(self.data)
    target = np.array(other.data)
    
    return np.array_equal(base, target)
  
  def __lt__(self, other) -> bool:
    return self.f < other.f
  
  def update_f(self) -> None:
    self.f = self.g + self.h
    
  def validate_data(self) -> bool:
    """Validate the data of the node
    
    Returns:
        bool: True if the data is valid, False otherwise
    """
    
    if (len(self.data) != 3): return False
    
    numbers = []
    for row in self.data:
      if len(row) != 3: 
        return False
      
      for item in row:
        if (item in numbers): 
          return False
        numbers.append(item)
    
    return True
  
  def get_tile(self, tile:int) -> tuple[int, int]:
    """Get coordinates of empty tile

    Returns:
        tuple[int, int]: (x, y)
    """
    for y, row in enumerate(self.data):
      for x, item in enumerate(row):
        if item == tile: return (x, y)
    
    return (-1, -1)
  
  def swap(self, base_position: tuple[int, int], target_position: tuple[int, int]) -> "PuzzleNode | None":
    """Swap two tiles in the puzzle

    Args:
        base_position (tuple[int, int]): (x, y)
        target_position (tuple[int, int]): (x, y)

    Returns:
        PuzzleNode: The new node with swapped tiles
    """
    
    if not all(0 <= pos <= 2 for pos in base_position + target_position):
      # raise Exception("Position cannot be negative or greater than 2.")
      return None
    
    if (base_position[0] == target_position[0] and base_position[1] == target_position[1]):
      # raise Exception("Positions cannot be the same.")
      return None
    
    if abs(base_position[0] - target_position[0]) != 1 and abs(base_position[1] - target_position[1]) != 1:
      # raise Exception("Positions must be adjacent.")
      return None
    
    new_data = [copy(row) for row in self.data]
    
    new_data[base_position[1]][base_position[0]] = self.data[target_position[1]][target_position[0]]
    new_data[target_position[1]][target_position[0]] = self.data[base_position[1]][base_position[0]]
    
    new_child = PuzzleNode(new_data)
    new_child.g = self.g + 1
    new_child.name = f"Child node"
    return new_child

  def __str__(self) -> str:
    # I was bored, no AI used, don't ask me why
    layer ="-" * (len(self.data) * 4 + 1)
    data = "| " + "\n| ".join([" | ".join([str(i) for i in row]) + " |\n" + layer for row in self.data])
    
    data_string_result = f"{layer}\n{data}"
    
    name = f"Node: {self.name}\nDepth: {self.g}"
    
    # return f"{data_string_result} --> f: {self.f} g: {self.g} h: {self.h}\n{name}"
    return f"{str(self.data)} -> g: {self.g}; h: {self.h}; f: {self.f}"