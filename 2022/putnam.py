from manimce import *


use_opengl_renderer = True


class Introduction(Scene):
    def construct(self):
        pass


class Probabilities(Scene):
    def construct(self):
        self.camera.background_color = GREEN_SCREEN

        count = Variable(
            0.000, Tex("Count", stroke_width = 1.15),
            num_decimal_places = 3
        )
        probability = Variable(
            0.000, Tex("Probability", stroke_width = 1.15),
            num_decimal_places = 3
        )
        Group(count, probability).arrange(DOWN).to_corner(UL)


        probability.add_updater(lambda v: v.tracker.set_value(count.tracker.get_value()*0.01))
        self.add(count, probability)

        P = [
            0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0,
            2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0,
            3.0, 3.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0,
            4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 5.0, 5.0, 5.0, 5.0,
            5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
            5.0, 5.0, 6.0, 6.0, 6.0, 7.0, 7.0, 7.0, 7.0, 8.0,
            8.0, 8.0, 9.0, 9.0, 9.0, 9.0, 10.0, 10.0, 10.0, 10.0,
            10.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 12.0, 12.0, 
            12.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0
        ]
    
        for p in P[:2]:
            self.play(
                count.tracker.animate.set_value(p),
                rate_func = linear,
                run_time = 1/2
            )
            self.wait()


class QuestionPaper(ExternallyAnimatedScene):
    pass


class RandomTetrahedronInSphere(ExternallyAnimatedScene):
    pass
