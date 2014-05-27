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

import sys, curses, signal, time

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
                    new[r][c] = 0
            if not board[r][c]:
                if neighbors == 3:
                    new[r][c] = 1
    return new

def ch(x):
    if x:
        return "X"
    else:
        return " "

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    board = []
    rows = input()
    for i in range(0, rows):
        row = []
        line = raw_input()
        for each in line:
            if each == "X":
                row.append(1)
            elif each == "_":
                row.append(0)
        board.append(row)

    while 1:
        board = next_state(board)
        # print board
        for i, row in enumerate(board):
            # screen.addstr(i, j, board[i][j], curses.color_pair(1))
            r = [ch(x) for x in row]
            stdscr.addstr(i,0, " ".join(r), curses.color_pair(1))
        stdscr.refresh()
        time.sleep(0.1)

if __name__=='__main__':
    curses.wrapper(main) 
