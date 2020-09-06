import os, sys

class Puzzle:
	def __init__(self, side_length=3):
		self.puzzle = self.gen_empty_puzzle(side_length)
		self.score = 0
		self.side_length = side_length
		self.snail_solution = self.generate_snail_solution(self.gen_empty_puzzle(side_length), 0, 0, 0, 'right')
		self.print_snail_solution()
	
	def set_side_length(self, side_length):
		self.side_length = side_length
	
	def gen_empty_puzzle(self, side_length):
		return ([[0 for x in range(side_length)] for x in range(side_length)])

	def init_puzzle(self):
		self.puzzle = self.gen_empty_puzzle(self. side_length)

	def generate_snail_solution(self, puzzle, ctr, y, x, direction):
		if ctr == (self.side_length * 2) - 1:
			return (puzzle)
		else:
			if direction == 'right':
				while x < len(puzzle) and puzzle[y][x] == 0:
					print(x, y)
					puzzle[y][x] = ctr
					ctr += 1
					x += 1
				return (self.generate_snail_solution(puzzle, ctr, y + 1, x - 1, 'down'))
			elif direction == 'down':
				while y < len(puzzle) and puzzle[y][x] == 0:
					print(x, y)
					puzzle[y][x] = ctr
					ctr += 1
					y += 1
				return (self.generate_snail_solution(puzzle, ctr, y - 1, x - 1, 'left'))
			elif direction == 'left':
				while x > 0 and puzzle[y][x] == 0:
					print(x, y)
					puzzle[y][x] = ctr
					ctr += 1
					x -= 1
				return (self.generate_snail_solution(puzzle, ctr, y - 1, x + 1, 'up'))
			elif direction == 'up':
				while y > 0 and puzzle[y][x] == 0:
					print(x, y)
					puzzle[y][x] = ctr
					ctr += 1
					y -= 1
				return (self.generate_snail_solution(puzzle, ctr, y + 1, x + 1, 'right'))

	def solvable(self):
		return (True)

	def solved(self):
		return (True)

	def get_final_state(self):
		final_state = []
		return (final_state)

	def calculate_score(self, heuristic):
		return (0)

	def print_puzzle(self):
		for row in self.puzzle:
			for digit in row:
				print(digit, end=' ')
			print()

	def print_snail_solution(self):
		for row in self.snail_solution:
			for digit in row:
				print(digit, end=' ')
			print()

class	Solver:
	def	__init__(self):
		self.puzzle = Puzzle()
		self.heuristic =  "Manhattan"

	def get_input(self, file_name):
		f = open(file_name, "r")
		side_length = 0
		y_ctr = 0
		counting = False

		for line in f.readlines():
			x_ctr = 0
			for c in [x.rstrip('\n') for x in line.split(' ')]:
				if c == '#':
					break
				if side_length == 0 and c.isdigit():
					side_length = int(c)
					self.puzzle.set_side_length(side_length)
					self.puzzle.init_puzzle()
					self.puzzle.print_puzzle()
					break
				elif c.isdigit():
					self.puzzle.puzzle[y_ctr][x_ctr] = int(c)
					x_ctr += 1
					counting = True
			if counting == True:
					y_ctr += 1
		self.puzzle.print_puzzle()

if __name__ == "__main__":
	solver = Solver()
	if len(sys.argv) >= 2:
		solver.get_input(sys.argv[1])
		# solver.print_puzzle()
	else:
		print("Incorrect amount of arguments, usage: python npuzzle_solver.py [puzzle_file] (heuristic)")
