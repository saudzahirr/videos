from manimce import *


use_opengl_renderer = True



class PhaseFlowExampleOne(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range = (-FRAME_WIDTH, FRAME_WIDTH),
            y_range = (-FRAME_HEIGHT, FRAME_HEIGHT),
            faded_line_ratio = 2
        )
        plane.axes.set_color(GREY_B)
        self.add(plane)

        matrix_function = MathTex(
            "\\begin{bmatrix} \\ x' \\ \\\\ \\ y' \\ \\end{bmatrix} = \\begin{bmatrix} \\ { \\mathrm{sin}(y) } \\ \\\\ \\ { \\mathrm{cos}(x) } \\ \\end{bmatrix}"
        )
        matrix_function.scale(1.25)
        matrix_function.set_fill(WHITE, 2)
        matrix_function.to_corner(UL, buff = 0.25)
        self.add_foreground_mobjects(matrix_function)
        matrix_function.add_background_rectangle()

        dots = VGroup()
        for x in range(-10, 10):
            for y in range(-10, 10):
                dots.add(Dot(array([x, y, 0]), color = YELLOW))
        
        dots.move_to(ORIGIN)

        function = lambda p: sin(p[1]) * RIGHT + cos(p[0]) * UP
        field = ArrowVectorField(function, colors = [RED, YELLOW, GREEN, TEAL, BLUE])
        

        self.play(Create(dots), run_time = 1)
        self.wait()

        self.play(
            PhaseFlow(
                function = function, mobject = dots,
            ),
            # Create(field),
            run_time = 10,
            rate_func = linear
        )
        # self.wait(2)



class PhaseFlowExampleTwo(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range = (-FRAME_WIDTH, FRAME_WIDTH),
            y_range = (-FRAME_HEIGHT, FRAME_HEIGHT),
            faded_line_ratio = 2
        )
        plane.axes.set_color(GREY_B)
        self.add(plane)

        matrix_function = MathTex(
            "\\begin{bmatrix} \\ x' \\ \\\\ \\ y' \\ \\end{bmatrix} = {1 \\over 5} \\begin{bmatrix} \\ { - y } \\ \\\\ \\ { x } \\ \\end{bmatrix}"
        )
        matrix_function.scale(1.25)
        matrix_function.set_fill(WHITE, 2)
        matrix_function.to_corner(UL, buff = 0.25)
        self.add_foreground_mobjects(matrix_function)
        matrix_function.add_background_rectangle()

        dots = VGroup()
        for x in range(-10, 10):
            for y in range(-10, 10):
                dots.add(Dot(array([x, y, 0]), color = YELLOW))
        
        dots.move_to(ORIGIN)

        function = lambda p: (p[0] * UP - p[1] * RIGHT) / 5
        field = ArrowVectorField(function, colors = [RED, YELLOW, GREEN, TEAL, BLUE])
        

        self.play(Create(dots), run_time = 1)
        self.wait()

        self.play(
            PhaseFlow(
                function = function, mobject = dots,
            ),
            # Create(field),
            run_time = 10,
            rate_func = linear
        )
        # self.wait(2)



class PositiveDivergence(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range = (-FRAME_WIDTH, FRAME_WIDTH),
            y_range = (-FRAME_HEIGHT, FRAME_HEIGHT),
            faded_line_ratio = 2
        )
        plane.axes.set_color(GREY_B)
        self.add(plane)

        matrix_function = MathTex(
            "p' = {p \\over { 2 \\sqrt{ \\norm{ p \\over 2 } } } }"
        )
        matrix_function.scale(1.25)
        matrix_function.set_fill(WHITE, 2)
        matrix_function.to_corner(UL, buff = 0.25)
        self.add_foreground_mobjects(matrix_function)
        matrix_function.add_background_rectangle()

        dots = VGroup()
        for x in range(-10, 10):
            for y in range(-10, 10):
                dots.add(Dot(array([x, y, 0]), color = YELLOW))
        
        dots.move_to(ORIGIN)

        function = lambda p: p / (2 * get_norm(0.5 * p)**0.5 + 0.01)
        field = ArrowVectorField(function, colors = [RED, YELLOW, GREEN, TEAL, BLUE])
        

        self.play(Create(dots), run_time = 1)
        self.wait()

        self.play(
            PhaseFlow(
                function = function, mobject = dots,
            ),
            # Create(field),
            run_time = 10,
            rate_func = linear
        )
        # self.wait(2)



