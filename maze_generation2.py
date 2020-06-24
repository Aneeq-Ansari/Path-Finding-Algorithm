

import pygame
import time
import random
from pygame import mixer


# set up pygame window
WIDTH = 1369
HEIGHT = 700
FPS = 30

G = {}


# Define colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
BLUE = (0, 0, 200)
BRIGHT_BLUE = (0, 0, 255)
YELLOW = (255 ,220 ,0)
BRIGHT_YELLOW = (255, 255, 51)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BRIGHT_RED = (255, 0, 0)
BRIGHT_PINK = (255, 51, 153)
PINK = (255, 0, 127)
PURPLE = (75,0,130)
BRIGHT_PURPLE = (75,50,130)
ORANGE = (255,69,0)
BRIGHT_ORANGE = (255,119,0)
# Define helper functions:

color_lst = [RED, BLUE, BRIGHT_BLUE, BRIGHT_RED, PURPLE]
maze_color = random.choice(color_lst)
maze_color = WHITE



# initalise Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()

# mixer.music.load("journey.wav")
# mixer.music.play(-1)

# setup maze variables
x = 0                    
y = 0                    
w = 20                   
grid = []
visited = []
stack = []
solution = {}

G = {}



# build the grid
def build_grid_1(x, y, w):
    for i in range(1,31):
        x = 17                                                         
        y = y + 17                                                        
        for j in range(1, 51):
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])           
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])   
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])   
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])           
            grid.append((x,y))                                            
            x = x + 17                                                    
    screen.fill(BLACK)
edges = {}

def display_girl(x, y, teacher):
    screen.blit(teacher, (x, y))

maze = pygame.image.load("maze2.png")
pygame.display.set_icon(maze)

def display_maze(maze, x, y):
    screen.blit(maze, (x, y))
    
def display_tree(x, y, tree):
    screen.blit(tree, (x, y))

def display_volume(x, y, volume):
    screen.blit(volume, (x, y))

def build_grid_2(x, y, w):
    for i in range(1,31):
        x = 17                                                           
        y = y + 17                                                       
        for j in range(1, 51):
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])           
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])   
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])   
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])           
            grid.append((x,y))                                           
            edges[(x, y)] = random.randint(0, 1000)
            x = x + 17
    screen.fill(BLACK)
    # teacher = pygame.image.load("teacher.png")
    # pygame.display.set_icon(teacher)
    # display_girl(500, 400, teacher)

tree = pygame.image.load("tuscany.png")
pygame.display.set_icon(tree)


volume = pygame.image.load("volume.png")
pygame.display.set_icon(volume)
path = []


def selection_sort(lst):
    for i in range(len(lst)):
        minimum = i
        for j in range(i, len(lst)):
            if lst[minimum][2] > lst[j][2]:
                lst[j], lst[minimum] = lst[minimum], lst[j]
    return lst


def push_up(x, y, color):
    pygame.draw.rect(screen, color, (x+1 , y - w  +4, 16, 32), 0)         
    pygame.display.update()                                              


def push_down(x, y, color):
    pygame.draw.rect(screen, color, (x +  1, y + 2, 16, 32), 0)
    pygame.display.update()


def push_left(x, y, color):
    pygame.draw.rect(screen, color, (x - w+4 , y +1, 32, 16), 0)
    pygame.display.update()


def push_right(x, y, color):
    pygame.draw.rect(screen, color, (x +1, y +1, 33, 16), 0)
    pygame.display.update()


def single_cell(x, y, color):
    pygame.draw.rect(screen, color, (x +1, y +1, 16, 16), 0)          
    pygame.display.update()

def draw_vertical(x, y):
    pygame.draw.rect(screen, GREEN, (x +1, 20, 18, 400), 0) 
    pygame.display.update()

def draw_horizontal(x, y):
    pygame.draw.rect(screen, GREEN, (20, y+1, 400, 18), 0) 
    pygame.display.update()

def backtracking_cell(x, y, maze_color):
    pygame.draw.rect(screen, maze_color, (x +1, y +1, 16, 16), 0)        
    pygame.display.update()                                        

def backtracking_cell_1(x, y, maze_color):
    pygame.draw.rect(screen, maze_color, (x , y +1, 17, 16), 0)        
    pygame.display.update()

def solution_cell(x,y):
    pygame.draw.rect(screen, YELLOW, (x+8, y+8, 5, 5), 0)             
    pygame.display.update()                                        

def find_node(dis_set, node):
    for j in range(len(dis_set)):
        if node in dis_set[j]:
            return j

