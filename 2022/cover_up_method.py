from manimce import *


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
