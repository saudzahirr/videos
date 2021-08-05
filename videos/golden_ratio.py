from manim import *

class GoldenRatio(Scene):
    def construct(self):
        pentagon = RegularPolygon(n = 5, color = WHITE)
        pentagon.scale(2)
        point = pentagon.get_vertices()
        line = DashedLine(start=point[0], end=point[2])
        self.play(
            line.animate,
            pentagon.animate
        )
        self.wait()
