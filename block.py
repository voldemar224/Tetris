import const as const
import pygame


class Block:
    def __init__(self, x, y, width=const.BLOCK_WIDTH, state=0):
        self.x = x
        self.y = y
        self.width = width
        self.state = state

    def __str__(self):
        return f"(   {self.x}, {self.y}, {self.state}   )"

    def get_color(self):
        if self.state == 8:
            return const.WHITE
        elif self.state == 1:
            return const.CYAN
        elif self.state == 2:
            return const.ORANGE
        elif self.state == 3:
            return const.BLUE
        elif self.state == 4:
            return const.VIOLET
        elif self.state == 5:
            return const.GREEN
        elif self.state == 6:
            return const.RED
        else:
            return const.YELLOW

    def draw_block(self, screen):
        if 1 <= self.state <= 8:
            pygame.draw.rect(screen, self.get_color(),
                             (self.x * self.width, self.y * self.width, self.width - 1, self.width - 1), 1, 5)
