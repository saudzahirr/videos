from manimce import *


class JordanCurve(SVGMobject):
    file_name = get_svg("Jordan_curve_theorem.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)


class JordanCurveScene(Scene):
    def construct(self):
        jordan_curve = JordanCurve()
        jordan_curve[0].scale(8)
        jordan_curve[1].scale(4)
        jordan_curve[1].set_stroke(BLACK, 2)

        explanation = Tex(
            "A Jordan curve, a plane simple closed curve" "\\\\",
            "(drawn in black) divides the plane into" "\\\\",
            "an `inside' region (", "light blue", ") and an `outside' region (", "pink", ")."
        )
        explanation[3].set_color(BLUE_B)
        explanation[5].set_color(DARK_PINK)
        explanation.to_edge(UL)
        explanation.set_stroke(BLACK, 3, background = True)
        
        
        self.add(jordan_curve[0])
        self.play(
            DrawBorderThenFill(jordan_curve[1]),
            rate_func = smooth,
            run_time = 3
        )

        self.add_foreground_mobject(explanation)
        self.play(
            Write(explanation),
            rate_func = smooth,
            run_time = 4
        )
        self.wait()