class NegativeDivergence(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range = (-FRAME_WIDTH, FRAME_WIDTH),
            y_range = (-FRAME_HEIGHT, FRAME_HEIGHT),
            faded_line_ratio = 2
        )
        plane.axes.set_color(GREY_B)
        self.add(plane)

        matrix_function = MathTex(
            "p' = {-p \\over { 2 \\sqrt{ \\norm{ p \\over 2 } } } }"
        )
        matrix_function.scale(1.25)
        matrix_function.set_fill(WHITE, 2)
        matrix_function.to_corner(UL, buff = 0.25)
        self.add_foreground_mobjects(matrix_function)
        matrix_function.add_background_rectangle()

        dots = VGroup()
        for x in range(-10, 10):
            for y in range(-10, 10):
                dots.add(Dot(array([x, y, 0]), color = YELLOW))
        
        dots.move_to(ORIGIN)

        function = lambda p: - p / (2 * get_norm(0.5 * p)**0.5 + 0.01)
        field = ArrowVectorField(function, colors = [RED, YELLOW, GREEN, TEAL, BLUE])
        

        self.play(Create(dots), run_time = 1)
        self.wait()

        self.play(
            PhaseFlow(
                function = function, mobject = dots,
            ),
            # Create(field),
            run_time = 10,
            rate_func = linear
        )
        # self.wait(2)



class IncompressibleFluid(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range = (-FRAME_WIDTH, FRAME_WIDTH),
            y_range = (-FRAME_HEIGHT, FRAME_HEIGHT),
            faded_line_ratio = 2
        )
        plane.axes.set_color(GREY_B)
        self.add(plane)

        matrix_function = MathTex(
            "\\begin{bmatrix} \\ x' \\ \\\\ \\ y' \\ \\end{bmatrix} = \\begin{bmatrix} \\ {1} \\ \\\\ \\  \\mathrm{sin}(x) \\ \\end{bmatrix}"
        )
        matrix_function.scale(1.25)
        matrix_function.set_fill(WHITE, 2)
        matrix_function.to_corner(UL, buff = 0.25)
        self.add_foreground_mobjects(matrix_function)
        matrix_function.add_background_rectangle()

        dots = VGroup()
        for x in range(-20, 20):
            for y in range(-20, 20):
                dots.add(Dot(array([x, y, 0]), color = YELLOW))
        
        dots.move_to(ORIGIN)

        function = lambda p: RIGHT + sin(p[0]) * UP
        field = ArrowVectorField(function, colors = [RED, YELLOW, GREEN, TEAL, BLUE])
        

        self.play(Create(dots), run_time = 1)
        self.wait()

        self.play(
            PhaseFlow(
                function = function, mobject = dots,
            ),
            # Create(field),
            run_time = 10,
            rate_func = linear
        )
        # self.wait(2)



