###################################
# Python maze generator program
# using PyGame for animation
# Davis MT
# Python 3.4
# 10.02.2018
###################################

import pygame
import time
import random

# set up pygame window
WIDTH = 800
HEIGHT = 600
FPS = 30

# Define colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
BLUE = (0, 0, 200)
BRIGHT_BLUE = (0, 0, 255)
YELLOW = (255 ,255 ,0)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BRIGHT_RED = (255, 0, 0)
BRIGHT_PINK = (255, 51, 153)
PINK = (255, 0, 127)

# initalise Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()

# setup maze variables
x = 0                    # x axis
y = 0                    # y axis
w = 20                   # width of cell
grid = []
visited = []
stack = []
solution = {}


# build the grid
def build_grid_1(x, y, w):
    for i in range(1,21):
        x = 20                                                            # set x coordinate to start position
        y = y + 20                                                        # start a new row
        for j in range(1, 21):
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])           # top of cell
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])   # right of cell
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])   # bottom of cell
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])           # left of cell
            grid.append((x,y))                                            # add cell to grid list
            x = x + 20                                                    # move cell to new position

edges = {}

def display_girl(x, y, teacher):
    screen.blit(teacher, (x, y))


def build_grid_2(x, y, w):
    for i in range(1,21):
        x = 20                                                            # set x coordinate to start position
        y = y + 20                                                        # start a new row
        for j in range(1, 21):
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])           # top of cell
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])   # right of cell
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])   # bottom of cell
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])           # left of cell
            grid.append((x,y))                                           # add cell to grid list
            edges[(x, y)] = random.randint(0, 1000)
            x = x + 20
    screen.fill(BLACK)
    teacher = pygame.image.load("teacher.png")
    pygame.display.set_icon(teacher)
    display_girl(500, 400, teacher)

path = []

def build_grid_3(x, y, w):
    for i in range(1,21):
        x = 20                                                            # set x coordinate to start position
        y = y + 20                                                        # start a new row
        for j in range(1, 21):
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])           # top of cell
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])   # right of cell
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])   # bottom of cell
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])           # left of cell
            grid.append((x,y))
            num = random.randint(0, 1000)                                        # add cell to grid list
            path.append((num, x, y))
            x = x + 20
    screen.fill(BLACK)
    teacher = pygame.image.load("teacher.png")
    pygame.display.set_icon(teacher)
    display_girl(500, 400, teacher)
    path.sort()


     



def push_up(x, y, color):
    pygame.draw.rect(screen, color, (x + 1, y - w + 1, 19, 39), 0)         # draw a rectangle twice the width of the cell
    pygame.display.update()                                              # to animate the wall being removed


