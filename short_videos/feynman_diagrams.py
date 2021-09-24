from manimce import *

class Feynman(Scene):
    def construct(self):
    
        feynman_diagram = self.get_feynman_diagram()
        feynman_diagram.scale(1.5)
        
        self.play(LaggedStartMap(
            Write, feynman_diagram,
            run_time=4
        ))
        self.wait()

    def get_feynman_diagram(self):
        arrow = Arrow(LEFT, RIGHT, buff=0, stroke_width = 4.5, tip_length = 0.85 * DEFAULT_ARROW_TIP_LENGTH)
        arrow.tip.move_to(arrow.get_center())
        arrows = VGroup(*[
            arrow.copy().rotate(angle).next_to(point, vect, buff=0)
            for (angle, point, vect) in [
                (-45 * DEGREES, -1.5 * RIGHT, UL),
                (-135 * DEGREES, -1.5 * RIGHT, DL),
                (-135 * DEGREES, 1.5 * RIGHT, UR),
                (-45 * DEGREES, 1.5 * RIGHT, DR),
            ]
        ])
        labels = VGroup(*[
            MathTex(tex)
            for tex in ["e^{-}", "e^{+}", "\\text{\\=q}", "q"]
        ])
        vects = [UR, DR, UL, DL]
        for arrow, label, vect in zip(arrows, labels, vects):
            label.next_to(arrow.get_center(), vect, buff=1.25*SMALL_BUFF)

        wave = FunctionGraph(
            lambda x: 0.2 * np.sin(2 * TAU * x),
            x_range=[-1.5, 1.5]
        )
        wave_label = MathTex("\\gamma")
        wave_label.next_to(wave, UP, SMALL_BUFF)
        labels.add(wave_label)

        squiggle = ParametricFunction(
            lambda t: np.array([
                t + 0.5 * np.sin(TAU * t),
                0.5 * np.cos(TAU * t),
                0,
            ]),
            t_range=[0,4]
        )
        squiggle.scale(0.25)
        squiggle.set_color(BLUE)
        squiggle.rotate(-30 * DEGREES)
        squiggle.next_to(
            arrows[2].point_from_proportion(0.75),
            DR, buff=0
        )
        squiggle_label = MathTex("g")
        squiggle_label.next_to(squiggle, UR, buff=-MED_SMALL_BUFF)
        labels.add(squiggle_label)

        return VGroup(arrows, wave, squiggle, labels)
