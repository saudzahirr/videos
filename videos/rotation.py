from manimce import *


class RotationScene(Scene):
    def construct(self):
        self.camera.background_color = GREY_E
        screen = ScreenRectangle(stroke_width=4,stroke_color=WHITE,fill_opacity=1,fill_color=BLACK)
        screen.scale(1.3)
        screen.to_edge(DOWN)
        self.add(screen)
        exps = VGroup(
            MathTex("e^{", "\\begin{bmatrix} 0 & -1 \\\\ 1 & 0 \\end{bmatrix}", "t}"),
            MathTex("e^{it}", tex_to_color_map={"i": RED}),
            MathTex(
                "e^{(ai + bj + ck)t}",
                tex_to_color_map={
                    "i": RED,
                    "j": GREEN,
                    "k": BLUE,
                }
            ),
            MathTex(
                "e^{i \\sigma_1 t}, \\quad ",
                "e^{i \\sigma_2 t}, \\quad ",
                "e^{i \\sigma_3 t}",
                tex_to_color_map={
                    "\\sigma_1": RED,
                    "\\sigma_2": GREEN,
                    "\\sigma_3": BLUE,
                }
            ),
        )
        exps[1:].scale(1.5)
        exps[0][1].set_color_by_gradient(WHITE, MAROON_B, MAROON_C, MAROON_C, MAROON_B, WHITE)
        exps[0][2].scale(1.5)
        exps[0][1].shift(0.25 * UP)
        exps[0][2].shift(0.15 * DOWN)
        exps[0][0].set_height(0.35)

        labels = VGroup(
            Tex("$90^\\circ$ Rotation Matrix:"),
            Tex("Imaginary Numbers:"),
            Tex("Quaternions:"),
            Tex("Pauli Matrices:"),
        )
        labels.scale(1.3)
        for label, exp in zip(labels, exps):
            label.next_to(exp, LEFT, 0.75*LARGE_BUFF)
            label.add(exp)

        quat_note = MathTex("(a^2 + b^2 + c^2 = 1)").scale(0.75)
        quat_note.next_to(exps[2], DOWN, aligned_edge=LEFT)
        exps[2].add(quat_note)

        labels.arrange(RIGHT, buff = 2*LARGE_BUFF)
        labels.move_to(ORIGIN, LEFT)
        labels.to_edge(UP)
        self.play(
            labels.animate.shift((labels.get_width() - 5) * LEFT),
            run_time=20,
            rate_func = smooth
        )
        

        
class RotationIn3dPlane(ExternallyAnimatedScene):
    pass
