from manimce import *
from Fourier_Series.fourier_series_mobject import *




class SkullandCrossedBones(SVGMobject):
    file_name = get_svg("Skull_and_crossed_bones.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.85)
        self.set_color(GREY_B)
        self.set_stroke(GREY_D, 2)


class FourierSeriesScene(ZoomedScene, MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(
            zoom_factor = 0.3,
            zoomed_display_height = 5,
            zoomed_display_width = 5,
            image_frame_stroke_width = 1,
            zoomed_camera_config = {
                "default_frame_stroke_width": 1,
                },
            **kwargs
        )

    def setup(self):
        MovingCameraScene.setup(self)
        ZoomedScene.setup(self)

    def construct(self):
        self.add_sound(get_sound("Euler's_Clock.mp3"))
        N = 1000
        # tex = "$e^{i \\theta}$"
        # shape = Tex(tex)
        shape = SVGMobject(get_svg("Re.svg"))
        # shape = SkullandCrossedBones()
        # self.add(shape)

        def get_shape(shape):
            path = VMobject()
            shape = shape
            for sp in shape.family_members_with_points():
                path.append_points(sp.get_points())
            return path
        path = get_shape(shape)
        complex_points = np.array([complex(*path.point_from_proportion(alpha)[:2]) for alpha in np.arange(0, 1, 1 / N)])
        complex_points = (complex_points - np.mean(complex_points)) / np.max(abs(complex_points)) * 4
        
        ec = FourierEpicyclesMObject(complex_points, num_coefs = 1000, speed_factor = 1/20,
                                     circles_color = YELLOW, circles_opacity = 0.75)
        self.add_foreground_mobjects(ec)
        self.wait(12)

        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame
        zoomed_display.to_edge(2 * DL)
        zd_rect = BackgroundRectangle(zoomed_display, fill_opacity = 0, buff = MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)
        unfold_camera = UpdateFromFunc(zd_rect, lambda rect: rect.replace(zoomed_display))

        
        frame.add_updater(lambda m: m.move_to(
            ec.get_rect_center()
        ))
        self.play(Create(frame))
        self.activate_zooming()
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)

        for a in range(0, 25):
            self.wait(2)
        
        for a in range(0, 5):
            self.wait(5)
           
        self.clear()
