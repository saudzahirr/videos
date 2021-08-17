from manim import *


class Relativity(MovingCameraScene):
    def construct(self):
        clock = Circle(radius = 2, color = WHITE)
        clock.add(Dot(ORIGIN))
        for vect in compass_directions(12):
            clock.add(Line(1.8*vect, 2*vect, color = GREY))
        hour_hand = Line(ORIGIN, UP)
        minute_hand = Line(ORIGIN, 1.5*UP)
        hour_hand.get_center = lambda : clock.get_center()
        minute_hand.get_center = lambda : clock.get_center()
        clock.add(hour_hand, minute_hand)
        clock.scale(0.5)

        rect = Rectangle(height = 2)
        rect.scale(1.2)
        clock.add(rect)
        clock.shift(10 * RIGHT)
        clock.to_edge(2 * UP)

        moving_clock = always_shift(clock, direction = LEFT, rate = 2)
        rest_frame = Rectangle(height = 2)
        rest_frame.scale(1.2)
        rest_frame.to_edge(2 * DOWN)

        self.play(
            moving_clock.animate,
            rest_frame.animate
        )
        self.play(
            Rotating(hour_hand, radians = -2*np.pi, about_point = clock.get_center(),run_time = 5),
            Rotating(minute_hand, radians = -12*2*np.pi, about_point = clock.get_center(), run_time = 5),
            rate_func = linear,
        )
