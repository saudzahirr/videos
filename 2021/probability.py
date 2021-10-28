from manimce import *


class LawsOfProbability(Scene):
    def construct(self):
        formula = self.get_formula()

        venn_diagram = self.get_venn_diagram()
        venn_diagram.next_to(formula, DOWN, LARGE_BUFF)

        arrow = Arrow(
            formula[3].get_bottom(),
            venn_diagram.get_center(),
        )

        self.add(formula)
        self.play(
            formula[:3].animate.set_opacity(0.2),
            formula[-3:].animate.set_opacity(0.2),
        )
        for i in (0, 1):
            self.play(
                FadeIn(venn_diagram[0][i]),
                Write(venn_diagram[1][i]),
                run_time=1,
            )
        self.play(Create(arrow))
        self.wait()
    

    def get_formula(self):
        kw = {
            "tex_to_color_map": {
                "A": YELLOW,
                "B": BLUE,
            }
        }
        parts = VGroup(*[
            Tex(tex, **kw)
            for tex in [
                "P(B)", "P(A|B)", "=",
                "P(A \\text{ and } B)",
                "=", "P(A)", "P(B|A)",
            ]
        ])
        attrs = [
            "pb", "pab", "eq1", "p_both", "eq2", "pa", "pba"
        ]
        for attr, part in zip(attrs, parts):
            setattr(parts, attr, part)

        parts.arrange(RIGHT, buff=SMALL_BUFF),
        parts.set_width(FRAME_WIDTH - 1)
        parts.center().to_edge(UP)
        return parts


    def get_venn_diagram(self):
        c1 = Circle(
            radius=2.5,
            stroke_width=2,
            stroke_color=YELLOW,
            fill_opacity=0.5,
            fill_color=YELLOW,
        )
        c1.flip(RIGHT)
        c1.rotate(3 * TAU / 8)
        c2 = c1.copy()
        c2.set_color(BLUE)
        c1.shift(LEFT)
        c2.shift(RIGHT)
        circles = VGroup(c1, c2)

        titles = VGroup(
            Tex("A"),
            Tex("B"),
        )
        for title, circle, vect in zip(titles, circles, [UL, UR]):
            title.match_color(circle)
            title.scale(2)
            title.next_to(
                circle.get_boundary_point(vect),
                vect,
                buff=SMALL_BUFF
            )

        return VGroup(circles, titles)
      
      
      
      
      
      
      
      
      
      
      
      
      
