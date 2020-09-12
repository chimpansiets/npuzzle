from Puzzle import Puzzle
import hashlib

def puzzle_in_list(oc_list, puzzle):
	for curr_puzzle in oc_list:
		if str(curr_puzzle) == str(puzzle):
			return (True)
	return (False)

class	Solver:
	def	__init__(self):
		self.puzzle = Puzzle()
		self.heuristic =  "manhattan"

	def set_heuristic(self, heuristic):
		self.heuristic = heuristic

	def get_input(self, file_name):
		try:
			f = open(file_name, "r")
		except IOError:
			print("Your input file does not appear to exist")
			exit(1)
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
		print("Input: ")
		self.puzzle.print_puzzle()

	def	solve_puzzle(self):
		i = 0
		start_puzzle = Puzzle(self.puzzle.puzzle, None, self.puzzle.side_length)
		start_puzzle.generate_snail_solution(start_puzzle.gen_empty_puzzle(start_puzzle.side_length), 1, 0, 0, 'right')
		start_puzzle.give_score(0)
		all_puzzles = []
		open_list = []
		current = start_puzzle
		g_score = 1
		cost_so_far = 0
		maxStates = 0

		open_list.append(current)
		while len(open_list) > 0:
			# Find the item in the open set with the lowest f score
			score_list = [x.h_score for x in open_list]
			lowest_index = score_list.index(min(score_list))
			# print("move to make: ")
			# open_list[lowest_index].print_puzzle()
			current = open_list[lowest_index]
			# print("current: " + str(current.score))
			# current.print_puzzle()

			if self.puzzle.is_solved(current.puzzle):
				path = []
				while current.parent:
					path.append(current)
					current = current.parent
				path.append(current)
				# print(len(path))
				print("Total states: %i" % i)
				print("Max number of states in memory: %i" % maxStates)
				print("Moves required: %i" % (len(path) - 1))
				# list(map(lambda x: print(x.move_made), path[::-1]))
				return path[::-1]

			up = current.up()
			down = current.down()
			right = current.right()
			left = current.left()
			if up != -1:
				up = Puzzle(up, current, self.puzzle.side_length, True, 'up')
				up.give_score(g_score, self.heuristic)
				if not (str(up.puzzle) in all_puzzles):
					open_list.append(up)
					all_puzzles.append(str(up.puzzle))
			if down != -1:
				down = Puzzle(down, current, self.puzzle.side_length, True, 'down')
				down.give_score(g_score, self.heuristic)
				if not (str(down.puzzle) in all_puzzles):
					open_list.append(down)
					all_puzzles.append(str(down.puzzle))
			if right != -1:
				right = Puzzle(right, current, self.puzzle.side_length, True, 'right')
				right.give_score(g_score, self.heuristic)
				if not (str(right.puzzle) in all_puzzles):
					open_list.append(right)
					all_puzzles.append(str(right.puzzle))
			if left != -1:
				left = Puzzle(left, current, self.puzzle.side_length, True, 'left')
				left.give_score(g_score, self.heuristic)
				if not (str(left.puzzle) in all_puzzles):
					open_list.append(left)
					all_puzzles.append(str(left.puzzle))

			# Maximum number of states ever represented in memory
			if len(open_list) > maxStates:
				maxStates = len(open_list)

			open_list.remove(current)
			g_score += 1
			i += 1

		# print(self.puzzle.down())
		# print(self.puzzle.right())
		# print(self.puzzle.left())
