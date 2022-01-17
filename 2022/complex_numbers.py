from manimce import *



class CasusIrreducibilis(Scene):
    def construct(self):
        year = Tex("1545")
        year.scale(1.5)
        year.to_edge(UP + 2 * LEFT)
        italy_map = SVGMobject(get_svg("Italy.svg"))
        italy_map.scale(1.5)
        italy_map.next_to(year, RIGHT, buff = 1.0)

        for part, color in zip(italy_map, cycle([GREEN, WHITE, RED])):
            part.set_color(color)
        
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
            DrawBorderThenFill(italy_map),
            run_time = 2,
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
            FadeOut(year, italy_map, equations, roots[0]),
            roots[1].animate.move_to(ORIGIN)
        )
        self.wait()


        casus_irreducibilis = Tex(r"Casus Irreducibilis")
        casus_irreducibilis.scale(1.2)
        casus_irreducibilis.next_to(roots[1], UP, buff = 1.0)
        translation = Tex(r"Latin for “the irreducible case”")
        translation.set_color(GREY_B)
        translation.next_to(casus_irreducibilis, DOWN, buff = 0.25)
        bombelli = ImageMobject(get_portrait("Rafael_Bombelli.jpeg"))
        bombelli.scale(1.5)
        bombelli.to_edge(LEFT)
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
            FadeIn(bombelli),
            Write(rafael_bombelli),
            rate_func = smooth,
            run_time = 2
        )
        self.wait()
