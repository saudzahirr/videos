from manimce import *



DARK_BLUE = interpolate_color(BLUE_D, BLUE_E, 0.5)

def number_plane(x, y):
    plane = NumberPlane(
        x_range = [-x, x],
        y_range = [-y, y],
        x_length = 2*x,
        y_length = 2*y,
        background_line_style = {
            "stroke_color": GREY_B,
            "stroke_opacity": 1,
            "stroke_width": 1,
        },
        faded_line_ratio = 2,
    )
    plane.axes.set_stroke(opacity = 1.5)
    plane.set_fill(GREY_BROWN)
    plane.add(SurroundingRectangle(plane, WHITE, buff = 0.0, stroke_width = 2))
    return plane


def glow_dot(point, r_min = 0.05, r_max = 0.15, color = YELLOW, n = 20, opacity_mult = 1.0):
    result = VGroup(*(
        Dot(point, radius = interpolate(r_min, r_max, a))
        for a in linspace(0, 1, n)
    ))
    result.set_fill(color, opacity = opacity_mult / n)
    return result



from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL
class Count(VMobject, metaclass = ConvertToOpenGL):
    def __init__(
        self, count, **kwargs
    ):
        self.tracker = ValueTracker(count)
        self.value = Integer(self.tracker.get_value())
        self.value.add_updater(lambda v: v.set_value(self.tracker.get_value()))

        super().__init__(**kwargs)
        self.add(self.value)



class Draw(Write):
    def __init__(self, line, **kwargs):
        Write.__init__(self, line, **kwargs)
