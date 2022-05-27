from manimce import *
from numpy import *

# Binet's Formula.

def F(n):
    a = (1 + sqrt(5)) / 2
    b = (a**n - (-a)**(-n)) / sqrt(5)
    return b

# Golden Ratio.

a = (1 + sqrt(5)) / 2


class ComplexFibonacci(MovingCameraScene):
    def construct(self):
        plane = ComplexPlane(
            x_range = (-5*FRAME_WIDTH, 5*FRAME_WIDTH),
            y_range = (-5*FRAME_HEIGHT, 5*FRAME_HEIGHT),
            background_line_style={
                "stroke_color": GREY_B,
                "stroke_opacity": 0.5,
                "stroke_width": 2
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
            "F_{n} = { { {\\varphi}^{n} - \\left( - {\\varphi} \\right)^{-{n} } } \\over 2 {\\varphi} - 1 }",
            **kw
        )
        formula.scale(1.35)
        formula.set_stroke(BLACK, 5, background = True)

        golden_ratio = MathTex(
            "{\\varphi} = { {1 + \\sqrt{5} } \\over 2 }",
            **kw
        )
        golden_ratio.next_to(formula.get_bottom(), DOWN)
        golden_ratio.set_stroke(BLACK, 5, background = True)
        formula.add(golden_ratio)
        rect = BackgroundRectangle(formula, fill_opacity = 0.75, buff = SMALL_BUFF)

        plane.add_coordinates(font_size = 30)
        self.add_foreground_mobjects(plane)
        self.wait(2)

        complex_fibonacci_curve = ParametricFunction(
            lambda t: [
                (a**t - a**(-t) * cos(pi*t)) / sqrt(5),
                (a**(-t) * sin(pi*t)) / sqrt(5),
                0
            ],
            t_range = [-FRAME_WIDTH, +FRAME_WIDTH],
            color = YELLOW
        )

        # Not Useful.

        # complex_fibonacci_curve = ParametricFunction(
        #     lambda t: complex_to_R3(F(complex(t, t))),
        #     t_range = (-FRAME_WIDTH, +FRAME_WIDTH),
        #     color = YELLOW
        # )

        self.play(
            Write(complex_fibonacci_curve),
            rate_func = smooth,
            run_time = 5,
        )
        self.wait(2)

        frame = self.camera.frame
        frame.save_state()

        self.play(
            frame.animate.scale(5),
            rate_func = smooth,
            run_time = 5
        )
        self.wait(2)

        # self.add_foreground_mobjects(formula)
        # self.play(
        #     Write(
        #         formula
        #     ),
        #     FadeIn(rect),
        #     rate_func = smooth,
        #     run_time = 3
        # )
        # self.wait()
