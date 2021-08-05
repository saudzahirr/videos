from manim import *

class GoldenRatio(Scene):
    def construct(self):
        circle = Circle(color = WHITE)
        pentagon = RegularPolygon(n = 5, color = GREY)
        point = pentagon.get_vertices()
        line_1 = Line(start = point[1], end = point[4], color = GREY)
        line_2 = Line(start = point[2], end = point[4], color = BLUE)
        line_3 = Line(start = point[1], end = point[3], color = BLUE)
        coord_label = VGroup(
            Tex(r"D").scale(0.5).next_to(point[1], 0.5*LEFT),
            Tex(r"A").scale(0.5).next_to(point[2], 0.5*LEFT + 0.5*DOWN),
            Tex(r"B").scale(0.5).next_to(point[3], 0.5*RIGHT + 0.5*DOWN),
            Tex(r"C").scale(0.5).next_to(point[4], 0.5*RIGHT)
        )
        circle.add(pentagon, line_1, line_2, line_3, coord_label)
        circle.scale(2)
        self.play(
            Write(circle),
            run_time = 2
        )
        self.wait()

        self.play(
            circle.animate.shift(4*LEFT),
            run_time = 2
        )
        self.wait()
