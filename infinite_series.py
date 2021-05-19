from manim import *

class Series(Scene):
    def construct(self):
        
        text = Text(
            "Infinite Series"
        ).scale(0.85).to_edge(UP+LEFT)
        self.play(FadeIn(text),run_time=0.5)
        self.formulas()
        self.draw_circle()
        self.wait(2)

    def formulas(self):

        basel_sum = MathTex(
            "1 + {1 \\over 2^{2} } + {1 \\over 3^{2} } + {1 \\over 4^{2} } + \\cdots", 
            "=", "{\\pi^2 \\over 6}"
        )
        beta_sum = MathTex(
            "1-{1\\over 2}+{1\\over 4}-{1\\over 5}+{1\\over 7}-\\cdots",
            "=", "{\\pi \\over { 3 \\sqrt{3} } }")

        leibniz_sum = MathTex(
            "1-{1\\over 3}+{1\\over 5}-{1\\over 7}+{1\\over 9}-\\cdots",
            "=", "{\\pi \\over 4}")

        wallis_product = MathTex(
            "{2\\over 1} \\cdot {2\\over 3} \\cdot {4\\over 3} \\cdot {4\\over 5}" +
             "\\cdot {6\\over 5} \\cdot {6\\over 7} \\cdots",
             "=", "{\\pi \\over 2}")

        dirichlet_sum = MathTex(
            "1 - {1 \\over 3^{3} } + {1 \\over 5^{3} } - {1 \\over 7^{3} } + \\cdots", 
            "=", "{\\pi^3 \\over 32}"
        )

        formulas = VGroup(wallis_product, beta_sum, leibniz_sum, basel_sum, dirichlet_sum)
        formulas.scale(0.75)
        formulas.arrange(DOWN, buff = MED_LARGE_BUFF)
        for formula in formulas:
            formula_equals_x = formula.get_part_by_tex("=").get_center()[0]

        formulas.to_corner(UP+RIGHT)
        formulas.shift(2*LEFT)
        self.formulas = formulas
        for formula in formulas[:]:
            self.play(
                FadeIn(
                    formula, 
                    lag_ratio = 0.5, 
                    run_time = 3
                ),
            )
        self.wait()
        

    def draw_circle(self):
        semi_circle = Arc(angle = np.pi, radius = 2)
        radius = Line(ORIGIN, semi_circle.get_points()[0])
        radius.set_color(BLUE)
        semi_circle.set_color(YELLOW)

        VGroup(radius, semi_circle).to_edge(4*UP+4*LEFT)

        decimal = DecimalNumber(0).to_edge(7.5*UP+2*LEFT)
        def decimal_position_update_func(decimal):
            decimal.move_to(semi_circle.get_points()[-1])
            decimal.shift(0.3*radius.get_vector())

        one = Text("1")
        one.next_to(radius, UP)

        self.play(Create(radius), FadeIn(one))
        self.play(
            Rotate(radius, np.pi, about_point = radius.get_start()),
            Create(semi_circle),
            ChangeDecimalToValue(
                decimal, np.pi, 
                position_update_func = decimal_position_update_func
            ),
            MaintainPositionRelativeTo(one, radius),
            run_time = 3,
        )
        self.wait(2)

        self.circle_group = VGroup(semi_circle, radius, one, decimal)