def carve_out_maze_1(x,y, maze_color):
    single_cell(x, y, GREEN)                                              
    stack.append((x,y))                                            
    visited.append((x,y))
    w = 17                                     
    while len(stack) > 0:
        if (x, y) not in G:
            G[(x, y)] = []                                           
        time.sleep(0.01)                                           
        cell = []                                                  
        if (x + w, y) not in visited and (x + w, y) in grid:       
            cell.append("right")                                   

        if (x - w, y) not in visited and (x - w, y) in grid:       
            cell.append("left")

        if (x , y + w) not in visited and (x , y + w) in grid:     
            cell.append("down")

        if (x, y - w) not in visited and (x , y - w) in grid:      
            cell.append("up")

        if len(cell) > 0:                                          
            cell_chosen = (random.choice(cell))                    

            if cell_chosen == "right":                             
                push_right(x, y, maze_color)                                   
                solution[(x + w, y)] = x, y
                G[(x, y)].append((x+w, y))                        
                x = x + w                                          
                visited.append((x, y))                              
                stack.append((x, y))                                

            elif cell_chosen == "left":
                push_left(x, y, maze_color)
                solution[(x - w, y)] = x, y
                G[(x, y)].append((x-w, y))
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                push_down(x, y, maze_color)
                solution[(x , y + w)] = x, y
                G[(x, y)].append((x, y+w))
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                push_up(x, y, maze_color)
                solution[(x , y - w)] = x, y
                G[(x, y)].append((x, y-w))
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()                                    
            single_cell(x, y, GREEN)                                     
            time.sleep(.01)                                       
            backtracking_cell(x, y, maze_color)                               

def carve_out_maze_2(x,y, stack, maze_color):
    # single_cell(x, y, GREEN)
    stack.append((x, y))
    visited.append((x, y))
    w = 17
    while len(stack) > 0:
        # time.sleep(0.001)
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
            x, y = b[1]
            # single_cell(x, y, GREEN)
            # time.sleep(0.03)
            if b[4] == "right":
                push_right(x, y, maze_color)                                                                          
                visited.append((x + w, y))                              
                stack.append((x + w, y))
            elif b[4] == "left":
                push_left(x, y, maze_color)
                visited.append((x - w, y))                              
                stack.append((x - w, y))
            elif b[4] == "down":
                push_down(x, y, maze_color)
                visited.append((x , y + w))                              
                stack.append((x , y + w))
            elif b[4] == "up":
                push_up(x, y, maze_color)
                visited.append((x , y - w))                              
                stack.append((x , y - w))
        else:
            break
            
def is_empty(stack):
    return len(stack) == 0


        

def plot_route_back(x,y):
    solution_cell(x, y)                                         
    while (x, y) != (17,17):                                  
        x, y = solution[x, y]
        print(x, y)                                   
        solution_cell(x, y)                                    
        time.sleep(.1)
    return 

def plot_route_back_1(x,y):
    solution_cell(x, y)
    visited = []                                     
    while (x, y) != (17,17):
        visited.append((x, y))
        if (x, y) not in solution:
            while True:
                x += 17
                if solution[x, y] == (x, y-17):
                    break
        x, y = solution[x, y]                              
        solution_cell(x, y)                                    
        time.sleep(.1)
    return 



x_change = 0
y_change = 0

def display_player(player, x, y):
    screen.blit(player, (x, y))

def text_object(text, font):
    text_surf = font.render(text, True, BLACK)
    return text_surf, text_surf.get_rect()
 
# game_intro()

def RECURSIVE_BACKTRACKER_1(x_change, y_change):
    running = True
    check = False
    
    while running:
        # keep running at the at the right speed
        clock.tick(FPS)
        
        # process input (events)
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    plot_route_back(850,510)
                    running = False
                if event.key == pygame.K_RIGHT:
                    if (x + 17, y) in G[(x, y)]:
                        # backtracking_cell(x, y, maze_color)
                        # x_change += 17
                        x += 17
                if event.key == pygame.K_LEFT:
                    if (x - 17, y) in G[(x, y)]:
                        # backtracking_cell(x, y, maze_color)
                        # x_change -= 17
                        x -= 17
                if event.key == pygame.K_UP:
                    if (x, y - 17) in G[(x, y)]:
                        # backtracking_cell(x, y, maze_color)
                        # y_change-= 17 
                        y -= 17
                if event.key == pygame.K_DOWN:
                    if (x, y + 17) in G[(x, y)]:
                        # backtracking_cell(x, y, maze_color)
                        # y_change += 17
                        y += 17
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0; y_change = 0
        if check:
            x += x_change
            y += y_change
            backtracking_cell(x, y, GREEN)
            # pygame.display.update()
        else:
            screen.fill(BLACK)
            x, y = 17, 17                     
            build_grid_1(17, 0, 17)            
            carve_out_maze_1(x,y, maze_color)
            # plot_route_back(850,510)
            x, y = 17, 17
            check = True
            continue
         


