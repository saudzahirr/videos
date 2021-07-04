from manim imporrt *

class Clock(Scene):
    def construct(self):
        clock = Circle(radius = 2, color = WHITE)
        clock.add(Dot(ORIGIN))
        for vect in compass_directions(12):
            clock.add(Line(1.8*vect, 2*vect, color = WHITE))
        hour_hand = Line(ORIGIN, UP)
        minute_hand = Line(ORIGIN, 1.5*UP)
        clock.add(hour_hand, minute_hand)
        hour_hand.get_center = lambda : clock.get_center()
        minute_hand.get_center = lambda : clock.get_center()
        self.add(clock)
        self.play(
            Rotating(hour_hand, radians = -2*np.pi, about_point = clock.get_center(),run_time = 5),
            Rotating(minute_hand, radians = -12*2*np.pi, about_point = clock.get_center(), run_time = 5),
            rate_func = slow_into,
        )
        self.wait()
