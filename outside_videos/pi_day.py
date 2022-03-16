from manimce import *
import random



class PiDay(Scene):
    def construct(self):
        title = Tex("March 14 (3/14), Pi Day.")
        title.scale(1.5)
        title.to_edge(UP)
        self.add(title)

        pi = Tex("$\\pi$", color = GREY_BROWN)
        pi.scale(10)
        pi.to_edge(5 * LEFT)

        value = Tex("$3.141592653 \\cdots$").scale(2.5)
        value.to_edge(2 * DOWN)

        party_hat = SVGMobject(get_svg("party_hat.svg"), stroke_width = 1, stroke_color = GREY_BROWN, fill_color = PINK).scale(0.75)
        party_hat.next_to(pi.get_left(), UR, buff = 0.0)
        party_hat.shift(UP)
        party_hat.rotate(15 * DEGREES)

        for a in [0, 2, 3, 4, 5]:
            party_hat[a].set_color(YELLOW)
        
        for a, color in zip(range(8, 16), cycle([BLUE, GREEN, PURPLE])):
            party_hat[a].set_color(color)

        self.play(
            Write(pi),
            DrawBorderThenFill(party_hat),
            Write(value),
            rate_func = smooth,
            run_time = 2,
        )
        self.draw_arc()
        self.wait(2)

        pi.add(party_hat)

        self.play(
            FadeOut(value, shift = DOWN),
            FadeOut(title, shift = UP)
        )
        self.clear()
        self.add(pi)
        self.play(pi.animate.to_edge(5 * RIGHT), run_time = 1, rate_func = smooth)
        self.write_formulas()
        self.wait()
        self.play(
            FadeOut(pi)
        )
        self.wait()
        
        euler = ImageMobject("EulersManuscript\EulersPortrait")
        euler.to_edge(13.5 * LEFT)

        self.play(
            FadeIn(euler)
        )
        self.clear()

        euler = ImageMobject("EulersManuscript\EulersPortrait")
        euler.to_edge(13.5 * LEFT)
        
        self.add(euler)
        self.wait()

        history = Tex(r"Leonhard Euler used infinite series" "\\\\",
                    "of arctan$(z)$ and calculated an" "\\\\",
                    "infinite series for $\\pi$."
        )
        history.shift(3 * LEFT)
        history.shift(2 * UP)

        series = MathTex("{\\pi \\over 4} = \\mathrm{arctan} \\left({1 \\over 2}\\right) + \\mathrm{arctan} \\left({1 \\over 3}\\right)").next_to(history, 2 * DOWN).scale(0.8)
        pi_formula = MathTex(
            "\\pi = 4 \\cdot \\left\\{\\begin{matrix} {1 \\over 1 \\cdot 2} - {1 \\over 3 \\cdot 2^{3}} + {1 \\over 5 \\cdot 2^{5}} \\\\ \\\\ {1 \\over 1 \\cdot 3} - {1 \\over 3 \\cdot 3^{3}} + {1 \\over 5 \\cdot 3^{5}} \\end{matrix}\\right. \\left.\\begin{matrix} - {1 \\over 7 \\cdot 2^{7}} + {1 \\over 9 \\cdot 2^{9}} - \\&\\mathrm{c.}  \\\\ \\\\  - {1 \\over 7 \\cdot 3^{7}} + {1 \\over 9 \\cdot 3^{9}} - \\&\\mathrm{c.} \\end{matrix}\\right\\} "
        ).next_to(series, 2 * DOWN).scale(0.75)

        self.play(
            Write(history),
            run_time = 4,
            rate_func = smooth
        )
        self.wait(1)
        self.play(
            FadeIn(series, shift = UP),
            rate_func = smooth
        )
        self.wait(1)
        self.play(
            FadeIn(pi_formula, shift = UP),
            rate_func = smooth
        )
        self.wait(2)

        self.play(
            FadeOut(
                VGroup(history, series, pi_formula),
                shift = DOWN
            ),
            rate_func = smooth
        )
        self.wait()



    def write_formulas(self):

        basel_sum = MathTex(
            "1 + {1 \\over 2^{2} } + {1 \\over 3^{2} } + {1 \\over 4^{2} } + \\cdots = {\\pi^2 \\over 6}"
        )
        beta_sum = MathTex(
            "1-{1\\over 2}+{1\\over 4}-{1\\over 5}+{1\\over 7}-\\cdots = {\\pi \\over { 3 \\sqrt{3} } }")

        leibniz_sum = MathTex(
            "1-{1\\over 3}+{1\\over 5}-{1\\over 7}+{1\\over 9}-\\cdots = {\\pi \\over 4}")

        wallis_product = MathTex(
            "{2\\over 1} \\cdot {2\\over 3} \\cdot {4\\over 3} \\cdot {4\\over 5} \\cdot {6\\over 5} \\cdot {6\\over 7} \\cdots = {\\pi \\over 2}")

        dirichlet_sum = MathTex(
            "1 - {1 \\over 3^{3} } + {1 \\over 5^{3} } - {1 \\over 7^{3} } + \\cdots = {\\pi^3 \\over 32}"
        )

        formulas = VGroup(wallis_product, beta_sum, leibniz_sum, basel_sum, dirichlet_sum)
        formulas.scale(0.80)
        formulas.arrange(DOWN, buff = MED_LARGE_BUFF)
        for formula in formulas:
            formula_equals_x = formula.get_part_by_tex("=").get_center()[0]

        formulas.to_edge(3 * LEFT)
        self.formulas = formulas
        for formula in formulas[:]:
            self.play(
                FadeIn(
                    formula,
                    shift = UP,
                    lag_ratio = 0.25, 
                    run_time = 3
                ),
            )
        self.add_foreground_mobjects(formulas)
        self.wait()
        


    def draw_arc(self):
        circle = Arc(angle = np.pi, radius = 2)
        radius = Line(ORIGIN, circle.get_points()[0])
        radius.set_color(BLUE)
        circle.set_color(YELLOW)

        VGroup(radius, circle).to_edge(4*UP+4*RIGHT)

        decimal = DecimalNumber(0).next_to(radius.get_boundary_point(RIGHT), RIGHT, buff = MED_LARGE_BUFF)
        def decimal_position_update_func(decimal):
            decimal.move_to(circle.get_points()[-1])
            decimal.shift(0.3*radius.get_vector())

        one = Tex("1")
        one.next_to(radius, UP)

        self.play(Create(radius), FadeIn(one))
        self.play(
            Rotate(radius, np.pi, about_point = radius.get_start()),
            Create(circle),
            ChangeDecimalToValue(
                decimal, np.pi, 
                position_update_func = decimal_position_update_func
            ),
            MaintainPositionRelativeTo(one, radius),
            run_time = 3,
        )
        self.wait(2)

        self.circle_group = VGroup(circle, radius, one, decimal)
