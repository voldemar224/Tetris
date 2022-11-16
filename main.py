from tetris_main import Tetris
import pygame
import const


menu_screen = pygame.display.set_mode((const.MENU_WIDTH, const.MENU_HEIGHT))

pygame.font.init()


tetris = Tetris(menu_screen)


pygame.display.update()