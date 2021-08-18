from manim import *


class Relativity(MovingCameraScene):
    def construct(self):
        rest_frame = self.camera.frame

        t_tracker = VectorizedPoint()
        k_tracker = VectorizedPoint(2*RIGHT)
        always_shift(t_tracker, RIGHT, 1)

        moving_frame = ScreenRectangle(height = 2)
        moving_frame.to_edge(RIGHT)
        always_shift(moving_frame, LEFT, 1)
        moving_frame_movement = moving_frame


        ref_frame1 = Tex("Rest frame")
        ref_frame1.to_edge(UP)
        ref_frame2 = Tex("Moving frame")
        ref_frame2.next_to(moving_frame, UP)
        ref_frame2_follow = Mobject.add_updater(
            ref_frame2, lambda m : m.next_to(moving_frame, UP)
        )

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
        clock.to_edge(LEFT + DOWN)

        self.add(
            t_tracker, moving_frame_movement,
            ref_frame2_follow, ref_frame1,
            clock
        )
        self.add(ref_frame1)
        self.play(
            Rotating(hour_hand, radians = -1*np.pi, about_point = clock.get_center(),run_time = 4),
            Rotating(minute_hand, radians = -6*2*np.pi, about_point = clock.get_center(), run_time = 4),
            rate_func = linear,
        )
        self.play(
            MaintainPositionRelativeTo(
                rest_frame, moving_frame,
                run_time = 10
            ),
            Rotating(hour_hand, radians = -1*np.pi, about_point = clock.get_center(),run_time = 10),
            Rotating(minute_hand, radians = -6*2*np.pi, about_point = clock.get_center(), run_time = 10),
            rate_func = linear,
        )
        self.play(
            #moving_frame.animate.shift(5 * RIGHT),
            Rotating(hour_hand, radians = -1*np.pi, about_point = clock.get_center(),run_time = 4),
            Rotating(minute_hand, radians = -6*2*np.pi, about_point = clock.get_center(), run_time = 4),
            rate_func = linear,
        )
