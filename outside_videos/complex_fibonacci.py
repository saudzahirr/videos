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

        kw = {"tex_to_color_map": {
            "F": BLUE_C,
            "{n}": BLUE_B,
            "{\\varphi}": YELLOW}
        }

        formula = MathTex(
            "F_{n} = { { {\\varphi}^{n} - \\left( - {\\varphi} \\right)^{n} } \\over 2 {\\varphi} - 1 }",
            **kw
        )
        formula.scale(1.25)
        formula.to_corner(UL)
        formula.set_stroke(BLACK, 5, background = True)

        golden_ratio = MathTex(
            "{\\varphi} = { {1 + \\sqrt{5} } \\over 2 }",
            **kw
        )
        golden_ratio.next_to(formula.get_bottom(), DOWN)
        golden_ratio.set_stroke(BLACK, 5, background = True)
        formula.add(golden_ratio)
        
        rect = BackgroundRectangle(formula, fill_opacity = 0.5, buff = SMALL_BUFF)

        grid = plane.copy()
        grid.set_stroke(GREY_B, 2)
        grid.prepare_for_nonlinear_transform()
        self.add(grid, rect)

        plane.add_coordinates(font_size = 30)
        self.add_foreground_mobjects(plane, formula)
        self.wait(2)

        self.play(
            grid.animate.apply_complex_function(lambda z: F(z)),
            rate_func = smooth,
            run_time = 10,
        )
        self.wait(2)
