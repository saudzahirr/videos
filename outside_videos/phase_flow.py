from manimce import *



class PhaseFLowScene(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range = (-FRAME_WIDTH, FRAME_WIDTH),
            y_range = (-FRAME_HEIGHT, FRAME_HEIGHT),
            background_line_style = {
                "stroke_color": GREY_B,
                "stroke_opacity": 1,
                "stroke_width": 2
            },
            faded_line_ratio = 4
        )
        self.add(plane)

        points = VGroup()
        for x in range(-10, 10):
            for y in range(-10, 10):
                points.add(Dot(np.array([x, y, 0]), color = WHITE))
        self.add(points)
        self.wait()


        def function(t):
            return 0.5*(t**3 - 9*t)*RIGHT + 0.5*(t**3 - 9*t)*UP

        self.play(
            PhaseFlow(function, points),
            rate_func = smooth,
            run_time = 5
        )
        self.wait()
