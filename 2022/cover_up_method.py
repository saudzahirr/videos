from manimce import *


class PartialFractions(Scene):
    def construct(self):
        partial_fraction = Tex(
            "${ { lx^{2} + mx + n } \over { (x-a)(x-b)(x-c) } } =$",
            "$ { A \over (x - a) } $", "$ +$",
            "$ { B \over (x - b) } $","$ +$",
            "$ { C \over (x - c) }$",
            tex_to_color_map = {
                "$A$" : BLUE_B,
                "$B$" : BLUE_C,
                "$C$" : BLUE_D
            }
        )
        partial_fraction.scale(1.25)
        partial_fraction.set_stroke(BLACK, 5, background = True)

        self.play(
            Write(partial_fraction),
            run_time = 2,
            rate_func = smooth
        )
        self.wait()
        partial_fraction.save_state()

        for a in [1, 3, 5]:
            partial_fraction.set_opacity(0.5)
            self.play(
                partial_fraction[a].animate.set_opacity(1),
                rate_func = smooth
            )
            self.wait()
            self.play(
                Restore(partial_fraction),
                rate_func = smooth
            )
            self.wait(0.5)

        self.wait()
