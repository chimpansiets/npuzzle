import hashlib

def manhattan_distance(puzzle, solution, y, x):
	for i in range(len(solution)):
		for j in range(len(solution[i])):
			if solution[i][j] == puzzle[y][x]:
				return (abs(i - y) + abs(j - x))

puzzle1 = [[2, 8, 4],[5, 0, 6],[1, 3, 7]]
puzzle2 = [[1, 1, 1], [1, 1, 1], [1, 1, 2]]
print(manhattan_distance(puzzle1, puzzle2, 0, 0))