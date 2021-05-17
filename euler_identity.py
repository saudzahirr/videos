from manim import *

class EulerFormula(Scene):
    def construct(self):
        euler_formula = Text("Euler's Formula.").to_edge(LEFT+UP)
        eq = MathTex("e^{", "j", "\\theta}", "= \\mathrm{cos}(", "\\theta", ") + ", "j", "\\cdot \\mathrm{sin}(", "\\theta", ")").next_to(euler_formula,DOWN)
        eq.set_color_by_tex('j',YELLOW)
        eq.set_color_by_tex('\\theta',BLUE)
        feynman_words = Tex("Richard P. Feynman:""\\\\",
                            " ``Our jewel'' ""\\\\","and""\\\\",
                            " ``the most remarkable""\\\\",
                            "formula in mathematics.'' "
        ).next_to(eq,4*DOWN)
        feynman_words.set_color_by_tex('Our jewel',YELLOW)
        feynman_words.set_color_by_tex('the most remarkable',YELLOW)
        feynman_words.set_color_by_tex('formula in mathematics.',YELLOW)
        feynman_words.set_color_by_tex('Richard P. Feynman',BLUE)

        self.play(
            Write(euler_formula),
            run_time=3
        )
        self.wait(1)
        self.play(
            Write(eq),
            run_time=4,
            lag_ratio=0.5
        )
        self.wait(2)
        self.play(
            FadeIn(feynman_words),
            run_time=1
        )
        self.wait(1)
        self.draw_circle()
        self.wait(2)
        self.play(
            FadeOut(euler_formula),
            FadeOut(eq),
            FadeOut(feynman_words),
            run_time=0.7
        )
        self.clear()
        
        history = Text("History").to_edge(UP)
        euler_portrait = ImageMobject("euler").scale(0.5)
        euler_portrait.to_edge(UP+LEFT)   
    
        fame = Tex(r"The 18th-century Swiss mathematician""\\\\",
                    "Leonhard Euler"," (1707–1783) is among ""\\\\",
                    "the most prolific and successful ""\\\\",
                    "mathematicians in the history of the field.")
        fame.set_color_by_tex('Leonhard Euler',BLUE)
        fame.to_edge(2.5*UP+RIGHT)
        fame.scale(0.8)
        basel_sum = Tex(r"Basel Problem:"
            " $1 + {1 \\over 4 } + {1 \\over 9 } + {1 \\over 16 } + \\cdots = {\\pi^2 \\over 6}.$",
            " (1735)"
        ).next_to(fame,DOWN)
        euler_identity = Tex("$e^{i\\pi} + 1 = 0. $"," (1740)").next_to(basel_sum,DOWN)
        beam_equation = MathTex("EI \\frac{ d^{4} w }{ dx^{4} } = q(x), \\",
                            "F = { \\pi^{2} EI \\over (KL)^{2}}."
        ).next_to(euler_identity,DOWN)
        euler_work = VGroup(basel_sum,euler_identity,beam_equation)
        euler_work.scale(0.8)
        symbol = Tex(r"He also popularized"," `$\\pi$' ","for the ratio of""\\\\",
                    "a circle's circumference to its""\\\\",
                    " diameter and"," `$\\Sigma$' ","for summation."
        ).scale(0.8)
        symbol.next_to(euler_work,DOWN)
        symbol.set_color_by_tex('\\pi',RED_C)
        symbol.set_color_by_tex('\\Sigma',TEAL_C)
        self.play(
            FadeIn(history),
            run_time=1
        )
        self.play(
            FadeIn(euler_portrait),
            Write(fame),
            run_time=5
        )
        self.wait(1)
        self.play(
            Write(euler_work),
            run_time=6,
            lag_ratio=0.5
        )
        self.wait()
        self.play(
            Indicate(euler_work)
        )
        self.wait(1)
        self.play(
            Write(symbol),
            run_time=4
        )
        for mob in [symbol[1],symbol[5]]:
            self.play(Indicate(mob))
        self.wait(2)

        self.play(
            FadeOut(fame),
            FadeOut(euler_work),
            FadeOut(symbol),
            run_time=0.5
        )
        euler_book = ImageMobject("book").scale(0.8) 
        self.play(
            ReplacementTransform(euler_portrait,euler_book),
            run_time=0.5
        )
        self.wait(2)



             
    def draw_circle(self):
        circle = Arc(angle = 2*np.pi, radius = 2)
        radius = Line(ORIGIN, circle.get_points()[0])
        radius.set_color(BLUE)
        circle.set_color(YELLOW)

        VGroup(radius, circle).to_edge(4*UP+4*RIGHT)

        decimal = DecimalNumber(0).to_edge(7.5*UP+2*RIGHT)
        def decimal_position_update_func(decimal):
            decimal.move_to(circle.get_points()[-1])
            decimal.shift(0.3*radius.get_vector())

        one = Text("1")
        one.next_to(radius, UP)

        self.play(Create(radius), FadeIn(one))
        self.play(
            Rotate(radius, 2*np.pi, about_point = radius.get_start()),
            Create(circle),
            ChangeDecimalToValue(
                decimal, 2*np.pi, 
                position_update_func = decimal_position_update_func
            ),
            MaintainPositionRelativeTo(one, radius),
            run_time = 3,
        )
        self.wait(2)

        self.circle_group = VGroup(circle, radius, one, decimal)
