from manim import *
from numpy import *
from itertools import *
from constants import *



def logo(self):
    # Logo
    circle_1 = Circle(radius = 1, fill_color = CHARCOAL, stroke_color = WHITE, stroke_width = 5, fill_opacity = 0.3)
    title_1 = MathTex("\\alpha")
    title_1.scale(4.5)
    logo = VGroup(circle_1, title_1)
    logo.scale(2.0)
    logo.shift(UP)
    logo_name = Text("aljabrak")
    logo_name.scale(1.6)
    logo_name.next_to(logo, 2 * DOWN)
    self.play(
        LaggedStartMap(Write, logo),
        Write(logo_name),
        rate_func = smooth,
        run_time = 5
    )
    self.wait(2)
    self.clear()

    
def aljabrak(self):
    #LOGO
    circle_1 = Circle(radius=1,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2)
    title_1 = MathTex("\\alpha")
    title_1.scale(4.5)
    logo = VGroup(circle_1, title_1)
    logo.scale(1.5)
    logo_name = Text("aljabrak")
    logo_name.scale(1.5)
    logo_name.next_to(logo, 1.5*DOWN)
    self.play(
        LaggedStartMap(Write, logo),
        Write(logo_name),
        run_time = 5
    )
    self.wait(2)

    circle_2 = Circle(radius=0.25,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2)
    title_2 = MathTex("\\alpha")
    watermark = VGroup(circle_2, title_2)
    watermark.scale(1.1)
    watermark.to_edge(0.5*DOWN+0.5*RIGHT)
    self.play(Transform(logo, watermark), FadeOut(logo_name), run_time = 1)


def logo_transformation(self):
    #LOGO
    circle_1 = Circle(radius = 1, fill_color = CHARCOAL, stroke_color = WHITE, stroke_width = 5, fill_opacity = 0.3)
    title_1 = MathTex("\\alpha")
    title_1.scale(4.5)
    logo = VGroup(circle_1, title_1)
    logo.scale(1.7)
    logo.shift(0.5 * UP)
    logo_name = Text("aljabrak")
    logo_name.scale(1.6)
    logo_name.next_to(logo, 1.5*DOWN)
    self.play(
        LaggedStartMap(Write, logo),
        Write(logo_name),
        run_time = 5
    )
    self.wait(1.25)
    self.play(
        FadeOut(logo_name)
    )
    self.play(
        Succession(
            logo.animate.scale(25),
            FadeOut(logo, run_time = 1),
            run_time = 2,
            rate_func = smooth
        )
    )

    
def watermark(self):
    circle = Circle(radius=0.25,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2)
    title = MathTex("\\alpha")
    logo = VGroup(circle, title)
    logo.scale(1.2)
    logo.to_edge(0.5*DOWN+0.5*RIGHT)
    self.add(logo)

    
    
    
    
    
    
    
    
