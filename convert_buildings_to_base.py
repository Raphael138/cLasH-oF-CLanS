import pygame
from pygame.locals import *

pygame.init()

# visualizer settings
WIDTH = 920
HEIGHT = 920
green1 = (130, 255, 148)
green2 = (88, 210, 105)
font = pygame.font.Font('freesansbold.ttf', 15)

#note: c.o.c. base is 44x44 grid
SQAURE_SIZE = 20

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("cLash of cLans")

### CLASSES ###

class Building:

    def __init__(self, name, id, type, size, x, y):
        self.name = name
        self.id = id
        self.type = type
        self.size = size
        self.x = x
        self.y = y

    def getColor(self):

        if(self.type == "defense"):
            return (212, 35, 35)
        if(self.type == "resource"):
            return (38, 85, 12)
        if(self.type == "wall"):
            return (212, 145, 35)
        if(self.type == "townhall"):
            return (255, 147, 0)
        else:
            print("Z&R ERROR: type is not valid")
            return (0, 0, 0)
     
    def drawBuilding(self):
        #draw main part
        color = self.getColor()
        pygame.draw.rect(screen, (0, 0, 0), Rect(self.x*SQAURE_SIZE+20, self.y*SQAURE_SIZE+20, self.size * SQAURE_SIZE, self.size * SQAURE_SIZE))
        pygame.draw.rect(screen, color, Rect(self.x*SQAURE_SIZE+25, self.y*SQAURE_SIZE+25, self.size * SQAURE_SIZE - 10, self.size * SQAURE_SIZE - 10))

        #add text
        text = font.render(self.name, True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (self.x*SQAURE_SIZE+20 + self.size*SQAURE_SIZE//2, self.y*SQAURE_SIZE+20+ self.size*SQAURE_SIZE//2)
        screen.blit(text, textRect)
        


### FUNCTIONS ###
def mainDraw():
    screen.fill(green1)
    for i in range(44):
        for j in range(44):

            if (i + j) % 2 == 1:
                pygame.draw.rect(screen, green2, Rect(i*SQAURE_SIZE+20, j*SQAURE_SIZE+20, SQAURE_SIZE, SQAURE_SIZE))

            for b in buildings:
                b.drawBuilding()


buildings = list()

#sample buildings
buildings.append(Building("townhall", "", "townhall", 4, 20, 20))

### GAME LOOP ###
running = True
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        ### Quit program ###
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
        exit()

    mainDraw()
    pygame.display.update()

pygame.quit()