class ConstantPositiveCurl(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range = (-FRAME_WIDTH, FRAME_WIDTH),
            y_range = (-FRAME_HEIGHT, FRAME_HEIGHT),
            faded_line_ratio = 2
        )
        plane.axes.set_color(GREY_B)
        self.add(plane)

        matrix_function = MathTex(
            "\\begin{bmatrix} \\ x' \\ \\\\ \\ y' \\ \\end{bmatrix} = {1 \\over 2} \\begin{bmatrix} \\ { -y } \\ \\\\ \\ { x } \\ \\end{bmatrix}"
        )
        matrix_function.scale(1.25)
        matrix_function.set_fill(WHITE, 2)
        matrix_function.to_corner(UL, buff = 0.25)
        self.add_foreground_mobjects(matrix_function)
        matrix_function.add_background_rectangle()

        dots = VGroup()
        for x in range(-10, 10):
            for y in range(-10, 10):
                dots.add(Dot(array([x, y, 0]), color = YELLOW))
        
        dots.move_to(ORIGIN)

        function = lambda p : 0.5 * (-p[1] * RIGHT + p[0] * UP)
        field = ArrowVectorField(function, colors = [RED, YELLOW, GREEN, TEAL, BLUE])
        

        self.play(Create(dots))
        self.wait()

        self.play(
            PhaseFlow(
                function = function, mobject = dots
            ),
            run_time = 4,
            rate_func = linear
        )
        # self.wait()
        
        
        
class SingleSwirl(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range = (-FRAME_WIDTH, FRAME_WIDTH),
            y_range = (-FRAME_HEIGHT, FRAME_HEIGHT),
            faded_line_ratio = 2
        )
        plane.axes.set_color(GREY_B)
        self.add(plane)

        matrix_function = MathTex(
            "\\begin{bmatrix} \\ x' \\ \\\\ \\ y' \\ \\end{bmatrix} = { { \\begin{bmatrix} \\ { -y } \\ \\\\ \\ { x } \\ \\end{bmatrix} } \\over { \\sqrt{ x^{2} + y^{2} } }"
        )
        matrix_function.scale(1.25)
        matrix_function.set_fill(WHITE, 2)
        matrix_function.to_corner(UL, buff = 0.25)
        self.add_foreground_mobjects(matrix_function)
        matrix_function.add_background_rectangle()

        dots = VGroup()
        for x in range(-10, 10):
            for y in range(-10, 10):
                dots.add(Dot(array([x, y, 0]), color = YELLOW))
        
        dots.move_to(ORIGIN)


        function = lambda p: (- p[1] * RIGHT + p[0] * UP) / get_norm(p)
        # field = ArrowVectorField(function, colors = [RED, YELLOW, GREEN, TEAL, BLUE])
        

        self.play(Create(dots), run_time = 1)
        self.wait()

        self.play(
            PhaseFlow(
                function = function, mobject = dots,
            ),
            # Create(field),
            run_time = 10,
            rate_func = linear
        )
        # self.wait(2)



class DropletFlow(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range = (-FRAME_WIDTH, FRAME_WIDTH),
            y_range = (-FRAME_HEIGHT, FRAME_HEIGHT),
            faded_line_ratio = 2
        )
        plane.axes.set_color(GREY_B)
        self.add(plane)

        matrix_function = MathTex(
            "\\begin{bmatrix} \\ x' \\ \\\\ \\ y' \\ \\end{bmatrix} = \\begin{bmatrix} \\ { y } \\ \\\\ \\ { \\mathrm{sin}(2\\pi x) } \\ \\end{bmatrix}"
        )
        matrix_function.scale(1.25)
        matrix_function.set_fill(WHITE, 2)
        matrix_function.to_corner(UL, buff = 0.25)
        self.add_foreground_mobjects(matrix_function)
        matrix_function.add_background_rectangle()

        dots = VGroup()
        for x in range(-20, 20):
            for y in range(-20, 20):
                dots.add(Dot(array([x, y, 0]), color = BLUE))
        
        dots.move_to(ORIGIN)


        function = lambda p: p[1] * RIGHT + sin(2 * pi * p[0]) * UP
        field = ArrowVectorField(function, colors = [RED, YELLOW, GREEN, TEAL, BLUE])
        

        self.play(Create(dots), run_time = 1)
        self.wait()

        self.play(
            PhaseFlow(
                function = function, mobject = dots,
            ),
            # Create(field),
            run_time = 15,
            virtual_time = 2,
            rate_func = linear
        )
        # self.wait(2)
