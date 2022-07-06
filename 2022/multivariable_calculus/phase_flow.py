from manimce import *
from multivariable_calculus.helpers import *


class PhaseFlowExampleOne(PhaseFlowScene):
    def construct(self):
        function = lambda p: sin(p[1]) * RIGHT + cos(p[0]) * UP
        label = """\\begin{bmatrix} \\ x' \\ \\\\ \\ y' \\ \\end{bmatrix} = 
        \\begin{bmatrix} \\ { \\mathrm{sin}(y) } \\ \\\\ \\ { \\mathrm{cos}(x) } \\ \\end{bmatrix}
        """

        self.get_plane(show_axis = True, add_cordinate_labels = False)
        self.get_dots(color = YELLOW, show_creation = True)
        self.get_label(label)
        self.get_vector_field(function, show_vector_field = False)
        self.phase_flow(function, run_time = 10, rate_func = linear)
        self.wait()


class PhaseFlowExampleTwo(PhaseFlowScene):
    def construct(self):
        function = lambda p: (p[0] * UP - p[1] * RIGHT) / 5
        label = """\\begin{bmatrix} \\ x' \\ \\\\ \\ y' \\ \\end{bmatrix} = 
        {1 \\over 5} \\begin{bmatrix} \\ { - y } \\ \\\\ \\ { x } \\ \\end{bmatrix}"
        """

        self.get_plane(show_axis = True, add_cordinate_labels = False)
        self.get_dots(color = YELLOW, show_creation = True)
        self.get_label(label)
        self.get_vector_field(function, show_vector_field = False)
        self.phase_flow(function, run_time = 10, rate_func = linear)
        self.wait()


class PositiveDivergence(PhaseFlowScene):
    def construct(self):
        function = lambda p: p / (2 * get_norm(0.5 * p)**0.5 + 0.01)
        label = """p' = {p \\over { 2 \\sqrt{ \\norm{ p \\over 2 } } } }"""

        self.get_plane(show_axis = True, add_cordinate_labels = False)
        self.get_dots(color = YELLOW, show_creation = True)
        self.get_label(label)
        self.get_vector_field(function, show_vector_field = False)
        self.phase_flow(function, run_time = 10, rate_func = linear)
        self.wait()


class NegativeDivergence(PhaseFlowScene):
    def construct(self):
        function = lambda p: - p / (2 * get_norm(0.5 * p)**0.5 + 0.01)
        label = """p' = {-p \\over { 2 \\sqrt{ \\norm{ p \\over 2 } } } }"""

        self.get_plane(show_axis = True, add_cordinate_labels = False)
        self.get_dots(color = YELLOW, show_creation = True)
        self.get_label(label)
        self.get_vector_field(function, show_vector_field = False)
        self.phase_flow(function, run_time = 10, rate_func = linear)
        self.wait()


class IncompressibleFluid(PhaseFlowScene):
    def construct(self):
        function = lambda p: RIGHT + sin(p[0]) * UP
        label = """\\begin{bmatrix} \\ x' \\ \\\\ \\ y' \\ \\end{bmatrix} = 
        \\begin{bmatrix} \\ {1} \\ \\\\ \\  \\mathrm{sin}(x) \\ \\end{bmatrix}"""

        self.get_plane(show_axis = True, add_cordinate_labels = False)
        self.get_dots(color = YELLOW, show_creation = True)
        self.get_label(label)
        self.get_vector_field(function, show_vector_field = False)
        self.phase_flow(function, run_time = 10, rate_func = linear)
        self.wait()


class ConstantPositiveCurl(PhaseFlowScene):
    def construct(self):
        function = lambda p : 0.5 * (-p[1] * RIGHT + p[0] * UP)
        label = """\\begin{bmatrix} \\ x' \\ \\\\ \\ y' \\ \\end{bmatrix} = 
        {1 \\over 2} \\begin{bmatrix} \\ { -y } \\ \\\\ \\ { x } \\ \\end{bmatrix}"""

        self.get_plane(show_axis = True, add_cordinate_labels = False)
        self.get_dots(color = YELLOW, show_creation = True)
        self.get_label(label)
        self.get_vector_field(function, show_vector_field = False)
        self.phase_flow(function, run_time = 4, rate_func = linear)
        self.wait()


class SingleSwirl(PhaseFlowScene):
    def construct(self):
        function = lambda p: (- p[1] * RIGHT + p[0] * UP) / get_norm(p)
        label = """\\begin{bmatrix} \\ x' \\ \\\\ \\ y' \\ \\end{bmatrix} = 
        { { \\begin{bmatrix} \\ { -y } \\ \\\\ \\ { x } \\ \\end{bmatrix} } \\over { \\sqrt{ x^{2} + y^{2} } }"""

        self.get_plane(show_axis = True, add_cordinate_labels = False)
        self.get_dots(color = YELLOW, show_creation = True)
        self.get_label(label)
        self.get_vector_field(function, show_vector_field = False)
        self.phase_flow(function, run_time = 10, rate_func = linear)
        self.wait()


class DropletFlow(PhaseFlowScene):
    def construct(self):
        function = lambda p: p[1] * RIGHT + sin(2 * pi * p[0]) * UP
        label = """\\begin{bmatrix} \\ x' \\ \\\\ \\ y' \\ \\end{bmatrix} = 
        \\begin{bmatrix} \\ { y } \\ \\\\ \\ { \\mathrm{sin}(2\\pi x) } \\ \\end{bmatrix}"""

        self.get_plane(show_axis = True, add_cordinate_labels = False)
        self.get_dots(color = BLUE, show_creation = True)
        self.get_label(label)
        self.get_vector_field(function, show_vector_field = False)
        self.phase_flow(function, run_time = 10, rate_func = linear)
        self.wait()
