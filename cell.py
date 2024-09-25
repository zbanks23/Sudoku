import pygame
pygame.init()

class Cell:
    num_font = pygame.font.Font(None, 80)
    sketch_font = pygame.font.Font(None, 35)

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketch_value(self, v):
        self.sketch_value = str(v)
        if self.sketch_value != "0" and self.value == 0:
            # erases existing sketches
            pygame.draw.line(
                self.screen,
                # this color should match with the screen's background color
                (255,255,255),
                (((self.col) * 80 + 14), ((self.row) * 80 + 8)),
                ((self.col) * 80 + 14, (self.row) * 80 + 40),
                18
            )
            # sketch the number in the cell
            number = self.sketch_font.render(self.sketch_value, 0, (128, 128, 128))
            number_rect = number.get_rect(center=(((self.col) * 80)+14, ((self.row) * 80+18)))
            self.screen.blit(number, number_rect)

    def draw(self):
        # erases existing sketches
        pygame.draw.line(
            self.screen,
            # this color should match with the screen's background color
            (255, 255, 255),
            (((self.col) * 80 + 14), ((self.row) * 80 + 8)),
            ((self.col) * 80 + 14, (self.row) * 80 + 40),
            18
        )
        # printing the number
        if self.value != 0:
            self.value = str(self.value)
            number = self.num_font.render(self.value, 0, (0, 0, 0))
            number_rect = number.get_rect(center=(((self.col+ 1) * 80) - 40, ((self.row+1) * 80) - 40))
            self.screen.blit(number, number_rect)

        # outline the border to be red when currently selected
        # left line
        x=0
        if x == 1:
            pygame.draw.line(
                self.screen,
                (255, 0, 0),
                (self.col * 80, self.row * 80),
                (self.col * 80, (self.row + 1) * 80),
                10
            )
            # right line
            pygame.draw.line(
                self.screen,
                (255, 0, 0),
                ((self.col + 1) * 80, self.row * 80),
                ((self.col +1) * 80, (self.row + 1) * 80),
                10
            )
            # top line
            pygame.draw.line(
                self.screen,
                (255, 0, 0),
                (self.col * 80, self.row * 80),
                ((self.col+1) * 80, self.row * 80),
                10
            )
            # bottom line
            pygame.draw.line(
                self.screen,
                (255, 0, 0),
                ((self.col + 0) * 80, (self.row + 1) * 80),
                ((self.col + 1) * 80, (self.row + 1) * 80),
                10
            )

    def border_reset(self):
        # recolor the border back to black
        # top line
        pygame.draw.line(
            self.screen,
            (0, 0, 0),
            ((self.col - 1) * 80, (self.row - 1) * 80),
            (self.col * 80, (self.row - 1) * 80),
            4
        )
        # bottom line
        pygame.draw.line(
            self.screen,
            (0, 0, 0),
            ((self.col - 1) * 80, self.row * 80),
            (self.col * 80, self.row * 80),
            4
        )
        # left line
        pygame.draw.line(
            self.screen,
            (0, 0, 0),
            ((self.col - 1) * 80, (self.row - 1) * 80),
            ((self.col - 1) * 80, self.row * 80),
            4
        )
        # right line
        pygame.draw.line(
            self.screen,
            (0, 0, 0),
            (self.col * 80, (self.row - 1) * 80),
            (self.col * 80, self.row * 80),
            4
        )