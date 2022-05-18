from manimce import *



# Helpers.

def get_figure(filename, person_name, height = 3, label_direction = DOWN):

    image = ImageMobject(get_portrait(filename))
    image.set_height(height)
    rect = SurroundingRectangle(image, buff = 0)
    rect.set_stroke(WHITE, 2)
    name = Tex(person_name, font_size = 36)
    name.next_to(image, label_direction)
    
    return Group(rect, image, name)



# Scenes.

class RationalFractions(Scene):
    def construct(self):
        title = Tex(
            r"Rational Fractions"
        )
        title.scale(1.5)
        title.set_stroke(BLACK, 5, background = True)
        title.to_edge(UP)

        self.add(title)

        definition = MathTex("f(x) = { p(x) \\over q(x)}")
        definition.set_stroke(BLACK, 5, background = True)
        definition.shift(UP)

        explanation = Tex(
            "$p(x)$ and $q(x)$ are polynomials." "\\\\",
            "(", "not transcendental functions!" "\\\\",
            "$\mathrm{sin}(x), \\ \mathrm{log}(x), \\ \mathrm{e}^{x}$",
            " \\ etc.)"
        )
        
        explanation[2].set_color(RED)
        explanation[3].set_color(BLUE)
        explanation.next_to(definition, DOWN, buff = 0.5)

        examples = VGroup(
            MathTex("9 \\over {(x + 3)(x + 7)}"),
            MathTex("{2x \\over x^{2} - 1} "),
            MathTex("{3x + 1 \\over x^{2} + 2x - 3} "),
            MathTex("{\sqrt{x+2} \over x^{2} - 3}"),
            MathTex("{x^2-3 \\over x+1}"),
            MathTex("\\mathrm{cos}(x) \\over \\mathrm{sin} \\left( x \\over 2 \\right)"),
            MathTex("\\mathrm{log}(x) \\over {x^2 + 1}"),
            MathTex("{x^{2} - 1} \\over {x^{2} - 5}")
        )

        coords = [
            [0, 0, 0],
            [-4, 2, 0],
            [4, 0, 0],
            [0, 2, 0],
            [3, -2, 0],
            [-2, -2, 0],
            [-3, 0, 0],
            [-5, -2, 0]
        ]

        for example, coord in zip(examples, coords):
            example.move_to(coord)

        
        cross = VGroup(
            Cross(examples[3]),
            Cross(examples[5]),
            Cross(examples[6])
        )

        cross_label = Tex("Irrational Fractions!")
        cross_label.scale(1.35)
        cross_label.next_to(examples[5], UP, buff = 0.5)
        cross_label.set_stroke(BLACK, 5, background = True)

        proper_fractions = Tex(
            "Proper Rational Fractions!" "\\\\",
            "deg $p(x) <$ deg $q(x)$."
        )
        proper_fractions.scale(1.35)
        proper_fractions[1].scale(0.85, about_edge=UP)
        proper_fractions.next_to(examples[7], RIGHT, buff = 0.0)
        proper_fractions.set_stroke(BLACK, 5, background = True)
        
        self.play(
            Write(definition),
            run_time = 2,
            rate_func = smooth
        )
        self.wait()

        self.play(
            Write(explanation[0]),
            Write(explanation[1:], lag_ratio = 0.4),
            run_time = 3,
            rate_func = smooth
        )
        self.wait(3)

        self.play(
            FadeOut(definition, shift = DOWN),
            FadeOut(explanation, shift = DOWN),
            run_time = 1,
            rate_func = smooth
        )

        self.play(
            LaggedStart(
                *[
                    GrowFromPoint(example, coord)
                    for example, coord in zip(examples, coords)
                ]
            )
        )
        self.wait(3)

        self.play(
            Create(cross),
            run_time = 2,
            rate_func = smooth
        )
        self.wait()

        self.play(
            Write(cross_label),
            run_time = 2,
            rate_func = smooth
        )
        self.wait()

        self.play(
            FadeOut(
                VGroup(
                    examples[3],
                    examples[5],
                    examples[6],
                    cross, cross_label
                )
            ),
            run_time = 2,
            rate_func = smooth
        )
        self.wait()

        
        VGroup(
            examples[3],
            examples[5],
            examples[6]
        ).shift(5 * FRAME_WIDTH)

        self.play(
            Write(proper_fractions[0]),
            examples[3:].animate.set_color(GREY_B)
        )
        self.wait()

        self.play(
            Write(proper_fractions[1]),
            lag_ratio = 0.5,
            rate_func = smooth
        )
        self.wait()

        # self.play(
        #     FadeOut(examples[3:]),
        #     examples[1].animate.next_to(examples[0], LEFT, buff = 1),
        #     rate_func = smooth
        # )
        self.wait(2)
        

        
