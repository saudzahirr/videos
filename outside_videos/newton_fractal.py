from manimce import *


colors = ["#3B528B", "#5DC963"]


class ParameterSpaceOfNewtonsFractal(Scene):
    def construct(self):
        plane = self.plane = ComplexPlane(
            x_range = (-FRAME_WIDTH, FRAME_WIDTH), y_range = (-FRAME_WIDTH, FRAME_WIDTH),
            background_line_style={
                "stroke_color": GREY_B,
                "stroke_opacity": 0.5,
                "stroke_width": 1
            },
            faded_line_ratio = 4
        )
        plane.scale(2)
        # plane.add_coordinates(font_size = 20)

        grid = plane.copy()
        grid.set_stroke(WHITE, 2)
        grid.prepare_for_nonlinear_transform()

        root_dots = VGroup(*(
            Dot(plane.n2p(z), color=color)
            for color, z in zip(colors, [-1, 1])
        ))
        root_dots.set_stroke(BLACK, 2)

        line = Line(plane.n2p(complex((1-1j)/sqrt(2))), plane.n2p(complex((1+1j)/sqrt(2))))
        line.set_color(YELLOW)
        line.apply_complex_function(lambda z: z**2)
        shape = VGroup(
            line,
            line.copy().flip(UP)
        )
        shape.set_fill(YELLOW, 0.5)

        title = Tex(
            "Parameter Space"
        )
        title.scale(1.5)
        title.set_stroke(BLACK, 5, background = True)
        title.to_corner(UP)

        complex_map = Tex(
            "$\\mathds{C}: z \\rightarrow z^{2}$"
        )
        complex_map.scale(1.25)
        complex_map.to_corner(UL)
        complex_map.set_stroke(BLACK, 5, background = True)
        rect = BackgroundRectangle(complex_map, fill_opacity = 0.5, buff = SMALL_BUFF)

        self.add_foreground_mobjects(plane, root_dots)

        parameter_space = ImageMobject(get_image("ParameterSpace.png"))
        self.add(parameter_space)
        self.wait(2)

        self.play(
            grid.animate.apply_complex_function(lambda z: z**2),
            rate_func = smooth,
            run_time = 6,
        )

        self.add_foreground_mobject(complex_map)
        self.play(
            Write(complex_map),
            FadeIn(rect),
            rate_func = smooth,
            run_time = 2
        )
        self.wait(2)

        self.play(
            DrawBorderThenFill(shape),
            rate_func = smooth,
        )
        self.wait(2)
