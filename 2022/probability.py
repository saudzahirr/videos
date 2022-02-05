from manimce import *
from custom.drawings import Heart, Diamond, Spade, Clover



class DeckOfCards(RoundedRectangle):
    def __init__(self, height, width, fill_color, fill_opacity, **kwargs):
        self.height = height,
        self.width = width,
        self.fill_color = fill_color,
        self.fill_opacity = fill_opacity
        RoundedRectangle.__init__(self, height, width, fill_color, fill_opacity, **kwargs)
        self.set_height(height),
        self.set_width(width),
        self.set_fill(fill_color, fill_opacity)



class Test(Scene):
    def construct(self):
        self.play(
            Create(
                DeckOfCards(height = 5, width = 3, fill_color = WHITE, fill_opacity = 1.2)
            )
        )
        self.wait()
