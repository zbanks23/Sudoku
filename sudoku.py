from board import Board
from cell import Cell
from sudoku_generator import*
import pygame, sys

def draw_border(row,col,color):
    pygame.draw.line(
        screen,
        color,
        (col * 80, row * 80),
        (col * 80, (row + 1) * 80),
        4
    )
    # right line
    pygame.draw.line(
        screen,
        color,
        ((col + 1) * 80, row * 80),
        ((col + 1) * 80, (row + 1) * 80),
        4
    )
    # top line
    pygame.draw.line(
        screen,
        color,
        (col * 80, row * 80),
        ((col + 1) * 80, row * 80),
        4
    )
    # bottom line
    pygame.draw.line(
        screen,
        color,
        ((col + 0) * 80, (row + 1) * 80),
        ((col + 1) * 80, (row + 1) * 80),
        4
    )

def play_game(game_board):
    screen.fill((255, 255, 255))
    game_board.draw()


    button_font = pygame.font.Font(None, 60)

    # button text
    reset_text = button_font.render("Reset", 0, (255, 255, 255))
    restart_text = button_font.render("Restart", 0, (255, 255, 255))
    exit_text = button_font.render("Exit", 0, (255, 255, 255))

    # button background and text
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill((65, 105, 225))
    reset_surface.blit(reset_text, (10, 10))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill((65, 105, 225))
    restart_surface.blit(restart_text, (10, 10))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill((65, 105, 225))
    exit_surface.blit(exit_text, (10, 10))

    # Initialize button rectangle
    reset_rectangle = reset_surface.get_rect(
        center=(160, 770))
    restart_rectangle = restart_surface.get_rect(
        center=(360, 770))
    exit_rectangle = exit_surface.get_rect(
        center=(560, 770))

    # Draw buttons
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    for cell in game_board.cells:
        cell.draw()

    old_x, old_y = None, None
    while True:
        if game_board.is_full():
            if game_board.check_board():
                draw_game_won_screen()
            else:
                draw_game_lost_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if old_x != None:
                    if event.key == pygame.K_DOWN:
                        if old_y < 640:
                            col = old_x // 80
                            row = old_y // 80
                            draw_border(row,col,(0,0,0))
                            col = old_x // 80
                            row = old_y // 80 + 1
                            draw_border(row, col, (255, 0, 0))

                            old_y = row * 80 +40
                    elif event.key == pygame.K_RIGHT:
                        if old_x < 640:
                            col = old_x // 80
                            row = old_y // 80
                            draw_border(row,col,(0,0,0))
                            col = old_x // 80 + 1
                            row = old_y // 80
                            draw_border(row, col, (255, 0, 0))

                            old_x = col * 80 + 40
                    elif event.key == pygame.K_UP:
                        if old_y >= 80:
                            col = old_x // 80
                            row = old_y // 80
                            draw_border(row,col,(0,0,0))
                            col = old_x // 80
                            row = old_y // 80 - 1
                            draw_border(row, col, (255, 0, 0))

                            old_y = row * 80

                    elif event.key == pygame.K_LEFT:
                        if old_x >= 80:
                            col = old_x // 80
                            row = old_y // 80
                            draw_border(row,col,(0,0,0))
                            col = old_x // 80 -1
                            row = old_y // 80
                            draw_border(row, col, (255, 0, 0))

                            old_x = col * 80
                    elif event.key == pygame.K_1:
                        r = old_y//80
                        c = old_x//80
                        if r <= 9 and c<=9:
                            game_board.cells[r*9+c].set_sketch_value(1)
                    elif event.key == pygame.K_2:
                        r = old_y//80
                        c = old_x//80
                        if r <=9 and c<=9:
                            game_board.cells[r*9+c].set_sketch_value(2)
                    elif event.key == pygame.K_3:
                        r = old_y//80
                        c = old_x//80
                        if r <=9 and c<=9:
                            game_board.cells[r*9+c].set_sketch_value(3)
                    elif event.key == pygame.K_4:
                        r = old_y//80
                        c = old_x//80
                        if r <=9 and c<=9:
                            game_board.cells[r*9+c].set_sketch_value(4)
                    elif event.key == pygame.K_5:
                        r = old_y//80
                        c = old_x//80
                        if r <=9 and c<=9:
                            game_board.cells[r*9+c].set_sketch_value(5)
                    elif event.key == pygame.K_6:
                        r = old_y//80
                        c = old_x//80
                        if r <=9 and c<=9:
                            game_board.cells[r*9+c].set_sketch_value(6)
                    elif event.key == pygame.K_7:
                        r = old_y//80
                        c = old_x//80
                        if r <=9 and c<=9:
                            game_board.cells[r*9+c].set_sketch_value(7)
                    elif event.key == pygame.K_8:
                        r = old_y//80
                        c = old_x//80
                        if r <=9 and c<=9:
                            game_board.cells[r*9+c].set_sketch_value(8)
                    elif event.key == pygame.K_9:
                        r = old_y//80
                        c = old_x//80
                        if r <=9 and c<=9:
                            game_board.cells[r*9+c].set_sketch_value(9)
                    elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                        r = old_y // 80
                        c = old_x // 80
                        game_board.cells[r*9+c].set_cell_value(game_board.cells[r*9+c].sketch_value)
                        game_board.cells[r * 9 + c].draw()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

                elif restart_rectangle.collidepoint(event.pos):
                    screen.fill((255, 255, 255))
                    difficulty = draw_welcome_screen()
                    game_board = Board(screen_width, screen_height, screen, difficulty)
                    play_game(game_board)

                elif reset_rectangle.collidepoint(event.pos):
                    screen.fill((255, 255, 255))
                    game_board.reset_to_original()
                    for cell in game_board.cells:
                        cell.draw()
                    game_board.draw()
                    screen.blit(reset_surface, reset_rectangle)
                    screen.blit(restart_surface, restart_rectangle)
                    screen.blit(exit_surface, exit_rectangle)

                else:
                    x,y = pygame.mouse.get_pos()
                    if old_x != None:
                        col = old_x // 80
                        row = old_y // 80
                        draw_border(row, col, (0, 0, 0))

                    if x < 720 and y<720:
                        col = x//80
                        row = y//80
                        draw_border(row, col, (255, 0, 0))

                        old_y = y
                        old_x = x


        pygame.display.update()


