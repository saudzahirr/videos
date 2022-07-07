from manimce import *


use_opengl_renderer = True


class ComplexMapping(Scene):
    def construct(self):
        plane = ComplexPlane(
            x_range = [-FRAME_WIDTH, FRAME_WIDTH],
            y_range = [-FRAME_HEIGHT, FRAME_HEIGHT],
            background_line_style = {
                "stroke_color": GREY_B,
                "stroke_opacity": 1,
                "stroke_width": 1,
            },
            faded_line_ratio = 2,
        )
        plane.axes.set_stroke(opacity = 3/2)
        plane.add_coordinates()

        self.add(plane)
        self.wait()

        square = ComplexPlane(
            x_range = [-1/2, 1/2],
            y_range = [-1/2, 1/2],
            background_line_style = {
                "stroke_color": YELLOW,
                "stroke_opacity": 2,
                "stroke_width": 2,
            },
            faded_line_ratio = 6,
        )
        square.add(
            BackgroundRectangle(square, color = YELLOW, fill_opacity = 0.25),
            SurroundingRectangle(square, color = YELLOW, stroke_width = 1.5, buff = 0.0)
        )

        self.play(
            Create(square)
        )
        self.wait()

        square.prepare_for_nonlinear_transform()
        self.play(
            square.animate.apply_complex_function(lambda z: 1/z),
            rate_func = smooth,
            run_time = 2
        )
        self.wait()

