from manim import *

# This file contains deprecated classes and functions.

class Checkmark(Tex):
    def __init__(self, **kwargs):
        super().__init__("\\checkmark")
        self.scale(2.5)
        self.set_color(GREEN)



class Exmark(Tex):
    def __init__(self, **kwargs):
        super().__init__("\\exmark")
        self.scale(2.5)
        self.set_color(RED)

        

class FadeInFromDown(FadeIn):
    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, UP, **kwargs)

        

class FadeOutAndShiftDown(FadeOut):
    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, DOWN, **kwargs)


        
class FadeInFromLarge(FadeIn):
    def __init__(self, mobject, scale_factor=2, **kwargs):
        super().__init__(mobject, scale=(1 / scale_factor), **kwargs)
