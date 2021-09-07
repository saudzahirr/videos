from manim import *
from numpy import *
from itertools import *
from constants import *

def logo(self):
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
    thumbnail = VGroup(circle_2, title_2)
    thumbnail.scale(1.1)
    thumbnail.to_edge(0.5*DOWN+0.5*RIGHT)
    self.play(Transform(logo, thumbnail), FadeOut(logo_name), run_time = 1)


def logo_transformation(self):
    #LOGO
    circle_1 = Circle(radius = 1, fill_color = CHARCOAL, stroke_color = WHITE, stroke_width = 5, fill_opacity = 0.3)
    title_1 = MathTex("\\alpha")
    title_1.scale(4.5)
    logo = VGroup(circle_1, title_1)
    logo.scale(1.5)
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

def new_logo(self):
    colors = cycle(
        [BLUE_1, BLUE_2, BLUE_3, BLUE_4, BLUE_5,
        BLUE_6, BLUE_7, BLUE_8, BLUE_9, BLUE_10,
        BLUE_11, BLUE_12, BLUE_13, BLUE_14, BLUE_15,
        BLUE_16, BLUE_17, BLUE_18, BLUE_19, BLUE_20]
    )
    radius = []
    for i in arange(0, 2, 0.1):
        radius.append(i)
    circles = Group()
    for rad in radius:
        circles.add(Circle(rad, stroke_width = 20))
    
    circles[0].set_fill(BLUE_1)

    for circle, color in zip(circles, colors):
        circle.set_color(color)
    self.play(
        GrowFromCenter(circles)
    )
    self.wait()

def thumbnail(self):
    circle = Circle(radius=0.25,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2)
    title = MathTex("\\alpha")
    thumbnail = VGroup(circle, title)
    thumbnail.scale(1.2)
    thumbnail.to_edge(0.5*DOWN+0.5*RIGHT)
    self.add(thumbnail)


class Test(Scene):
    def construct(self):
        #logo_transformation(self)
        new_logo(self)
