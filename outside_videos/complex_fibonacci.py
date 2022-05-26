from manimce import *


def F(n):
    a = (1 + sqrt(5)) / 2
    b = (a**n - (-a)**(-n)) / sqrt(5)
    return b


class ComplexFibonacci(Scene):
    def construct(self):
        plane = ComplexPlane(
            x_range = (-FRAME_WIDTH*2, FRAME_WIDTH*2),
            y_range = (-FRAME_HEIGHT*2, FRAME_HEIGHT*2),
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
        self.add(rect)

        plane.add_coordinates(font_size = 30)
        self.add_foreground_mobjects(plane, formula)
        self.wait(2)

        complex_fibonacci_curve = plane.plot(
            lambda t: complex_to_R3(F(complex(t, t))),
            t_range = (-5, +5)
        )

        # complex_fibonacci_curve = ParametricFunction(
        #     lambda t: complex_to_R3(F(complex(t, t))),
        #     t_range = (-5, +5)
        # )

        self.play(
            Write(complex_fibonacci_curve),
            rate_func = smooth,
            run_time = 3,
        )
        self.wait(2)