def PRIM_ALGORITHM(playerx_change, playery_change, check = True):
    running = True
    check = False
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    plot_route_back(850,510)
                    running = False
                if event.key == pygame.K_RIGHT:
                    playerx_change = 2
                if event.key == pygame.K_LEFT:
                    playerx_change = -2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerx_change = 0
            
        
        if check:
            player_x += playerx_change
            player_y += playery_change
            display_player(player, player_x, player_y)
            pygame.display.update()
        else:
            screen.fill(BLACK)
            pygame.display.update()
            # for i in range(20, 401, 20):
            # for j in range(20, 401, 20):
            #     x, y = i, j
            lst = [(i, j)for i in range(17, 851, 17) for j in range(17, 511, 17)]
            x, y = random.choice(lst)                    
            build_grid_2(17, 0, 17)
            carve_out_maze_2(x,y,stack, maze_color)
            plot_route_back(850,510)
            # display_player(player, 20, 20)
            pygame.display.update()
            check = True



        
def game_intro():
    intro = True
    num = 0
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
        
        screen.fill(GREEN)
        display_tree(985, (HEIGHT / 2) - 100 , tree)
        large_text = pygame.font.Font("freesansbold.ttf", 60)
        text_surf, text_rect = text_object("MAZE GENERATOR", large_text)
        text_rect.center = ((WIDTH / 2), 50)
        screen.blit(text_surf, text_rect)

        # if not num % 2:
        #     mixer.music.load("journey.wav")
        #     mixer.music.play(-1)      
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # pygame.draw.rect(screen, BRIGHT_ORANGE, (1230, 45, 100, 90))
        display_maze(maze, (WIDTH/2) - 50,130)
        

        if 1230 + 100> mouse[0] > 1230 and 45 + 90 > mouse[1] > 45:
            pygame.draw.rect(screen, BLUE, (1230, 45, 100, 90)) #(x, y, width, height)
            if click[0] == 1:
                num += 1  
        else:
            pygame.draw.rect(screen, BRIGHT_BLUE, (1230, 45, 100, 90)) #(x, y, width, height)
        display_volume(1250, 60, volume)
        if 17 + 478 > mouse[0] > 17 and 300 + 50 > mouse[1] > 300:
            pygame.draw.rect(screen, BLUE, (17, 300, 478, 50)) #(x, y, width, height)
            if click[0] == 1:
                RECURSIVE_BACKTRACKER_1(x_change, y_change)
                
        else:
            pygame.draw.rect(screen, BRIGHT_BLUE, (17, 300, 478, 50)) #(x, y, width, height)


        if 535 + 270 > mouse[0] > 535 and 300 + 50 > mouse[1] > 300:
            pygame.draw.rect(screen, RED, (535, 300, 270, 50)) #(x, y, width, height)
            if click[0] == 1:
                PRIM_ALGORITHM(x_change, y_change, False)
        else:
            pygame.draw.rect(screen, BRIGHT_RED, (535, 300, 270, 50)) #(x, y, width, height)

        small_text1 = pygame.font.Font("freesansbold.ttf", 20)
        text_surf, text_rect = text_object("RECURSIVE BACKTRACKING ALGORITHM (DFS)", small_text1)
        text_rect.center = ((180+(150/2)), (300+(50/2)))
        screen.blit(text_surf, text_rect)
        

        small_text2 = pygame.font.Font("freesansbold.ttf", 20)
        text_surf, text_rect = text_object("PRIMS'S ALGORITHM", small_text2)
        text_rect.center = ((535+(270/2)), (300+(50/2)))
        screen.blit(text_surf, text_rect)
        

        pygame.display.update()
        # clock.tick(15)
game_intro()
# ##### pygame loop #######
# entered()
pygame.quit()
# quit()
        
                
# - Recursive backtracking algorithm
# - Hunt and kill algorithm
# - Eller's algorithm
# - Sidewinder algorithm
# - Prim's algorithm
# - Kruskal's algorithm
# - Depth-first search
# - Breadth-first search (not shown in video)
