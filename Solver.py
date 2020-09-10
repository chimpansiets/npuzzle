from Puzzle import Puzzle

def puzzle_equ(puzzle1, puzzle2):
	for y in range(len(puzzle1)):
		for x in range(len(puzzle1[y])):
			if puzzle1[y][x] != puzzle2[y][x]:
				return (0)
	return (1)

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
		i = 0
		start_puzzle = Puzzle(self.puzzle.puzzle)
		closed_list = []
		open_list = []
		current = start_puzzle
		g_score = 1
		cost_so_far = 0

		open_list.append(current)
		while len(open_list) > 0:
			# Find the item in the open set with the lowest f score
			score_list = [x.score for x in open_list]
			lowest_index = score_list.index(min(score_list))
			# print("move to make: ")
			# open_list[lowest_index].print_puzzle()
			current = open_list[lowest_index]

			if self.puzzle.is_solved(current.puzzle):
				path = []
				while current.parent:
					path.append(current)
					current = current.parent
				path.append(current)
				list(map(lambda x: x.print_puzzle(), path[::-1]))
				return path[::-1]
			
			open_list.remove(current)
			closed_list.append(current)
			print("current state: ")
			current.print_puzzle()
			up = current.up()
			down = current.down()
			right = current.right()
			left = current.left()
			if up != -1:
				print("up ", end='')
				up = Puzzle(up, current, self.puzzle.side_length, True)
				up.give_score(g_score)
				open_list.append(up)
			if down != -1:
				print("down ", end='')
				down = Puzzle(down, current, self.puzzle.side_length, True)
				down.give_score(g_score)
				open_list.append(down)
			if right != -1:
				print("right ", end='')
				right = Puzzle(right, current, self.puzzle.side_length, True)
				right.give_score(g_score)
				open_list.append(right)
			if left != -1:
				print("left ", end='')
				left = Puzzle(left, current, self.puzzle.side_length, True)
				left.give_score(g_score)
				open_list.append(left)
			g_score += 1

			i += 1

		# print(self.puzzle.down())
		# print(self.puzzle.right())
		# print(self.puzzle.left())
