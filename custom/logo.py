from manimlib import *


class Logo(VMobject):
    CONFIG = {
        "radius" : 1,
        "fill_color" : GREY_E,
        "stroke_color" : WHITE,
        "stroke_width" : 15,
        "fill_opacity" : 0.95,
        "logo" : "\\alpha",
        # "text" : "aljabrak"
    }
    def __init__(self, **kwargs):
        VMobject.__init__(self, **kwargs)
        self.add_logo()
        
    
    def add_logo(self):
        self.circle = Circle(
            radius = self.radius,
            fill_color = self.fill_color,
            stroke_color = self.stroke_color,
            stroke_width = self.stroke_width,
            fill_opacity = self.fill_opacity,
        )
        self.symbol = Tex(self.logo)
        self.symbol.scale(4.5)
        self.circle.add(self.symbol)
        self.add(self.circle)
        

        
        
        
class Test(Scene):
    def construct(self):
        logo = Logo().scale(3.5)
        self.play(
            GrowFromCenter(logo),
            rate_func = smooth,
            run_time = 3
        )
        self.wait(2)
