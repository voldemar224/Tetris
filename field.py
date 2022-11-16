from block import Block
import pygame
import const as const


class Field:
    def __init__(self, screen, menu_screen, block_width=const.BLOCK_WIDTH, width=const.FIELD_WIDTH, height=const.FIELD_HEIGHT,
                 field_list=None, score=None):
        self.screen = screen
        self.menu_screen = menu_screen
        self.block_width = block_width
        self.width = width
        self.height = height
        if field_list is None:
            field_list = []
        self.field_list = field_list
        if score is None:
            score = [0]
        self.score = score

    def __getitem__(self, item):
        if 0 <= item <= self.height + 1:
            # for row in self.field_list:
            #     for block in row:
            #         print(block, end=" ")
            #     print()
            return self.field_list[item]

    def create(self):
        for row in range(0, self.height):
            self.field_list.append([])
            for col in range(0, self.width):
                self.field_list[row].append(Block(col, row))

        bottom = []
        for col in range(0, self.width):
            bottom.append(Block(col, self.height, state=5))

        self.field_list.append(bottom)

    def draw_field(self):
        for row in self.field_list:
            for block in row:
                block.draw_block(self.screen)

    def redraw_field_with_figure(self, figure):
        self.screen.fill(const.BLACK)

        self.draw_field()

        figure.draw_figure()

        self.menu_screen.blit(self.screen, const.GAME_FIELD_COORD)

        pygame.display.update()

    def redraw_field_without_figure(self):
        self.screen.fill(const.BLACK)

        self.draw_field()

        self.menu_screen.blit(self.screen, const.GAME_FIELD_COORD)

        pygame.display.update()

    def check_filled_row(self):
        filled_row = False
        counter = 0
        for row in self.field_list:
            if row[0].y != self.height:
                blocks_in_a_row = 0
                for block in row:
                    if block.state == 0:
                        break
                    else:
                        blocks_in_a_row += 1
                if blocks_in_a_row == self.width:
                    filled_row = True
                    counter += 1
                    for row_ in range(row[0].y, 0, -1):
                        for col in range(0, self.width):
                            self[row_][col].state = self[row_ - 1][col].state
                            # print(f"{self[row_][col]} = {self[row_ - 1][col]}")

                    for block in self[0]:
                        block.state = 0
        self.score[0] += const.SCORE_ADD[counter]
        return filled_row