class PartialFractions(Scene):
    def construct(self):
        partial_fraction = Tex(
            "${ { lx^{2} + mx + n } \over { (x-a)(x-b)(x-c) } } =$",
            "$ \\ { A \over (x - a) } $", "$ \\ +$",
            "$ \\ { B \over (x - b) } $","$ \\ +$",
            "$ \\ { C \over (x - c) }$"
        )
        partial_fraction.scale(1.25)
        partial_fraction.set_stroke(BLACK, 5, background = True)
        partial_fraction.to_edge(2 * UP)

        constants = VGroup(
            MathTex("A = { { la^{2} + ma + n } \over { (a-b)(a-c) } }"),
            MathTex("B = { { lb^{2} + mb + n } \over { (b-a)(b-c) } }"),
            MathTex("C = { { lc^{2} + mc + n } \over { (c-a)(c-b) } }")
        )
        constants.set_stroke(BLACK, 5, background = True)
        constants.arrange(DOWN)
        constants.next_to(partial_fraction, DOWN)

        self.play(
            Write(partial_fraction),
            run_time = 3,
            rate_func = smooth
        )
        self.wait()
        partial_fraction.save_state()

        for a, constant in zip([1, 3, 5], constants):
            self.play(
                partial_fraction[1:].animate.set_opacity(0.5)
            )
            self.play(
                partial_fraction[a].animate.set_opacity(1),
                FadeIn(constant, shift = DOWN),
                run_time = 1.5,
                rate_func = smooth
            )
            self.wait()

        self.wait()
        
        
        
class History(Scene):
    def construct(self):
        year = Tex("1702")
        year.scale(1.5)
        year.to_edge(UL)

        # bernoulli = get_figure("Johann_Bernoulli.jpg", "Johann Bernoulli")
        # bernoulli.to_edge(LEFT)
        # leibniz = get_figure("Gottfried_Wilhelm_Leibniz.jpg", "Gottfried Wilhelm Leibniz")
        # leibniz.to_edge(RIGHT)

        kw = {
            "x" : YELLOW,
            "p" : BLUE_B,
            "q" : BLUE_C
        }

        formulas = VGroup(
            MathTex("\\int \\frac{p(x)}{q(x)} dx", kw),
            MathTex("\\int {dx \\over x^{2} + 1}"),
            MathTex("= {1 \\over 2 \\sqrt{-1}} \\int {\\left ( {1 \\over x - \\sqrt{-1}} - {1 \\over x + \\sqrt{-1}}  \\right )} dx")
            MathTex("= {1 \\over 2 \\sqrt{-1}} \\cdot \\mathrm{log} \\left ( {x - \\sqrt{-1}} \\over {x + \\sqrt{-1}} \\right )")
        )
        formulas.scale(0.75)
        formulas.arrange(DOWN)

        # self.play(
        #     FadeIn(bernoulli, leibniz)
        # )
        self.play(Write(year))
        self.wait()

        self.play(
            FadeIn(formulas, shift = DOWN),
            # lag_ratio = 0.5,
            run_time = 2,
            rate_func = smooth
        )
        self.wait()
