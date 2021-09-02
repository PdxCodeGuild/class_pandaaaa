import pygame
import random
import sys

class Snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)

    def face_location(self):
        return self.positions[0]    

    def turn(self, point):    
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else: 
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*GRIDSIZE)) % SCREEN_WIDTH), (cur[1] + (y*GRIDSIZE)))
        if len(self.positions) > 2 and new in self.postions[2:]:
            self.postions.pop()

    def reboot():
        pass

    def draw(self, surface):
        pass

    def handle_keys(self):
        pass

class Pellet(object):
    def __init__(self):
        pass

    def generate_location(self):
        pass

    def draw(self, surface):
        pass

def drawGrid(surface):    
    for y in range(0, int(GRID_HEIGHT)):
    for x in range(0), int(GRID_WIDTH)):


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.covert()
    drawGrid(surface)

    snake = Snake()
    pellet = Pellet()

    score = 0
    while (True):
        clock.tick(10)
        

main()    