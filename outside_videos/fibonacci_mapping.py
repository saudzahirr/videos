from manimce import *


def F(x):
    a = (1 + sqrt(5)) / 2
    b = (a**x - (-a)**x) / sqrt(5)
    return b


class FibonacciMapping(Scene):
    def construct(self):
        plane = ComplexPlane(
            x_range = (-FRAME_WIDTH, FRAME_WIDTH), y_range = (-FRAME_HEIGHT, FRAME_HEIGHT),
            background_line_style={
                "stroke_color": GREY_B,
                "stroke_opacity": 0.5,
                "stroke_width": 1
            },
            faded_line_ratio = 4
        )
        plane.scale(2)

        grid = plane.copy()
        grid.set_stroke(GREY_B, 2)
        grid.prepare_for_nonlinear_transform()
        self.add(grid)

        plane.add_coordinates(font_size = 20)
        self.add_foreground_mobject(plane)

        self.play(
            grid.animate.apply_complex_function(lambda z: F(z)),
            rate_func = smooth,
            run_time = 6,
        )
        self.wait()
