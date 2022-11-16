from block import Block


import const as const
import random
import copy


class Figure:
    figure_states_list = [const.I_figure, const.L_figure, const.J_figure, const.T_figure,
                          const.S_figure, const.Z_figure, const.O_figure]

    # figure_states_list = [const.I_figure]

    def __init__(self, field, figure=None, figure_clone=None):
        self.field = field
        self.figure_states = random.choice(Figure.figure_states_list)
        if figure is None:
            figure = []
        self.figure = figure
        self.height = len(self.figure_states)
        self.width = len(self.figure_states[0])
        if figure_clone is None:
            figure_clone = []
        self.figure_clone = figure_clone

    def __getitem__(self, item):
        return self.figure[item]

    def create_figure(self):
        x = int(self.field.width/2) - 2
        y = 0
        for row in range(0, len(self.figure_states)):
            self.figure.append([])
            for col in range(0, len(self.figure_states[row])):
                self.figure[row].append(Block(x, y, state=self.figure_states[row][col]))
                x += 1
            x = int(self.field.width / 2) - 2
            y += 1

    def figure_clone_move(self):
        for row in self.figure_clone:
            for block in row:
                block.y += 1

    def draw_figure(self):
        self.figure_clone = copy.deepcopy(self.figure)

        for row in self.figure_clone:
            for block in row:
                if block.state > 0:
                    block.state = 8
        while not self.figure_clone_collision():
            self.figure_clone_move()

        for row in self.figure_clone:
            for block in row:
                block.draw_block(self.field.screen)

        for row in self.figure:
            for block in row:
                block.draw_block(self.field.screen)

    def move(self):
        for row in self.figure:
            for block in row:
                block.y += 1

    def collision(self):
        bottom_blocks = []
        for row in range(0, self.height):
            for col in range(self.width - 1, -1, -1):
                if self[col][row].state > 0:
                    bottom_blocks.append(self[col][row])
                    break
        for block in bottom_blocks:
            if self.field[block.y + 1][block.x].state > 0:
                return True
        return False

    def figure_clone_collision(self):
        bottom_blocks = []
        for row in range(0, self.height):
            for col in range(self.width - 1, -1, -1):
                if self.figure_clone[col][row].state > 0:
                    bottom_blocks.append(self.figure_clone[col][row])
                    break
        for block in bottom_blocks:
            if self.field[block.y + 1][block.x].state > 0:
                return True
        return False

    def stop_figure(self):
        for row in self.figure:
            for block in row:
                if block.state > 0:
                    self.field[block.y][block.x].state = block.state

    def left_side_collision(self):
        last_left_blocks = []
        for row in self.figure:
            for block in row:
                if block.state > 0:
                    last_left_blocks.append(block)
                    break
        for block in last_left_blocks:
            if block.x == 0 or self.field[block.y][block.x - 1].state > 0:
                return True
        return False

    def right_side_collision(self):
        last_right_blocks = []
        for row in self.figure:
            for block in list(reversed(row)):
                if block.state > 0:
                    last_right_blocks.append(block)
                    break
        for block in last_right_blocks:
            if block.x == self.field.width - 1 or self.field[block.y][block.x + 1].state > 0:
                return True
        return False

    def move_left(self):
        for row in self.figure:
            for block in row:
                block.x -= 1

    def move_right(self):
        for row in self.figure:
            for block in row:
                block.x += 1

    def move_down(self):
        while not self.collision():
            self.move()

    def rotate(self):
        if self.height == 4:
            self[1][3].state, self[3][2].state, self[2][0].state, self[0][1].state = \
                self[0][1].state, self[1][3].state, self[3][2].state, self[2][0].state
            self[2][3].state, self[3][1].state, self[1][0].state, self[0][2].state = \
                self[0][2].state, self[2][3].state, self[3][1].state, self[1][0].state
            self[1][2].state, self[2][2].state, self[2][1].state, self[1][1].state = \
                self[1][1].state, self[1][2].state, self[2][2].state, self[2][1].state
        else:
            self[0][2].state, self[2][2].state, self[2][0].state, self[0][0].state = \
                self[0][0].state, self[0][2].state, self[2][2].state, self[2][0].state
            self[1][2].state, self[2][1].state, self[1][0].state, self[0][1].state = \
                self[0][1].state, self[1][2].state, self[2][1].state, self[1][0].state







