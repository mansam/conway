import copy
def next_state(board):
	new = copy.deepcopy(board)
	for r in range(0, len(board)):
		for c in range(0, len(board)):
			neighbors = 0

			# right angles
			if r - 1 >= 0:
				if board[r - 1][c]:
					neighbors += 1
			if r + 1 < len(board):
				if board[r + 1][c]:
					neighbors += 1
			if c - 1 >= 0:
				if board[r][c - 1]:
					neighbors += 1
			if c + 1 < len(board):
				if board[r][c + 1]:
					neighbors += 1 

			# diagonals
			if r - 1 >= 0 and c - 1 >= 0:
				if board[r - 1][c - 1]:
					neighbors += 1
			if r - 1 >= 0 and c + 1 < len(board):
				if board[r - 1][c + 1]:
					neighbors += 1
			if r + 1 < len(board) and c - 1 >= 0:
				if board[r + 1][c - 1]:
					neighbors += 1
			if r + 1 < len(board) and c + 1 < len(board):
				if board[r + 1][c + 1]:
					neighbors += 1

			if board[r][c]:
				if neighbors < 2 or neighbors > 3:
					new[r][c] = False
			if not board[r][c]:
				if neighbors == 3:
					new[r][c] = True
	return new

def print_board(board):
	import os
	from colorama import Fore
	os.system('clear')
	for row in board:
		for element in row:
			if element:
				print Fore.BLUE + "O",
			else:
				print " ",
		print

if __name__ == '__main__':
	from colorama import init
	init(autoreset=True)

	board = []
	rows = input()
	for i in range(0, rows):
		row = []
		line = raw_input()
		for each in line:
			if each == "X":
				row.append(True)
			elif each == "_":
				row.append(False)
		board.append(row)

	while True:
		import time
		time.sleep(0.05)
		print_board(board)
		board = next_state(board)