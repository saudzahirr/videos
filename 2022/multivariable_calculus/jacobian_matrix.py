from manimce import *


use_opengl_renderer = True


class ExampleLinearTransformation(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            background_plane_kwargs = {
                "faded_line_ratio" : 2
            },
            foreground_plane_kwargs = {
                "faded_line_ratio" : 2
            },
            show_coordinates = True,
            leave_ghost_vectors = True
        )

    def construct(self):
        matrix = [[2, 1], [-3, 1]]
        self.add_unit_square()
        self.apply_transposed_matrix(matrix)
        self.wait()


class ExampleMultivariableFunction(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            background_plane_kwargs = {
                "faded_line_ratio" : 2
            },
            foreground_plane_kwargs = {
                "faded_line_ratio" : 2
            },
            show_coordinates = True,
            leave_ghost_vectors = True
        )

    def construct(self):
        function = lambda p: array(
            [
                p[0] + sin(p[1]),
                p[1] + sin(p[0]),
                0
            ]
        )
        self.add_unit_square()
        self.apply_nonlinear_transformation(function)
        self.wait()
