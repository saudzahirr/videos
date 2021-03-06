from manimce import *


class PhaseFlowScene(Scene):

    def get_plane(self, show_axis = True, add_cordinate_labels = False):
        plane = NumberPlane(
            x_range = (-FRAME_WIDTH, FRAME_WIDTH),
            y_range = (-FRAME_HEIGHT, FRAME_HEIGHT),
            faded_line_ratio = 2
        )
        plane.axes.set_color(BLUE_E)


        if show_axis is True:
            plane.axes.set_color(GREY_B)

        if add_cordinate_labels is True:
            plane.add_coordinates()

        self.add(plane)


    def get_dots(self, color, show_creation = True):
        dots = VGroup()
        for x in range(-10, 10):
            for y in range(-10, 10):
                dots.add(Dot(array([x, y, 0]), color = color))
        
        dots.move_to(ORIGIN)

        self.dots = dots

        if show_creation is True:
            self.play(
                Create(dots)
            )
        
        else:
            self.add(dots)
    

    def get_vector_field(self, function, show_vector_field = False):
        if show_vector_field is True:
            field = ArrowVectorField(function, colors = [RED, YELLOW, GREEN, TEAL, BLUE])
            
            self.play(
                Create(field),
                run_time = 1,
                rate_func = linear
            )


    def get_streamlines(self, function):
        stream_lines = StreamLines(
            function, stroke_width = 3, max_anchors_per_line = 10, virtual_time = 1, color = GREY_A
        )
        self.add(stream_lines)
        stream_lines.start_animation(warm_up = False, flow_speed = 3/4, time_width = 0.5)


    def get_label(self, label):
        matrix_function = MathTex(label)
        matrix_function.scale(1.25)
        matrix_function.set_fill(WHITE, 2)
        matrix_function.to_corner(UL, buff = 0.25)
        self.add_foreground_mobjects(matrix_function)
        matrix_function.add_background_rectangle()


    def phase_flow(self, function, run_time, rate_func = linear):
        self.play(
            PhaseFlow(
                function = function, mobject = self.dots,
            ),
            run_time = run_time,
            rate_func = rate_func
        )
