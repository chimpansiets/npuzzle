def manhattan_distance(puzzle, solution, y, x):
	for i in range(len(solution)):
		for j in range(len(solution[i])):
			if solution[i][j] == puzzle[y][x]:
				return (abs(i - y) + abs(j - x))

class Puzzle:
	def __init__(self, puzzle=None, parent=None, side_length=3, gen_solution=False, move_made=None):
		if puzzle != None:
			self.puzzle = [row.copy() for row in puzzle]
		else:
			self.puzzle = None
		self.parent = parent
		self.score = 0
		self.h_score = 0
		self.g_score = 0
		self.side_length = side_length
		self.move_made = move_made
		if (gen_solution == True):
			self.generate_snail_solution(self.gen_empty_puzzle(side_length), 1, 0, 0, 'right')
		else:
			self.snail_solution = None
	
	def is_solvable(self):
		inversions = 0
		res = []
		sol = []

		for y in range(len(self.puzzle)):
			for x in range(len(self.puzzle[y])):
				res.append(self.puzzle[y][x])

		for y in range(len(self.snail_solution)):
			for x in range(len(self.snail_solution[y])):
				sol.append(self.snail_solution[y][x])

		for i in range(len(res)):
			for j in range(i + 1, len(res)):
				if sol.index(res[i]) > sol.index(res[j]):
					inversions += 1

		if len(self.puzzle) % 2 == 0:
			if inversions % 2 != 0:
				return (False)
			else:
				return (True)
		else:
			if inversions % 2 == 0:
				return (False)
			else:
				return (True)

	def give_score(self, g_score, heur='manhattan'):
		self.g_score = g_score
		score = 0

		if (heur == 'hamming'):
			for y in range(len(self.puzzle)):
				for x in range(len(self.puzzle)):
					if self.puzzle[y][x] != self.snail_solution[y][x] and self.puzzle[y][x] != 0:
						score += 1
		elif (heur == 'manhattan') or (heur == 'sietse'):
			for y in range(len(self.puzzle)):
				for x in range(len(self.puzzle)):
					score += manhattan_distance(self.puzzle, self.snail_solution, y, x)
		if (heur == 'sietse'):
			# self.print_puzzle()
			# self.print_snail_solution()
			pairs = []
			for y in range(len(self.puzzle)):
				for x in range(len(self.puzzle)):
					if self.puzzle[y][x] != self.snail_solution[y][x] and self.puzzle[y][x] != 0 and self.snail_solution[y][x] != 0:
						pairs.append([self.puzzle[y][x], self.snail_solution[y][x]])
			for pair in pairs:
				if pair[::-1] in pairs:
					score += 1
		self.h_score = score

		self.score = self.g_score + self.h_score

	def set_side_length(self, side_length):
		self.side_length = side_length
	
	def gen_empty_puzzle(self, side_length):
		return ([[0 for x in range(side_length)] for x in range(side_length)])

	def init_puzzle(self):
		self.puzzle = self.gen_empty_puzzle(self. side_length)

	def generate_snail_solution(self, puzzle, ctr, y, x, direction):
		if ctr == (self.side_length * self.side_length):
			self.snail_solution = puzzle
		else:
			if direction == 'right':
				while x < len(puzzle) and puzzle[y][x] == 0:
					puzzle[y][x] = ctr
					ctr += 1
					x += 1
				self.generate_snail_solution(puzzle, ctr, y + 1, x - 1, 'down')
			elif direction == 'down':
				while y < len(puzzle) and puzzle[y][x] == 0:
					puzzle[y][x] = ctr
					ctr += 1
					y += 1
				self.generate_snail_solution(puzzle, ctr, y - 1, x - 1, 'left')
			elif direction == 'left':
				while x >= 0 and puzzle[y][x] == 0:
					puzzle[y][x] = ctr
					ctr += 1
					x -= 1
				self.generate_snail_solution(puzzle, ctr, y - 1, x + 1, 'up')
			elif direction == 'up':
				while y >= 0 and puzzle[y][x] == 0:
					puzzle[y][x] = ctr
					ctr += 1
					y -= 1
				self.generate_snail_solution(puzzle, ctr, y + 1, x + 1, 'right')

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

	def up(self):
		ret_puzzle = []

		for row in self.puzzle:
			ret_puzzle.append(row.copy())

		for y in range(len(self.puzzle)):
			for x in range(len(row)):
				if ret_puzzle[y][x] == 0:
					if y > 0:
						tmp = ret_puzzle[y][x]
						ret_puzzle[y][x] = ret_puzzle[y - 1][x]
						ret_puzzle[y - 1][x] = tmp
						return (ret_puzzle)
					else:
						return (-1)

	def down(self):
		ret_puzzle = []

		for row in self.puzzle:
			ret_puzzle.append(row.copy())

		for y in range(len(self.puzzle)):
			for x in range(len(row)):
				if ret_puzzle[y][x] == 0:
					if y < (len(self.puzzle) - 1):
						tmp = ret_puzzle[y][x]
						ret_puzzle[y][x] = ret_puzzle[y + 1][x]
						ret_puzzle[y + 1][x] = tmp
						return (ret_puzzle)
					else:
						return (-1)

	def right(self):
		ret_puzzle = []

		for row in self.puzzle:
			ret_puzzle.append(row.copy())

		for y in range(len(self.puzzle)):
			for x in range(len(row)):
				if ret_puzzle[y][x] == 0:
					if x < len(self.puzzle) - 1:
						tmp = ret_puzzle[y][x]
						ret_puzzle[y][x] = ret_puzzle[y][x + 1]
						ret_puzzle[y][x + 1] = tmp
						return (ret_puzzle)
					else:
						return (-1)

	def left(self):
		ret_puzzle = []

		for row in self.puzzle:
			ret_puzzle.append(row.copy())

		for y in range(len(self.puzzle)):
			for x in range(len(row)):
				if ret_puzzle[y][x] == 0:
					if x > 0:
						tmp = ret_puzzle[y][x]
						ret_puzzle[y][x] = ret_puzzle[y][x - 1]
						ret_puzzle[y][x - 1] = tmp
						return (ret_puzzle)
					else:
						return (-1)

	def is_solved(self, puzzle):
		for y in range(len(puzzle)):
			for x in range(len(puzzle)):
				if puzzle[y][x] != self.snail_solution[y][x]:
					return (False)
		return (True)
