import random
import pygame as py
from dataclasses import dataclass

"""
TODO : Voir pour un système de déplacement sur la carte avec aussi si possible un système de zoom
TODO : Voir pour mettre des templates déjà fait pour ne pas avoir 
TODO : Documentation
"""

        
@dataclass
class Cell:
    x : int
    y : int
    value : int
    
    @property
    def state(self) -> bool:
        return bool(self.value)
    
    def neighbors(self):
        neighbors = [(self.x-1, self.y-1), (self.x, self.y-1), (self.x+1, self.y-1), (self.x-1, self.y), (self.x+1, self.y), (self.x-1, self.y+1), (self.x, self.y+1), (self.x+1, self.y+1)]
        return neighbors
    
    def neighbors_count(self, grid):
        neighbors = self.neighbors()
        n_count = 0
        for n in neighbors:
            if not n[0] < 0 and not n[1] < 0 and not n[0] > len(grid) - 1 and not n[1] > len(grid) - 1:
                n_count += grid[n[1]][n[0]].value
        return n_count
        

class Grid:
    def __init__(self, screen : py.Surface):
        self.screen = screen
        self.width = self.height = self.cell_per_line = 40
        self.cell_size = self.screen.get_height() // self.cell_per_line
        self.grid : list[list[Cell]] = self.dead_state(self.width, self.height)
        
    def __len__(self):
        return len(self.grid)
    
    def __getitem__(self, key):
        return self.grid[key]
        
    def dead_state(self, width, height):
        return [[Cell(x, y, 0) for x in range(width)] for y in range(height)]
    
    def random_state(self, width, height):
        return [[random.randint(0, 1) for x in range(width)] for y in range(height)]
    
    def draw(self):
        for y, line in enumerate(self.grid):
            for x, cell in enumerate(line):
                cell_pos_x = x * self.cell_size
                cell_pos_y = y * self.cell_size
                if cell.state == 1:
                    py.draw.rect(self.screen, (0, 0, 0), (cell_pos_x + 1, cell_pos_y + 1, self.cell_size - 2, self.cell_size - 2))
                    continue
                py.draw.rect(self.screen, (169, 169, 169), (cell_pos_x, cell_pos_y, self.cell_size, self.cell_size), 1)
                
    def add_cell(self, y, x):
        self.grid[y][x] = Cell(x, y, 1)
        
    def remove_cell(self, y, x):
        self.grid[y][x] = Cell(x, y, 0)
    
    

class Game:
    def __init__(self):
        # on créer la fenetre
        self.screen_width = self.screen_height = 800
        self.screen_size = (self.screen_width, self.screen_height)
        self.screen = py.display.set_mode((self.screen_size))
        
        self.grid = Grid(self.screen)
        
        self.playing = False
        self.NEXT_STEP_DELAY = 250
        self.FPS = 60
        

    
    def next_board_state(self):
        new_state = Grid(self.screen)
        for y, line in enumerate(self.grid):
            for x, cell in enumerate(line):
                n_count = cell.neighbors_count(self.grid)


                if cell.value == 1:
                    if n_count < 2 or n_count > 3:
                        new_state.remove_cell(y, x)
                    elif n_count == 2 or n_count == 3:
                        new_state.add_cell(y, x)
                elif cell.value == 0:
                    if n_count == 3:
                        new_state.add_cell(y, x)



        return new_state
    

    def handle_input(self):
        mouse_pos = py.mouse.get_pos()
        
        if not self.playing:
            if py.mouse.get_pressed()[0]:
                self.grid.add_cell(mouse_pos[1] // self.grid.cell_size, mouse_pos[0] // self.grid.cell_size)
            if py.mouse.get_pressed()[2]:
                self.grid.remove_cell(mouse_pos[1] // self.grid.cell_size, mouse_pos[0] // self.grid.cell_size)
        if py.mouse.get_pressed()[1]:
            self.playing = not self.playing
        
    # boucle principale du jeu      
    def run(self):
        running = True
        # horloge du jeu
        self.clock = py.time.Clock()
        while running:
            self.clock.tick(self.FPS)
            self.screen.fill((255, 255, 255))
            
            
            self.handle_input()
            self.grid.draw()
            
            
            if self.playing:
                self.grid = self.next_board_state()
                
                py.time.delay(self.NEXT_STEP_DELAY)
            
            py.display.flip()
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
            
        py.quit()

if __name__ == '__main__':
    py.init()
    game = Game()
    game.run()