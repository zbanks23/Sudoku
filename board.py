import pygame

# initializes pygame
from cell import *
from sudoku_generator import *

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        remove_cells = 0
        if difficulty == "easy":
            remove_cells = 30
        elif difficulty == "medium":
            remove_cells = 40
        elif difficulty == "hard":
            remove_cells = 50

        self.sudoku_board = generate_sudoku(9, remove_cells)

        self.cells = []
        for row in range(0, 9):
            for col in range(0, 9):
                self.cells.append(Cell(self.sudoku_board[row][col], row, col, self.screen))


        self.previous_row = None
        self.previous_col = None

    def draw(self):
        # draws the thick horizontal lines for 3x3 boxes
        for i in range(1, 3):
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (0, i * self.height // 3),
                (self.width, i * self.height // 3),
                10
            )

        # draws the thick vertical lines for 3x3 boxes
        for i in range(1, 3):
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (i * self.width // 3, 0),
                (i * self.width // 3, self.height),
                10
            )
        # need code to draw each cell
        for i in range(1, 9):
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (0, i * self.height // 9),
                (self.width, i * self.height // 9),
                4
            )
        for i in range(1, 9):
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (i * self.width // 9, 0),
                (i * self.width // 9, self.height),
                4
                )

        pygame.draw.line(
            self.screen,
            (0,0,0),
            (0,self.height),
            (self.width, self.height),
            4
        )

    def select(self, row, col):
        if self.selectrow != None and self.selectcol != None:
            previous_cell = self.cells[self.previous_row][self.previous_col]
            previous_cell.selected = False
        selected_cell = self.cells[row][col]
        selected_cell.selected = True
        self.previous_row = row
        self.previous_col = col

    def click(self,x,y):
        size = self.cells[0][0].cell_size
        col = x//size
        row = y//size
        if 0 <= row < 9 and 0 <= col < 9:
            return row , col
        else:
            return None



    def clear(self):
        for row in range(0,9):
            for col in range(0,9):
                cell = self.cells[row][col]
                if cell.selected:
                    cell.value = 0
                    cell.sketched_value = None

    def sketch(self, value):
        for row in range(0,9):
            for col in range(0,9):
                cell = self.cells[row][col]
                if cell.selected:
                    cell.set_sketch_value(value)

    def place_number(self, value):
        for row in range(0,9):
            for col in range(0,9):
                cell = self.cells[row][col]
                if cell.selected:
                    cell.set_cell_value(value)

    def reset_to_original(self):
        self.cells = []
        for row in range(0, 9):
            for col in range(0, 9):
                self.cells.append(Cell(self.sudoku_board[row][col], row, col, self.screen))




    def is_full(self):
        for cell in self.cells:
            if cell.value == 0:
                return False
        return True

    def update_board(self):
        for row in range(0,9):
            for col in range(0,9):
                cell = self.cells[row][col]
                self.sudoku_board[row][col] = cell.value

    def find_empty(self):
        for row in range(0, 9):
            for col in range(0, 9):
                cell = self.cells[row][col]
                if cell.value == 0:
                    return row,col

    def check_board(self):
        finished_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        for r in range(0,len(finished_board)):
            for c in range(0, len(finished_board[0])):
                finished_board[r][c] = self.cells[r*9+c].value


        for r in range(0, len(finished_board)):
            line = finished_board[r]
            if len(line) != len(set(line)):
                return False

        for r in range(0,len(finished_board)):
            for c in range(0, len(finished_board[0])):
                finished_board[c][r] = self.cells[r*9+c].value

        for r in range(0, len(finished_board)):
            line = finished_board[r]
            if len(line) != len(set(line)):
                return False

        for r in range(0, len(finished_board),3):
            for c in range(0, len(finished_board[0]),3):

                box_list = []

                for row in range(r,r+3):
                    for col in range(c, c+3):
                        box_list.append(finished_board[row][col])

                if len(box_list) != len(set(box_list)):
                    return False
        return True