def push_down(x, y, color):
    pygame.draw.rect(screen, color, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()


def push_left(x, y, color):
    pygame.draw.rect(screen, color, (x - w +1, y +1, 39, 19), 0)
    pygame.display.update()


def push_right(x, y, color):
    pygame.draw.rect(screen, color, (x +1, y +1, 39, 19), 0)
    pygame.display.update()


def single_cell( x, y):
    pygame.draw.rect(screen, GREEN, (x +1, y +1, 18, 18), 0)          # draw a single width cell
    pygame.display.update()


def backtracking_cell(x, y):
    pygame.draw.rect(screen, BLUE, (x +1, y +1, 18, 18), 0)        # used to re-colour the path after single_cell
    pygame.display.update()                                        # has visited cell


def solution_cell(x,y):
    pygame.draw.rect(screen, YELLOW, (x+8, y+8, 5, 5), 0)             # used to show the solution
    pygame.display.update()                                        # has visited cell


def carve_out_maze_1(x,y):
    single_cell(x, y)                                              # starting positing of maze
    stack.append((x,y))                                            # place starting cell into stack
    visited.append((x,y))                                          # add starting cell to visited list
    while len(stack) > 0:                                          # loop until stack is empty
        time.sleep(.07)                                            # slow program now a bit
        cell = []                                                  # define cell list
        if (x + w, y) not in visited and (x + w, y) in grid:       # right cell available?
            cell.append("right")                                   # if yes add to cell list

        if (x - w, y) not in visited and (x - w, y) in grid:       # left cell available?
            cell.append("left")

        if (x , y + w) not in visited and (x , y + w) in grid:     # down cell available?
            cell.append("down")

        if (x, y - w) not in visited and (x , y - w) in grid:      # up cell available?
            cell.append("up")

        if len(cell) > 0:                                          # check to see if cell list is empty
            cell_chosen = (random.choice(cell))                    # select one of the cell randomly

            if cell_chosen == "right":                             # if this cell has been chosen
                push_right(x, y, BLUE)                                   # call push_right function
                solution[(x + w, y)] = x, y                        # solution = dictionary key = new cell, other = current cell
                x = x + w                                          # make this cell the current cell
                visited.append((x, y))                              # add to visited list
                stack.append((x, y))                                # place current cell on to stack

            elif cell_chosen == "left":
                push_left(x, y, BLUE)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                push_down(x, y, BLUE)
                solution[(x , y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                push_up(x, y, BLUE)
                solution[(x , y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()                                    # if no cells are available pop one from the stack
            single_cell(x, y)                                     # use single_cell function to show backtracking image
            time.sleep(.05)                                       # slow program down a bit
            backtracking_cell(x, y)                               # change colour to green to identify backtracking path

def carve_out_maze_2(x,y, stack):
    single_cell(x, y)
    stack.append((x, y))
    visited.append((x, y))
    while len(stack) > 0:
        time.sleep(.07)
        cell = []
        stack = []
        for i in visited:
            x, y = i
            if (x + w, y) not in visited and (x + w, y) in grid:
                cell.append((edges[(x + w, y)],(x, y), x + w, y, "right"))
            if (x - w, y) not in visited and (x - w, y) in grid:
                cell.append((edges[(x - w, y)],(x, y), x - w, y, "left"))
            if (x , y + w) not in visited and (x , y + w) in grid:
                cell.append((edges[(x , y + w)],(x, y), x, y + w, "down"))
            if (x , y - w) not in visited and (x , y - w) in grid:
                cell.append((edges[(x , y - w)], (x, y), x, y - w, "up"))
        if cell:
            b = min(cell)
            cell.remove(b)
            stack.append((b[0], b[1]))
            cell = []
            solution[(b[2], b[3])] = b[1]
            x = b[2]
            y = b[3]
            if b[4] == "right":
                push_right(x, y, WHITE)                                   # call push_right function
                # solution[(x + w, y)] = x, y                      # solution = dictionary key = new cell, other = current cell
                # x = x + w                                          # make this cell the current cell
                visited.append((x, y))                              # add to visited list
                stack.append((x, y))
            elif b[4] == "left":
                push_left(x, y, WHITE)
                # x = x - w
                visited.append((x, y))                              # add to visited list
                stack.append((x, y))
            elif b[4] == "down":
                push_down(x, y, WHITE)
                # y = y + w
                visited.append((x, y))                              # add to visited list
                stack.append((x, y))
            elif b[4] == "up":
                push_up(x, y, WHITE)
                # y = y - w
                visited.append((x, y))                              # add to visited list
                stack.append((x, y))
        else:
            break
            




            





def plot_route_back(x,y):
    solution_cell(x, y)                                          # solution list contains all the coordinates to route back to start
    while (x, y) != (20,20):                                     # loop until cell position == start position
        x, y = solution[x, y]                                    # "key value" now becomes the new key
        solution_cell(x, y)
        print(x, y)                                      # animate route back
        time.sleep(.1)
    pygame.quit()



# x, y = 20, 20                     # starting position of grid
# build_grid(40, 0, 20)            # 1st argument = x value, 2nd argument = y value, 3rd argument = width of cell
# carve_out_maze(x,y)              # call build the maze  function
# plot_route_back(400, 400)         # call the plot solution function

def text_object(text, font):
    text_surf = font.render(text, True, BLACK)
    return text_surf, text_surf.get_rect()

# game_intro()

def RECURSIVE_BACKTRACKER():
    running = True
    while running:
        # keep running at the at the right speed
        clock.tick(FPS)
        # process input (events)
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)
        x, y = 20, 20                     # starting position of grid
        build_grid_1(40, 0, 20)            # 1st argument = x value, 2nd argument = y value, 3rd argument = width of cell
        carve_out_maze_1(x,y)              # call build the maze  function
        plot_route_back(400, 400)
        break         # call the plot solution function




def PRIM_ALGORITHM():
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)
        
        pygame.display.update() 
        x, y = 20, 20                     # starting position of grid
        build_grid_2(40, 0, 20)
        carve_out_maze_2(x,y,stack)
        print(solution)
        plot_route_back(400,400)
    
def KRUSKAL_ALGORITHM():
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)
        
        pygame.display.update()
        x, y = 20, 20                     # starting position of grid
        build_grid_3(40, 0, 20)
        # carve_out_maze_3(x,y,stack) 



        
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
        
        screen.fill(GREEN)
        large_text = pygame.font.Font("freesansbold.ttf", 60)
        text_surf, text_rect = text_object("MAZE GENERATOR", large_text)
        text_rect.center = ((WIDTH / 2), (HEIGHT / 4))
        screen.blit(text_surf, text_rect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 17 + 419 > mouse[0] > 17 and 350 + 50 > mouse[1] > 350:
            pygame.draw.rect(screen, BLUE, (17, 350, 419, 50)) #(x, y, width, height)
            if click[0] == 1:
                
                RECURSIVE_BACKTRACKER()
        else:
            pygame.draw.rect(screen, BRIGHT_BLUE, (17, 350, 419, 50)) #(x, y, width, height)


        if 443 + 337 > mouse[0] > 443 and 350 + 50 > mouse[1] > 350:
            pygame.draw.rect(screen, RED, (443, 350, 337, 50)) #(x, y, width, height)
            if click[0] == 1:
                PRIM_ALGORITHM()
        else:
            pygame.draw.rect(screen, BRIGHT_RED, (443, 350, 337, 50)) #(x, y, width, height)
        
        if 218 + 337 > mouse[0] > 218 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(screen, PINK, (218, 450, 337, 50)) #(x, y, width, height)
            if click[0] == 1:
                KRUSKAL_ALGORITHM()
        else:
            pygame.draw.rect(screen, BRIGHT_PINK, (218, 450, 337, 50)) #(x, y, width, height)

        small_text1 = pygame.font.Font("freesansbold.ttf", 20)
        text_surf, text_rect = text_object("RECURSIVE BACKTRACKING ALGORITHM", small_text1)
        text_rect.center = ((150+(150/2)), (350+(50/2)))
        screen.blit(text_surf, text_rect)
        

        small_text2 = pygame.font.Font("freesansbold.ttf", 20)
        text_surf, text_rect = text_object("PRIMS'S ALGORITHM", small_text2)
        text_rect.center = ((443+(337/2)), (350+(50/2)))
        screen.blit(text_surf, text_rect)
        

        small_text3 = pygame.font.Font("freesansbold.ttf", 20)
        text_surf, text_rect = text_object("KRUSKAL'S ALGORITHM", small_text3)
        text_rect.center = ((218+(337/2)), (450+(50/2)))
        screen.blit(text_surf, text_rect)
        pygame.display.update()

        # clock.tick(15)
game_intro()
# ##### pygame loop #######
# entered()
pygame.quit()
# quit()
        
                

