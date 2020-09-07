import os, sys
from Puzzle import Puzzle
from Solver import Solver

if __name__ == "__main__":
	solver = Solver()
	if len(sys.argv) >= 2:
		print("Input: ")
		solver.get_input(sys.argv[1])
		solver.puzzle.generate_snail_solution(solver.puzzle.gen_empty_puzzle(solver.puzzle.side_length), 1, 0, 0, 'right')
		print("Snail solution: ")
		solver.puzzle.print_snail_solution()
		solver.solve_puzzle()
	else:
		print("Incorrect amount of arguments, usage: python npuzzle_solver.py [puzzle_file] (heuristic)")
