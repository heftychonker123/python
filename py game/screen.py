import pygame
from sys import exit

pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("Chonky")
clock=pygame.time.Clock()
game_scene=pygame.Surface((800,800))
game_scene.fill('White')
#Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(game_scene,(0,0))
    pygame.display.update()