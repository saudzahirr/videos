from manimce import *


class GoldenRatio(Scene):
    def construct(self):
        logo(self)

        circle = Circle(color = WHITE)
        pentagon = RegularPolygon(n = 5, color = GREY)
        point = pentagon.get_vertices()
        line_1 = Line(start = point[1], end = point[4], color = GREY)
        line_2 = Line(start = point[2], end = point[4], color = BLUE)
        line_3 = Line(start = point[1], end = point[3], color = BLUE)
        coord_label = VGroup(
            Tex(r"D").scale(0.5).next_to(point[1], 0.5*LEFT),
            Tex(r"A").scale(0.5).next_to(point[2], 0.5*LEFT + 0.5*DOWN),
            Tex(r"B").scale(0.5).next_to(point[3], 0.5*RIGHT + 0.5*DOWN),
            Tex(r"C").scale(0.5).next_to(point[4], 0.5*RIGHT)
        )
        circle.add(pentagon, line_1, line_2, line_3, coord_label)
        circle.scale(2)
        self.play(
            Write(circle),
            run_time = 3
        )
        self.wait()

        self.play(
            circle.animate.shift(4*LEFT),
            run_time = 2
        )
        self.wait()

        ptolemy_theorem = Tex(
            r"\large{Ptolemy's Theorem}" "\\\\",
            r"\tiny{..............}" "\\\\",
            r"\small{\emph{If a quadrilateral is}}" "\\\\",
            r"\emph{inscribable in a circle then}" "\\\\",
            r"\emph{the product of the lengths}" "\\\\",
            r"\emph{of its diagonals is equal to the}" "\\\\",
            r"\emph{sum of the products of the}" "\\\\",
            r"\emph{lengths of the pairs of opposite sides.}" "\\\\",
            r"\tiny{..........}" "\\\\",
            r"\large{$\overline{\text{AC}}\cdot\overline{\text{BD}} = \overline{\text{AB}}\cdot\overline{\text{CD}} + \overline{\text{BC}}\cdot\overline{\text{AD}}$}"
        )
        ptolemy_theorem.to_edge(RIGHT)
        ptolemy_theorem[0].set_color(BLUE)
        ptolemy_theorem[1].set_color(BLACK)
        ptolemy_theorem[8].set_color(BLACK)

        self.play(
            FadeIn(ptolemy_theorem),
            run_time = 2
        )
        self.wait(3)

        self.play(
            FadeOut(ptolemy_theorem[0:8]),
            ptolemy_theorem[9].animate.scale(0.75).shift(5*UP),
            run_time = 1.5
        )
        self.wait(0.5)

        quote = Tex(r"Since the pentagon has equal side lengths!")
        quote.scale(0.75)
        quote.set_color(YELLOW)
        quote.next_to(ptolemy_theorem[9], DOWN)
        self.play(
            Write(quote),
            run_time = 3.5
        )
        self.wait()

        self.play(
            FadeOut(quote),
        )
        self.wait()

        proof = MathTex(
            "d = \\overline{\\text{AC}} = \\overline{\\text{BD}} = \\overline{\\text{CD}} \\\\",
            "a = \\overline{\\text{AB}} = \\overline{\\text{BC}} = \\overline{\\text{AD}} \\\\",
            "d^{2} = d\\cdot a + a^{2} \\\\",
            "\\left(d\\over a\\right)^{2} = {\\left(d\\over a\\right)} + 1 \\\\",
            "\\left(d\\over a\\right)^{2} - {\\left(d\\over a\\right)} - 1 = 0 \\\\",
            "x^{2} - x - 1 = 0",
        )
        mean = MathTex(
            "x  = { {1 \\pm \\sqrt{5}}\\over 2 } \\\\",
            "\\left( d \\over a \\right) = { {1 + \\sqrt{5}}\\over 2 } \\\\",
            "\\text{\\large{Golden Mean!}} \\\\",
            "\\phi = { {1 + \\sqrt{5}}\\over 2 }"
        )
        proof[0:2].scale(0.75)
        proof.to_edge(6*RIGHT + 4*UP)
        mean.next_to(proof[0], DOWN)
        mean[2].set_color(YELLOW)
        mean[3].set_color(BLUE)

        for words in proof[0:2]:
            self.play(
                FadeIn(words),
            )
        self.wait()
        for words in proof[2:]:
            self.play(
                Write(words),
                lag_ratio = 0.35,
                run_time = len(words)/3
            )
            self.wait(2)
        self.wait(1)

        self.play(
            FadeOut(proof[0:5]),
            proof[5].animate.next_to(ptolemy_theorem[9], 2*DOWN)
        )
        self.wait()

        for words in mean:
            self.play(
                Write(words),
                lag_ratio = 0.35,
                run_time = len(words)/3
            )
            self.wait(2)

        self.play(
            Wiggle(mean[1]),
            run_time = 2
        )
        self.wait()
        self.clear()
