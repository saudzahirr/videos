import numpy as np


# Frame and Pixel shape.
ASPECT_RATIO = 16.0 / 9.0
FRAME_HEIGHT = 8.0
FRAME_WIDTH = ASPECT_RATIO * FRAME_HEIGHT
FRAME_Y_RADIUS = FRAME_HEIGHT / 2
FRAME_X_RADIUS = FRAME_WIDTH / 2

DEFAULT_PIXEL_HEIGHT = 1080
DEFAULT_PIXEL_WIDTH = 1920
DEFAULT_FRAME_RATE = 30

# Buffs.
SMALL_BUFF = 0.1
MED_SMALL_BUFF = 0.25
MED_LARGE_BUFF = 0.5
LARGE_BUFF = 1

# Coordinates.
ORIGIN = np.array((0., 0., 0.))
UP = np.array((0., 1., 0.))
DOWN = np.array((0., -1., 0.))
RIGHT = np.array((1., 0., 0.))
LEFT = np.array((-1., 0., 0.))
IN = np.array((0., 0., -1.))
OUT = np.array((0., 0., 1.))
X_AXIS = np.array((1., 0., 0.))
Y_AXIS = np.array((0., 1., 0.))
Z_AXIS = np.array((0., 0., 1.))

# Useful abbreviations for diagonals
UL = UP + LEFT
UR = UP + RIGHT
DL = DOWN + LEFT
DR = DOWN + RIGHT

TOP = FRAME_Y_RADIUS * UP
BOTTOM = FRAME_Y_RADIUS * DOWN
LEFT_SIDE = FRAME_X_RADIUS * LEFT
RIGHT_SIDE = FRAME_X_RADIUS * RIGHT

# Texts
START_X = 30
START_Y = 20
NORMAL = "NORMAL"
ITALIC = "ITALIC"
OBLIQUE = "OBLIQUE"
BOLD = "BOLD"

# Extra Colors.
CHAR_TREE = "#7FFF00"
LIME = "#00FF00"
LAWN_GREEN = "#7CFC00"
AQUA_MARINE = "#7FFFD4"
DARK_PINK = "#FF084A"
TAUPE = "#CCAC93"
LAVENDER = "#EB96EB"
MAGENTA = "#E05194"
CHARCOAL = "#808080"
OLIVE_GREEN = "#AFB83B"
DARK_BLUE = "#288BA8"
APPLE = "#7CC53E"
BRILLIANT_AZURE = "#29A3FB"
INCHWORM = "#A2DE67"
MELON = "#FEAAAB"
RUBY = "#DD105E"
PERSIAN_PINK = "#EC83BF"
INDEPENDENCE = "#46466E"

COBALT = "#0047AB"
RED_F = "#D02028"

