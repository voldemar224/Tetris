PAUSE = 2000
PAUSE_ADD = 1

BLOCK_WIDTH_PXL = 25

MENU_WIDTH = 600
MENU_HEIGHT = 900


FIELD_WIDTH = 16
FIELD_HEIGHT = 36
BLOCK_WIDTH = 25

GAME_FIELD_WIDTH_PXL = FIELD_WIDTH * BLOCK_WIDTH
GAME_FIELD_HEIGHT_PXL = FIELD_HEIGHT * BLOCK_WIDTH
GAME_FIELD_COORD = (0, 0)

SCORE_FIELD_WIDTH = 200
SCORE_FIELD_HEIGHT = GAME_FIELD_HEIGHT_PXL
SCORE_FIELD_COORD = (GAME_FIELD_WIDTH_PXL, 0)

MAIN_SCREEN_WIDTH = FIELD_WIDTH * BLOCK_WIDTH + SCORE_FIELD_WIDTH
MAIN_SCREEN_HEIGHT = FIELD_HEIGHT * BLOCK_WIDTH

SCORE_TEXT_X = SCORE_FIELD_WIDTH / 2 - 45
SCORE_TEXT_Y = FIELD_HEIGHT * BLOCK_WIDTH * 2 / 2.7
SCORE_X = SCORE_FIELD_WIDTH / 2 - 30
SCORE_Y = SCORE_TEXT_Y + 55

GAME_OVER_COORD = (FIELD_WIDTH * BLOCK_WIDTH / 2 - 80, FIELD_HEIGHT * BLOCK_WIDTH / 3 + 40)
# RETRY_X = GAME_OVER_X
# RETRY_Y = GAME_OVER_Y + 50

# EXIT_X = RETRY_X
# EXIT_Y = RETRY_Y + 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (3, 65, 174)
RED = (255, 50, 19)
GREEN = (114, 203, 59)
ORANGE = (255, 151, 28)
YELLOW = (255, 213, 0)
CYAN = (32, 254, 255)
VIOLET = (163, 73, 164)

SCORE = [0]
SCORE_ADD = [0, 40, 100, 300, 1200]

I_figure = [[0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

L_figure = [[0, 0, 2],
            [2, 2, 2],
            [0, 0, 0]]

J_figure = [[3, 0, 0],
            [3, 3, 3],
            [0, 0, 0]]

T_figure = [[4, 4, 4],
            [0, 4, 0],
            [0, 0, 0]]
S_figure = [[0, 5, 5],
            [5, 5, 0],
            [0, 0, 0]]
Z_figure = [[6, 6, 0],
            [0, 6, 6],
            [0, 0, 0]]
O_figure = [[7, 7],
            [7, 7]]
