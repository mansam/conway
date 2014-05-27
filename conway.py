# Copyright (C) 2013 Samuel Lucidi <mansam@csh.rit.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
