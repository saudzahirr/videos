from manimce import *


class ComplexPlaneRotation(Scene):
    def construct(self):
        self.add_title()
        self.add_plane()
    
    def add_title(self):
        title = Tex("Complex Rotation")
        title.set_stroke(BLACK, 5, background=True)
        title.scale(1.5)
        title.to_edge(UP)
        title.add_background_rectangle()
        self.add_foreground_mobjects(title)

    def add_plane(self):
        plane = ComplexPlane(
            x_range=[-FRAME_X_RADIUS, FRAME_X_RADIUS], y_range=[-FRAME_HEIGHT, FRAME_HEIGHT],
            faded_line_ratio = 2, make_smooth_after_applying_functions = True
        )
        background_grid = plane.copy()
        background_grid.set_color(GREY_B)
        background_grid.add_coordinates()
        self.add(background_grid)
        self.add(plane)
        self.wait(2)

        self.play(
            Rotate(plane, angle = PI),
            run_time = 2,
            rate_func = smooth
        )
        self.wait(2)
