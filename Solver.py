from Puzzle import Puzzle

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
					break
				elif c.isdigit():
					self.puzzle.puzzle[y_ctr][x_ctr] = int(c)
					x_ctr += 1
					counting = True
			if counting == True:
					y_ctr += 1
		self.puzzle.print_puzzle()

	def	solve_puzzle(self):
		# while not self.puzzle.is_solved(self.puzzle):
		x = self.puzzle.up()
		if x != -1:
			x = Puzzle(x)
			x.print_puzzle()
		# print(self.puzzle.down())
		# print(self.puzzle.right())
		# print(self.puzzle.left())
