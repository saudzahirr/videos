from manimce import *


class LawsOfProbability(Scene):
    def construct(self):
        title = Tex('Laws of Probability')
        title.scale(2)
        title.to_edge(UP)
        #self.add(title)
        venn_diagram = self.get_venn_diagram()
        venn_diagram.to_edge(2 * RIGHT)
        venn_diagram.shift(DOWN)
        formula = Tex(
            'P','$($', 'A', '$\\cup$', 'B', '$) = \\ $', 'P',
            '$($', 'A', '$) \\ + \\ $', 'P', '$($', 'B', '$)$',
            '$ \\ - \\ $', 'P', '$($', 'A', '$\\cap$', 'B', '$)$',
            tex_to_color_map = {
                'A' : YELLOW,
                'B' : BLUE
            }
        )
        formula.scale(1.5)
        formula.to_edge(UP + LEFT)
        arrow = Arrow(
            formula[14:].get_bottom(),
            venn_diagram.get_center(),
        )
        speech_bubble = SpeechBubble()
        speech_bubble.add(
            Tex(
                'Mutually Exclusive \\\\ Events!'
                ' P$($A$\\cap$B$)= \\ 0$',
                tex_to_color_map = {
                    'P$($A$\\cap$B$)= \\ 0$' : GREY_BROWN
                }
            ).scale(1.35).move_to(speech_bubble.get_center()).shift(0.75*UP)
        )
        #speech_bubble.scale(1.2)
        speech_bubble.to_edge(LEFT + 2 * DOWN)
        speech_bubble.shift(RIGHT + 2.5 * UP)
        kolmogorov = ImageMobject('Andrej_Nikolajewitsch_Kolmogorov.jpg')
        kolmogorov.scale(2)
        kolmogorov.to_edge(LEFT + DOWN)
        venn_diagram.save_state()

        self.play(
            FadeIn(venn_diagram[0][2]),
            Write(venn_diagram[1][2]),
            run_time = 1.5,
        )

        for i in (0, 1):
            self.play(
                FadeIn(venn_diagram[0][i]),
                Write(venn_diagram[1][i]),
                run_time = 1.5,
            )

        self.wait(2)

        self.play(
            Write(formula, run_time = 4),
            GrowArrow(arrow),
            run_time = 2,
            rate_func = smooth
        )
        self.wait()

        self.play(
            Group(venn_diagram[0][0], venn_diagram[1][0]).animate.shift(0.75*LEFT),
            Group(venn_diagram[0][1], venn_diagram[1][1]).animate.shift(0.75*RIGHT),
            formula[14:].animate.set_opacity(0.2),
            FadeOut(arrow),
            run_time = 2,
            rate_func = smooth
        )
        self.wait()
        self.play(FadeIn(kolmogorov), rate_func = smooth)
        self.play(
            Write(speech_bubble),
            run_time = 4,
            rate_func = smooth
        )
        self.wait(3)

        self.play(
            FadeOut(kolmogorov, speech_bubble),
            run_time = 1
        )
        self.play(
            Restore(venn_diagram),
            formula[14:].animate.set_opacity(1),
            FadeIn(arrow),
            run_time = 2,
            rate_func = smooth
        )
        self.wait(2)

        




    def get_venn_diagram(self):
        box = Rectangle(height = 5.0, width = 8.0, fill_color = BLACK, fill_opacity = 0)
        c1 = Circle(
            radius = 1.5,
            stroke_width = 2,
            stroke_color = YELLOW,
            fill_opacity = 0.5,
            fill_color = YELLOW,
        )
        c1.flip(RIGHT)
        c1.rotate(3 * TAU / 8)
        c2 = c1.copy()
        c2.set_color(BLUE)
        c1.shift(LEFT)
        c2.shift(RIGHT)
        diagram = VGroup(c1, c2, box)

        titles = VGroup(
            Tex("A"),
            Tex("B"),
            Tex("S")
        )
        for title, part, vect in zip(titles[0:2], diagram[0:2], [UL, UR]):
            title.match_color(part)
            title.scale(2)
            title.next_to(
                part.get_boundary_point(vect),
                vect,
                buff=SMALL_BUFF
            )
        
        titles[2].scale(2)
        titles[2].next_to(diagram[2].get_left(), 6 * DOWN)
        titles[2].shift(0.5 * RIGHT)

        return VGroup(diagram, titles)











