from manimce import *



class CasusIrreducibilis(Scene):
    def construct(self):
        kwargs = {"run_time" : 3, "rate_func" : bezier([0, 0, 1, 1])}
        year = Tex("1545")
        year.scale(1.5)
        year.to_edge(UP + 2 * LEFT)
        
        equations = VGroup(
            MathTex("x^{2} + 2x + 2 = 0"),
            MathTex("x^{3} = 6x + 4")
        )
        equations.arrange(RIGHT, buff = 3.0)

        roots = VGroup(
            MathTex("-1 \\pm \\sqrt{-1}",),
            MathTex("\\sqrt[3]{2 + \\sqrt{-2}}  + \\sqrt[3]{2 - \\sqrt{-2}} ")
        )
        roots.arrange(RIGHT, buff = 3.0)

        self.play(
            Write(year),
            rate_func = smooth
        )
        for equation, root in zip(equations, roots):
            root.next_to(equation, DOWN, buff = 1.0)
            self.play(
                Write(equation),
                rate_func = smooth
            )
            self.wait(0.5)
            self.play(
                Write(root),
                rate_func = smooth
            )
            self.wait(1)
        self.wait(2)

        self.play(
            FadeOut(year, equations, roots[0]),
            roots[1].animate.next_to(ORIGIN, 0.25 * RIGHT)
        )
        self.wait()


        casus_irreducibilis = Tex(r"Casus Irreducibilis")
        casus_irreducibilis.scale(1.2)
        casus_irreducibilis.next_to(roots[1], UP, buff = 1.5)
        translation = Tex("Latin for ", "“the irreducible case”")
        translation.set_color_by_tex("“the irreducible case”", YELLOW)
        translation.set_color(GREY_B)
        translation.next_to(casus_irreducibilis, DOWN, buff = 0.25)
        bombelli = ImageMobject(get_portrait("Rafael_Bombelli.jpeg"))
        bombelli.scale(1.5)
        bombelli.to_edge(LEFT)
        bombelli.shift(DOWN)
        rafael_bombelli = Tex(r"Rafael Bombelli")
        rafael_bombelli.next_to(bombelli, DOWN)


        self.play(
            Write(casus_irreducibilis)
        )
        self.wait()
        self.play(
            Write(translation)
        )
        self.wait(2)

        self.play(
            FadeIn(bombelli, rafael_bombelli),
            rate_func = smooth,
            run_time = 2
        )
        self.wait()


        speech = SpeechBubble()
        speech.next_to(bombelli.get_right(), UP)
        words = Tex(
            "Plus by plus of minus," "\\\\",
            "makes plus of minus." "\\\\",
            "Minus by plus of minus," "\\\\",
            "makes minus of minus." "\\\\"
        )
        speech.add_content(words)
        speech.position_mobject_inside(words)
        speech.resize_to_content()
        speech.move_tip_to(bombelli.get_right())


        self.play(
            Create(speech),
            Write(words, run_time = 3, rate_func = smooth),
            rate_func = smooth
        )
        self.wait(2)


        bombelli_rules = Tex(
            "“plus of minus” for $i = \\sqrt{-1}$" "\\\\",
            "“minus of minus” for $-i = -\\sqrt{-1}$",
        )
        bombelli_rules.set_color(YELLOW)
        bombelli_rules.next_to(roots[1], DOWN, buff = 1.0)

        self.play(
            Write(bombelli_rules),
            rate_func = smooth,
            run_time = 3
        )
        self.wait()
