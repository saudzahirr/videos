from manimce import *


class Pixels(Scene):
    def construct(self):
        pixels = VGroup()
        for i in range(0,400):
            pixels.add(Square(side_length = 0.35).set_stroke(WHITE, width=0.35))
        
        pixels.arrange_in_grid(20, 20, buff = 0)
        self.add(pixels)
        self.wait()
