from manim import *

# Not useful.

class Checkmark(Tex):
    def __init__(self, **kwargs):
        super().__init__("\\checkmark")
        self.scale(2.5)
        self.set_color(GREEN)



class Exmark(Tex):
    def __init__(
        self,
        tex_template = tex_temp,
        **kwargs
    ):
        super().__init__("\\exmark")
        self.scale(2.5)
        self.set_color(RED)
