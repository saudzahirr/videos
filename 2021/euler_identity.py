from manimce import *

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
        fame.to_edge(2.5*UP+3*RIGHT)
        fame.scale(0.8)
        basel_sum = Tex(r"Basel Problem:"
            " $1 + {1 \\over 4 } + {1 \\over 9 } + {1 \\over 16 } + \\cdots = {\\pi^{2} \\over 6}.$",
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
            run_time=8,
            lag_ratio=0.1
        )
        self.wait()
        self.play(
            Indicate(euler_work),
            run_time = 1
        )
        self.wait(1)
        self.play(
            Write(symbol),
            run_time = 4
        )
        for mob in [symbol[1],symbol[5]]:
            self.play(
                Indicate(mob),
                run_time = 1
            )
        self.wait(2)

        self.play(
            FadeOut(fame),
            FadeOut(euler_work),
            FadeOut(symbol),
            FadeOut(euler_portrait),
            run_time=0.5
        )
        self.wait(0.25)

        euler_book = ImageMobject("book").scale(0.8) 
        euler_book.to_edge(UP+LEFT)
        history_formula = Tex(r"Around 1740 Euler turned his attention to the""\\\\",
            "exponential function instead of logarithms""\\\\",
            "and obtained the formula that is named after him.""\\\\", 
            "He obtained the formula by comparing the series""\\\\",
            "expansions of the exponential and trigonometric""\\\\",
            "expressions. It was published in 1748""\\\\",
            "in the"," `Introductio in analysin infinitorum'","."
        )
        history_formula.set_color_by_tex('Introductio in analysin infinitorum',BLUE)
        history_formula.to_edge(2*UP+RIGHT)
        history_formula.scale(0.75)
        euler_symbol = ImageMobject("127").next_to(history_formula,2*DOWN).scale(2)
        euler_eq_text = Tex(r"Extract from §127 of the""\\\\",
                            "Introductio in analysin infinitorum""\\\\",
                            "showing Euler's sine and cosine symbols.")
        euler_eq_text.scale(0.6).next_to(euler_symbol,DOWN)
        euler_eq_text.set_color_by_tex('Extract',YELLOW)
        euler_eq_text.set_color_by_tex('infinitorum',BLUE)
        euler_eq_text.set_color_by_tex('showing',YELLOW)

        self.play(
            Write(history_formula),
            FadeIn(euler_book),
            run_time = 4
        )
        self.wait(0.5)
        self.play(
            FadeIn(euler_symbol),
            FadeIn(euler_eq_text),
            run_time = 1
        )
        self.wait(4)

        self.play(
            FadeOut(history),
            FadeOut(euler_book),
            FadeOut(history_formula),
            FadeOut(euler_symbol),
            FadeOut(euler_eq_text),
            run_time = 0.25
        )
        self.wait(1.5)

        manuscript = Text("Euler's Manuscript").scale(0.9).to_edge(UP)
        euler_formula_image = ImageMobject("epii").next_to(manuscript,4*DOWN).scale(1.1)
        euler_formula_text = Tex(r"Extract from §124 of the""\\\\",
                            "Introductio in analysin infinitorum""\\\\",
                            "showing Euler's formula.")
        euler_formula_text.scale(0.65).next_to(euler_formula_image,DOWN)
        euler_formula_text.set_color_by_tex('Extract',YELLOW)
        euler_formula_text.set_color_by_tex('infinitorum',BLUE)
        euler_formula_text.set_color_by_tex('showing',YELLOW)

        manuscript_translation = Tex(r"``But in the preceding chapter we seen that""\\\\",
                                "$\\left ( {1 + {z \\over i}} \\right )^{i} = e^{z}$",
                                ", with $e$ denote the base of""\\\\",
                                "the hyperbolic logarithms; therefore for $z$ in one""\\\\",
                                "part I write $+v\\sqrt{-1}$, and for the",
                                " other part $-v\\sqrt{-1}$,""\\\\",
                                "and there becomes",
                                " $\\mathrm{cos}.v = { { e^{ +v \\sqrt{ -1 } } + e^{ -v \\sqrt{ -1 } } } \\over 2 }$"," ,",
                                " $\\mathrm{sin}.v = { { e^{ +v \\sqrt{ -1 } } - e^{ -v \\sqrt{ -1 } } } \\over { 2 \\sqrt{-1} } }$""\\\\",
                                "From which it is understood, how imaginary exponentials""\\\\",
                                "quantities may be reduced to the sine and""\\\\",
                                "cosine real arcs. Truly, there will be""\\\\",
                                "$e^{ +v \\sqrt{-1} } = \\mathrm{cos}.v + \\sqrt{-1} \\cdot \\mathrm{sin}.v$""\\\\",
                                " and"," $e^{ -v \\sqrt{-1} } = \\mathrm{cos}.v - \\sqrt{-1} \\cdot \\mathrm{sin}.v$","''"
        )
        manuscript_translation.to_edge(UP)
        manuscript_translation.scale(0.9)
        manuscript_translation.set_color_by_tex('$\\left ( {1 + {z \\over i}} \\right )^{i} = e^{z}$',BLUE)
        manuscript_translation.set_color_by_tex('$\\mathrm{cos}.v',BLUE)
        manuscript_translation.set_color_by_tex('$\\mathrm{sin}.v',BLUE)
        manuscript_translation.set_color_by_tex('$e^{ +v \\sqrt{-1} }',BLUE)
        manuscript_translation.set_color_by_tex('$e^{ -v \\sqrt{-1} }',BLUE)

        explain = Tex(r"This is the translation of previous manuscript!"
        ).scale(0.7).next_to(manuscript_translation,DOWN).set_color(YELLOW_C)

        self.play(
            Write(manuscript),
            FadeIn(euler_formula_image),
            FadeIn(euler_formula_text),
            run_time = 2
        )
        self.wait(3)

        self.play(
            ReplacementTransform(euler_formula_text,manuscript_translation),
            FadeOut(euler_formula_image),
            FadeOut(manuscript),
            run_time = 1
        )
        self.wait(2)
        self.play(
            Write(explain),
            run_time = 2
        )
        self.wait(1)
        self.play(
            Indicate(manuscript_translation)
        )
        self.wait(3)

        self.play(
            FadeOut(manuscript_translation),
            FadeOut(explain),
            run_time = 0.5
        )
        self.wait(1)
        
        euler_pi = ImageMobject('euler_pi').to_edge(UP)
        pi_text = Tex(r"Euler also used infinite series of arctan$(z)$""\\\\",
                    "and calculated an infinte series for $\\pi$."
        ).next_to(euler_pi,2*DOWN).set_color(BLUE)
        tan_inv = MathTex("{\\pi \\over 4} = \\mathrm{arctan} \\left({1 \\over 2}\\right) + \\mathrm{arctan} \\left({1 \\over 3}\\right)").next_to(pi_text,2*DOWN).scale(0.8)
        pi_formula = MathTex(
            "\\pi = 4 \\cdot \\left\\{\\begin{matrix} {1 \\over 1 \\cdot 2} - {1 \\over 3 \\cdot 2^{3}} + {1 \\over 5 \\cdot 2^{5}} \\\\ \\\\ {1 \\over 1 \\cdot 3} - {1 \\over 3 \\cdot 3^{3}} + {1 \\over 5 \\cdot 3^{5}} \\end{matrix}\\right. \\left.\\begin{matrix} - {1 \\over 7 \\cdot 2^{7}} + {1 \\over 9 \\cdot 2^{9}} - \\&\\mathrm{c.}  \\\\ \\\\  - {1 \\over 7 \\cdot 3^{7}} + {1 \\over 9 \\cdot 3^{9}} - \\&\\mathrm{c.} \\end{matrix}\\right\\} "
        ).next_to(tan_inv,2*DOWN).scale(0.8)
        
        pi_number = MathTex("\\pi=3.14159 \\ 26535 \\ 89793 \\ 23846 \\ 26433 \\ 83279 \\ 50288 \\ 41971 \\cdots").next_to(pi_formula,2*DOWN).scale(0.8)

        self.play(
            FadeIn(euler_pi),
            run_time = 2
        )
        self.play(
            Write(pi_text),
            run_time = 3
        )
        self.wait(1)

        self.play(
            FadeIn(tan_inv),
            FadeIn(pi_formula),
            run_time = 2
        )
        self.wait(1)

        self.play(
            Write(pi_number),
            Indicate(pi_formula),
            run_time = 2
        )
        self.wait(1)

        self.play(
            Indicate(pi_number),
            run_time = 2
        )
        self.wait(2)

        self.play(
            FadeOut(euler_pi),
            FadeOut(pi_text),
            FadeOut(pi_formula),
            FadeOut(pi_number),
            FadeOut(tan_inv),
            run_time=0.5
        )
        self.wait(1.5)

        taylor = Text("Taylor Series.").to_edge(UP)
        taylor_exp = Tex(r"Taylor Series"," of exponential,","\\\\"
                    "sine and cosine functions:"
        ).next_to(taylor,DOWN)
        taylor_exp.scale(0.8)
        taylor_exp.set_color_by_tex('Taylor Series',BLUE)

        exp = MathTex("e^{x} = \\sum_{n = 0}^{\\infty} { x^{n} \\over n! }","=",
                    "1 + x + {x^{2} \\over 2!} + \\cdots"
        )

        cos = MathTex("cos(x) = \\sum_{n = 0}^{\\infty} { (-1)^{n} \\over (2n)! }x^{2n}","=",
                    "1 - {x^{2} \\over 2} + {x^{4} \\over 4!} - \\cdots"
        ).next_to(exp,DOWN)

        sin = MathTex("sin(x) = \\sum_{n = 0}^{\\infty} { (-1)^{n} \\over (2n+1)! }x^{2n+1}","=",
                    "x - {x^{3} \\over 3!} + {x^{5} \\over 5!} - \\cdots"
        ).next_to(cos,DOWN)
        taylor_series = VGroup(exp,cos,sin)
        taylor_series.scale(0.5)
        taylor_series.next_to(taylor_exp,2*DOWN)
        box = SurroundingRectangle(taylor_series)
        self.play(
            Write(taylor),
            Write(taylor_exp),
            FadeIn(taylor_series),
            Create(box),
            run_time=1.5
        )
        self.wait(3)

        exponential = MathTex("e^{x} =",
                    "1 + x + {(x)^{2} \\over 2!} + {(x)^{3} \\over 3!} + {(x)^{4} \\over 4!} + \\cdots"
        )
        text = Tex(r"\\Derivation of Euler's Formula.").to_edge(UP)
        edit = Tex(r"Euler's Formula Derived!").to_edge(UP)

        self.play(
            FadeOut(box),
            FadeOut(taylor_exp),
            ReplacementTransform(taylor,text),
            ReplacementTransform(taylor_series,exponential),
            run_time = 1.5
        )
        self.wait(3)
        
        euler_eq1 = MathTex("e^{ix} =",
                    "1 + ix + {(ix)^{2} \\over 2!} + {(ix)^{3} \\over 3!} + {(ix)^{4} \\over 4!} + {(ix)^{5} \\over 5!} + \\cdots"
        )
        
        self.play(
            ReplacementTransform(exponential,euler_eq1)
        )
        self.wait(1)

        euler_eq2 = MathTex("i^{4n} = 1 \\\\ \\\\","e^{ix} =",
                    "1 + ix + {(ix)^{2} \\over 2!} + {(ix)^{3} \\over 3!} + {(ix)^{4} \\over 4!} + {(ix)^{5} \\over 5!} + \\cdots"
        )
        
        self.play(
            ReplacementTransform(euler_eq1,euler_eq2)
        )
        self.wait(1)

        euler_eq3 = MathTex("i^{4n+1} = i \\\\ \\\\","e^{ix} =",
                    "1 + ix + {(ix)^{2} \\over 2!} + {(ix)^{3} \\over 3!} + {(ix)^{4} \\over 4!} + {(ix)^{5} \\over 5!} + \\cdots"
        )
        
        self.play(
            ReplacementTransform(euler_eq2,euler_eq3)
        )
        self.wait(1)

        euler_eq4 = MathTex("i^{4n+2} = -1 \\\\ \\\\","e^{ix} =",
                    "1 + ix - {(x)^{2} \\over 2!} + {(ix)^{3} \\over 3!} + {(ix)^{4} \\over 4!} + {(ix)^{5} \\over 5!} + \\cdots"
        )
        
        self.play(
            ReplacementTransform(euler_eq3,euler_eq4)
        )
        self.wait(1)

        euler_eq5 = MathTex("i^{4n+3} = -i \\\\ \\\\","e^{ix} =",
                    "1 + ix - {(x)^{2} \\over 2!} - i{(x)^{3} \\over 3!} + {(ix)^{4} \\over 4!} + {(ix)^{5} \\over 5!} + \\cdots"
        )
        
        self.play(
            ReplacementTransform(euler_eq4,euler_eq5)
        )
        self.wait(1)

        euler_eq6 = MathTex("i^{4n+4} = 1 \\\\ \\\\","e^{ix} =",
                    "1 + ix - {(x)^{2} \\over 2!} - i{(x)^{3} \\over 3!} + {(x)^{4} \\over 4!} + {(ix)^{5} \\over 5!} + \\cdots"
        )
        
        self.play(
            ReplacementTransform(euler_eq5,euler_eq6)
        )
        self.wait(1)

        euler_eq7 = MathTex("i^{4n+5} = i \\\\ \\\\","e^{ix} =",
                    "1 + ix - {(x)^{2} \\over 2!} - i{(x)^{3} \\over 3!} + {(x)^{4} \\over 4!} + i{(x)^{5} \\over 5!} + \\cdots"
        )
        
        self.play(
            ReplacementTransform(euler_eq6,euler_eq7)
        )
        self.wait(1)

        euler_eq8 = MathTex("e^{ix} =",
                    "\\left( 1 - {(x)^{2} \\over 2!} + {(x)^{4} \\over 4!} + \\cdots \\right)"," + ",
                    "\\left( ix - i{(x)^{3} \\over 3!} + i{(x)^{5} \\over 5!} + \\cdots \\right)"
        )
        
        self.play(
            ReplacementTransform(euler_eq7,euler_eq8)
        )
        self.wait(1.5)

        euler_eq9 = MathTex("e^{ix} =",
                    "\\left( 1 - {(x)^{2} \\over 2!} + {(x)^{4} \\over 4!} + \\cdots \\right) + i \\left( x - {(x)^{3} \\over 3!} + {(x)^{5} \\over 5!} + \\cdots \\right)"
        )
        
        self.play(
            ReplacementTransform(euler_eq8,euler_eq9)
        )
        self.wait(2)

        euler_eq0 = MathTex("e^{ix} =",
                    "\\mathrm{cos}(x) + i \\cdot \\mathrm{sin}(x)"
        )
        
        self.play(
            ReplacementTransform(text,edit),
            ReplacementTransform(euler_eq9,euler_eq0)
        )
        self.wait(2)
        
        box_ = SurroundingRectangle(euler_eq0,color=TEAL_D)

        for obj in [euler_eq0[0]]:
            self.play(
                Flash(obj,color=YELLOW,flash_radius=1)
        )
        self.play(
            Create(box_),
            run_time=1
        )
        self.wait(1)
        self.play(
            FadeOut(box_)
        )

        self.wait(2)

        self.play(
            FadeOut(euler_eq0),
            FadeOut(edit),
            run_time = 0.25
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

        
        
        
        
