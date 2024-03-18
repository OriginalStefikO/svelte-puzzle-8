export type PuzzleSolution = {
  state: number[][];
  f: number;
  g: number;
  h: number;
};

export type PuzzleResponse = {
  status_code: number;
  message: string;
  requested_puzzle: string;
  desired_output: string;
  time_taken: number;
  total_nodes_expanded: number;
  solution: PuzzleSolution[];
};