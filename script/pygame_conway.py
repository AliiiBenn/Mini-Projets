import time
import pygame as py


class Game:
    def __init__(self):
        self.screen = py.display.set_mode((800, 800))
        self.grid = [[0] * 40 for _ in range(40)]
        self.size = 800 // 40
        self.playing = False
        self.clock = py.time.Clock()
        
    def dead_state(self, width, height):
        return [[0 for x in range(width)] for y in range(height)]
        
    def draw_grid(self):
        for y, line in enumerate(self.grid):
            for x, cell in enumerate(line):
                if not cell == 1:
                    py.draw.rect(self.screen, (169, 169, 169), (x * self.size, y * self.size, self.size, self.size), 1)
                else:
                    py.draw.rect(self.screen, (0, 0, 0), (x * self.size, y * self.size, self.size, self.size))
                
    def next_board_state(self, grid):
        new_state = self.dead_state(len(self.grid), len(self.grid))
        for y in range(0, len(self.grid)):
            for x in range(0, len(self.grid)):
                
                cell_value = grid[y][x]


                neighbors = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
                n_count = 0
                for n in neighbors:

                    if not n[0] < 0 and not n[1] < 0 and not n[0] > len(self.grid) - 1 and not n[1] > len(self.grid) - 1:
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
    
    def add_cell(self, y, x):
        self.grid[y][x] = 1
        
    def remove_cell(self, y, x):
        self.grid[y][x] = 0
        
    def handle_input(self):
        mouse_pos = py.mouse.get_pos()
        # print(mouse_pos[0] // self.size, mouse_pos[1] // self.size)
        
        if not self.playing:
            if py.mouse.get_pressed()[0]:
                self.add_cell(mouse_pos[1] // self.size, mouse_pos[0] // self.size)
            if py.mouse.get_pressed()[2]:
                self.remove_cell(mouse_pos[1] // self.size, mouse_pos[0] // self.size)
        if py.mouse.get_pressed()[1]:
            self.playing = not self.playing
        
                
    def run(self):
        running = True
        
        while running:
            self.clock.tick(30)
            self.screen.fill((255, 255, 255))
            self.handle_input()
            self.draw_grid()
            
            
            if self.playing:
                self.grid = self.next_board_state(self.grid)
                py.time.delay(500)
            
            py.display.flip()
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
            
        py.quit()

if __name__ == '__main__':
    py.init()
    game = Game()
    game.run()