def draw_picture():
    screen.fill((255, 255, 255))

    # imports welconme image
    welcome_image = pygame.image.load("welcome.png")
    screen.blit(welcome_image, (90,180))


    # draws border around image
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (86, 180),
        (635, 180),
        10
    )
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (630, 180),
        (630, 540),
        10
    )
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (635, 540),
        (86, 540),
        10
    )
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (90, 180),
        (90, 540),
        10
    )


def draw_welcome_screen():
    #creates fonts
    welcome_font = pygame.font.Font(None, 100)
    prompt_font = pygame.font.Font(None, 70 )
    button_font = pygame.font.Font(None, 50)

    draw_picture()

    # adds weclome message
    welcome_surface = welcome_font.render("Welcome to Sudoku", 0, (0,0,0))
    welcome_rectangle = welcome_surface.get_rect(
        center=(360, 100))
    screen.blit(welcome_surface, welcome_rectangle)

    # adds "select a gamemode"
    prompt_surface = prompt_font.render("Select a Game Mode", 0, (0, 0, 0))
    prompt_rectangle = prompt_surface.get_rect(
        center=(360, 580))
    screen.blit(prompt_surface, prompt_rectangle)

    # adds buttons
    # button text
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    # button background and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill((65,105,225))
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill((65,105,225))
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill((65, 105, 225))
    hard_surface.blit(hard_text, (10, 10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(
        center=(160,655))
    medium_rectangle = medium_surface.get_rect(
        center=(360,655))
    hard_rectangle = hard_surface.get_rect(
        center=(560, 655))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):

                    return "easy"
                elif medium_rectangle.collidepoint(event.pos):

                    return "medium"
                elif hard_rectangle.collidepoint(event.pos):

                    return "hard"
        pygame.display.update()


def draw_game_won_screen():
    screen.fill((255, 255, 255))

    victory_message = pygame.font.Font(None, 85)
    button_font = pygame.font.Font(None, 70)

    draw_picture()

    # adds victory message
    victory_message_surface = victory_message.render("Congrats, Game Won!", 0, (0, 0, 0))
    victory_rectangle = victory_message_surface.get_rect(
        center=(360, 100))
    screen.blit(victory_message_surface, victory_rectangle)

    #adds exit button
    exit_text = button_font.render("Exit", 0, (255, 255, 255))

    # button background and text
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill((65,105,225))
    exit_surface.blit(exit_text, (10, 10))

    exit_rectangle = exit_surface.get_rect(
        center=(360, 630))

    screen.blit(exit_surface, exit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def draw_game_lost_screen():
    screen.fill((255, 255, 255))

    lost_message = pygame.font.Font(None, 85)
    button_font = pygame.font.Font(None, 70)

    draw_picture()

    # adds victory message
    lost_message_surface = lost_message.render("Sorry, Game Over :(", 0, (0, 0, 0))
    lost_rectangle = lost_message_surface.get_rect(
        center=(360, 100))
    screen.blit(lost_message_surface, lost_rectangle)

    # adds exit button
    restart_text = button_font.render("Restart", 0, (255, 255, 255))

    # button background and text
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill((65, 105, 225))
    restart_surface.blit(restart_text, (10, 10))

    restart_rectangle = restart_surface.get_rect(
        center=(360, 630))

    screen.blit(restart_surface, restart_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if restart_rectangle.collidepoint(event.pos):
                    screen.fill((255, 255, 255))
                    difficulty = draw_welcome_screen()
                    game_board = Board(screen_width, screen_height, screen, difficulty)
                    play_game(game_board)



            pygame.display.update()

        pygame.display.update()


if __name__ == '__main__':

    pygame.init()

    screen_width = 720
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height+100))
    pygame.display.set_caption("Sudoku")
    screen.fill((255, 255, 255))

    difficulty = draw_welcome_screen()

    game_board = Board(screen_width, screen_height, screen, difficulty)

    play_game(game_board)






