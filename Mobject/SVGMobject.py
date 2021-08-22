from manim import *

class ChessBoard(SVGMobject):
    file_name = "chess.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(3)


class Heart(SVGMobject):
    file_name = "heart.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_color(RED)
        self.scale(0.5)


class Diamond(SVGMobject):
    file_name = "diamond.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_color(RED)
        self.scale(0.5)


class Spade(SVGMobject):
    file_name = "spade.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_color(WHITE)
        self.scale(0.5)


class Clover(SVGMobject):
    file_name = "clover.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_color(WHITE)
        self.scale(0.5)
