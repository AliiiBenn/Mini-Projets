from hashlib import new
from operator import ne
import random
import time


def dead_state(width, height):
    return [[0 for x in range(width)] for y in range(height)]

def random_state(width, height):
    return [[random.randint(0, 1) for x in range(width)] for y in range(height)]

def render(grid):
    for row in grid:
        print(''.join(['#' if x else '.' for x in row]))
    print()
    
# a_dead_state = dead_state(20, 30)
# render(a_dead_state)

# print('================================')

# a_random_state = random_state(20, 30)
# render(a_random_state)

def next_board_state(grid):
    new_state = dead_state(3, 3)
    for y in range(0, 3):
        for x in range(0, 3):
            cell_value = grid[y][x]
            

            neighbors = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
            n_count = 0
            for n in neighbors:
                
                if not n[0] < 0 and not n[1] < 0 and not n[0] > 2 and not n[1] > 2:
                    # print('positions :', n, grid[n[1]][n[0]])
                    n_count += grid[n[1]][n[0]]
            
        
            # print((y, x), "neighbors :", n_count, '| cell_value :', cell_value)
            
            # ? Mettre dans une liste le nombre de voisins de chaque cellule puis dans une boucle de cette nouvelle liste faire les conditions du jeu
                
            if cell_value == 1:
                if n_count < 2 or n_count > 3:
                    new_state[y][x] = 0
                elif n_count == 2 or n_count == 3:
                    new_state[y][x] = 1
            elif cell_value == 0:
                if n_count == 3:
                    new_state[y][x] = 1
                    
                
                    
    return new_state
            
        
        
if __name__ == "__main__":
    # # TEST 1: dead cells with no live neighbors
    # # should stay dead.
    # init_state1 = [
    #     [0,0,0],
    #     [0,0,0],
    #     [0,0,0]
    # ]
    # expected_next_state1 = [
    #     [0,0,0],
    #     [0,0,0],
    #     [0,0,0]
    # ]
    # actual_next_state1 = next_board_state(init_state1)

    # if expected_next_state1 == actual_next_state1:
    #     print("PASSED 1")
    # else:
    #     print("FAILED 1!")
    #     print("Expected:")
    #     print(expected_next_state1)
    #     print("Actual:")
    #     print(actual_next_state1)

    # # TEST 2: dead cells with exactly 3 neighbors
    # # should come alive.
    # init_state2 = [
    #     [0,0,1],
    #     [0,1,1],
    #     [0,0,0]
    # ]
    # expected_next_state2 = [
    #     [0,1,1],
    #     [0,1,1],
    #     [0,0,0]
    # ]
    # actual_next_state2 = next_board_state(init_state2)

    # if expected_next_state2 == actual_next_state2:
    #     print("PASSED 2")
    # else:
    #     print("FAILED 2!")
    #     print("Expected:")
    #     print(expected_next_state2)
    #     print("Actual:")
    #     print(actual_next_state2)
    
    grid = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    
    while True:
        grid = next_board_state(grid)
        # render(next_board_state(grid))
        render(grid)
        time.sleep(3)