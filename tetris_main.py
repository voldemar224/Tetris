from field import Field
from block import Block
from figure import Figure


import const as const
import pygame
import sys


class Tetris:
    def __init__(self, menu_screen, game_over=False):
        self.menu_screen = menu_screen
        self.game_over = game_over
        timer = 0

        game_field_screen = pygame.Surface((const.GAME_FIELD_WIDTH_PXL, const.GAME_FIELD_HEIGHT_PXL))
        score_field_screen = pygame.Surface((const.SCORE_FIELD_WIDTH, const.GAME_FIELD_HEIGHT_PXL))

        field = Field(game_field_screen, menu_screen)
        field.create()

        figure = Figure(field)
        figure.create_figure()

        field.draw_field()
        figure.draw_figure()

        menu_screen.blit(game_field_screen, const.GAME_FIELD_COORD)

        pygame.draw.line(score_field_screen, const.WHITE, (0, 0), (0, const.SCORE_FIELD_HEIGHT), 1)

        menu_screen.blit(score_field_screen, const.SCORE_FIELD_COORD)

        pygame.display.update()

        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_LEFT:
                        if not figure.left_side_collision():

                            figure.move_left()

                            field.redraw_field_with_figure(figure)

                    elif i.key == pygame.K_RIGHT:
                        if not figure.right_side_collision():

                            figure.move_right()

                            field.redraw_field_with_figure(figure)

                    elif i.key == pygame.K_DOWN:

                        figure.move_down()

                        field.redraw_field_with_figure(figure)

                        timer = 0

                    elif i.key == pygame.K_UP:
                        if figure.height > 2:
                            if not figure.left_side_collision() and \
                                    not figure.right_side_collision() and \
                                    not figure.collision():

                                figure.rotate()

                                field.redraw_field_with_figure(figure)

            if timer >= const.PAUSE:
                if figure.collision():
                    figure.stop_figure()
                    del figure
                    figure = Figure(field)
                    figure.create_figure()

                    self.check_game_over(figure, field)
                    if self.game_over:
                        while self.game_over:
                            self.print_game_over(game_field_screen)
                            pygame.display.update()

                else:
                    figure.move()

                if field.check_filled_row():
                    print(field.score[0])

                    field.redraw_field_without_figure()

                    pygame.time.delay(300)

                else:
                    field.redraw_field_with_figure(figure)

                    timer = 0
            else:
                timer += const.PAUSE_ADD

            pygame.display.update()

    def print_game_over(self, game_field_screen):
        game_over_text_font = pygame.font.Font(None, 45)
        game_over_text = game_over_text_font.render('Game Over', True, const.WHITE)
        game_field_screen.blit(game_over_text, const.GAME_OVER_COORD)
        self.menu_screen.blit(game_field_screen, const.GAME_FIELD_COORD)

    def check_game_over(self, figure, field):
        for row in figure:
            for block in row:
                if field[block.y][block.x].state > 0:
                    self.game_over = True
