import os, sys
from Puzzle import Puzzle
from Solver import Solver
from tkinter import *

def insert_input(solver, gui_text, file_name):
	side_length = 0
	y_ctr = 0
	counting = False

	try:
		f = open(file_name, "r")
	except IOError:
		print("Your input file does not appear to exist")
		exit(1)
	for line in f.readlines():
		x_ctr = 0
		for c in [x.rstrip('\n') for x in line.split(' ')]:
			if c == '#':
				break
			if side_length == 0 and c.isdigit():
				side_length = int(c)
				solver.puzzle.set_side_length(side_length)
				solver.puzzle.init_puzzle()
				break
			elif c.isdigit():
				solver.puzzle.puzzle[y_ctr][x_ctr] = int(c)
				x_ctr += 1
				counting = True
		if counting == True:
			y_ctr += 1
	
	for row in solver.puzzle.puzzle:
		text = ""
		for digit in row:
			text += str(digit) + " "
		gui_text.insert(INSERT, text + "\n")


def parse_arguments(solver, argv):
	for i in range(len(argv)):
		if (argv[i].lower() == "-hamming"):
			solver.set_heuristic('hamming')
		elif (argv[i].lower() == '-manhattan'):
			solver.set_heuristic('manhattan')
		elif (argv[i].lower() == '-sietse'):
			solver.set_heuristic('sietse')

if __name__ == "__main__":
	solver = Solver()
	if len(sys.argv) >= 2 and '-i' not in sys.argv:
		solver.get_input(sys.argv[1])
		solver.puzzle.generate_snail_solution(solver.puzzle.gen_empty_puzzle(solver.puzzle.side_length), 1, 0, 0, 'right')
		print("Snail solution: ")
		solver.puzzle.print_snail_solution()
		parse_arguments(solver, sys.argv)
		path = solver.solve_puzzle()
	elif '-i' in sys.argv:
		root = Tk()
		frame=Frame(root, width=300, height=300)
		frame.pack()

		solver.get_input(sys.argv[1])
		solver.puzzle.generate_snail_solution(solver.puzzle.gen_empty_puzzle(solver.puzzle.side_length), 1, 0, 0, 'right')

		print(solver.puzzle.side_length)
		height = 50 + (40 * (solver.puzzle.side_length - 3))
		width = 50 + (40 * (solver.puzzle.side_length - 3))
		tbox1 = Text(frame)
		tbox1.place(x=(150 - (width / 2)), y=10, height=height, width=width)

		# entryFrame = Tkinter.Frame(mainFrame, width=454, height=20)
		# entryFrame.grid(row=0, column=1)


		# textbox = Text(root)
		insert_input(solver, tbox1, sys.argv[1])
		# textbox.width
		# textbox.pack()

		# textbox.tag_add("here", "1.0", "1.4")
		# textbox.tag_add("start", "1.8", "1.13")
		# textbox.tag_config("here", background="yellow", foreground="blue")
		# textbox.tag_config("start", background="black", foreground="green")
		root.mainloop()
	else:
		print("Incorrect amount of arguments, usage: python npuzzle_solver.py [puzzle_file] (heuristic)")
