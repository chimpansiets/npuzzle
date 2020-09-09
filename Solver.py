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
		i = 0
		start_puzzle = Puzzle(self.puzzle.puzzle)
		closed_list = [[start_puzzle, None]]
		curr_state = start_puzzle
		open_list = []
		g_score = 1
		cost_so_far = 0

		while not self.puzzle.is_solved(curr_state[0].puzzle):
			print("current state: ")
			curr_state.print_puzzle()
			up = curr_state.up()
			down = curr_state.down()
			right = curr_state.right()
			left = curr_state.left()
			if up != -1:
				print("up ", end='')
				up = Puzzle(up, self.puzzle.side_length, True)
				up.give_score(g_score)
				open_list.append(up)
			if down != -1:
				print("down ", end='')
				down = Puzzle(down, self.puzzle.side_length, True)
				down.give_score(g_score)
				open_list.append(down)
			if right != -1:
				print("right ", end='')
				right = Puzzle(right, self.puzzle.side_length, True)
				right.give_score(g_score)
				open_list.append(right)
			if left != -1:
				print("left ", end='')
				left = Puzzle(left, self.puzzle.side_length, True)
				left.give_score(g_score)
				open_list.append(left)
			g_score += 1

			score_list = [x[0].score for x in open_list]
			lowest_index = score_list.index(min(score_list))
			print("move to make: ")
			open_list[lowest_index][0].print_puzzle()
			closed_list.append(open_list[lowest_index])
			curr_state = open_list[lowest_index]
			del open_list[lowest_index]
			i += 1

		print(*(x[1] for x in closed_list))
		# print(self.puzzle.down())
		# print(self.puzzle.right())
		# print(self.puzzle.left())
