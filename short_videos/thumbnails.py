from manimce import *


class MatrixIntegration(ThreeDScene):
    def construct(self):
        title = Tex("Matrix Integration")
        title.scale(2.5)
        self.add_fixed_in_frame_mobjects(title)
        self.add_foreground_mobject(title)
        M = np.array([
            [-1, 2, 0],
            [0, 1, 0],
            [2, 1, 0]
        ])

        axes = ThreeDAxes()
        axes.set_color(GREY_D)
        axes.scale(2)
        self.set_camera_orientation(phi=55 * DEGREES, theta=-45 * DEGREES)

        self.add(axes)
        self.begin_ambient_camera_rotation(rate=0.2)

        cube = Cube(side_length=1.5, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE)
        cube.scale(2)

        cube_to_plane = ApplyMatrix(M, cube)

        self.play(
            cube_to_plane,
        )

        
class EulerIdentity(Scene):
    def construct(self):
        grid = ComplexPlane(x_range = [-100, 100], y_range = [-100, 100])
        plane = grid.copy()
        plane.set_color(GREY_E)
        grid.rotate_about_origin(30 * DEGREES)
        equation = MathTex(
            "e^{", "v", "\\sqrt{-1}}", "=", "\\mathrm{cos}", ".", "v", "+", "\\sqrt{-1}", "\\cdot", "\\mathrm{sin}", ".", "v"
        )
        #equation.set_color(BLUE_B)
        equation.set_color_by_tex('v', BLUE_D)
        equation.set_color_by_tex('\\sqrt{-1}', YELLOW)
        equation.set_color_by_tex('=', BLUE_A)
        equation.set_color_by_tex('+', BLUE_A)
        equation.set_color_by_tex('.', BLUE_A)
        equation.scale(2.25)
        equation.add_background_rectangle()
        self.add(plane, grid)
        self.add_foreground_mobject(equation)

        
        
class GoldenRatio(Scene):
    def construct(self):
        ptolemy = ImageMobject("ptolemy.png")
        ptolemy.shift(5 * DOWN)
        ptolemy.scale(1.5)
        ptolemy.fade(0.8)
        equation = MathTex(
            "{\\mathrm{BD} \\over \\mathrm{AD}} = { {1 + \\sqrt{5} } \\over 2}"
        )
        equation.scale(1.5)
        equation.set_color(BLUE)
        equation.to_edge(UP)
        circle = Circle(color = WHITE)
        pentagon = RegularPolygon(n = 5, color = GREY)
        point = pentagon.get_vertices()
        line_1 = Line(start = point[1], end = point[4], color = GREY)
        line_2 = Line(start = point[2], end = point[4], color = YELLOW)
        line_3 = Line(start = point[1], end = point[3], color = YELLOW)
        phi = MathTex("\\varphi")
        phi.set_color(BLUE_B)
        phi.scale(3)
        phi.to_edge(2 * RIGHT)
        phi.shift(1.75 * UP)
        coord_label = VGroup(
            Tex(r"D").scale(0.5).next_to(point[1], 0.5*LEFT),
            Tex(r"A").scale(0.5).next_to(point[2], 0.5*LEFT + 0.5*DOWN),
            Tex(r"B").scale(0.5).next_to(point[3], 0.5*RIGHT + 0.5*DOWN),
            Tex(r"C").scale(0.5).next_to(point[4], 0.5*RIGHT)
        )
        circle.add(pentagon, line_1, line_2, line_3, coord_label)
        circle.scale(2.25)
        circle.next_to(equation, 2 * DOWN)
        self.add(ptolemy)
        self.add_foreground_mobjects(equation, circle, phi)

        
        
class HammingCodes(Scene):
    def construct(self):
        title = Tex(r"Hamming Codes")
        title.scale(2.5)
        title.to_edge(UP)
        punchcard = SVGMobject("punchcard_relay.svg")
        punchcard.scale(2)
        punchcard.set_opacity(0.5)
        punchcard.next_to(title, 3 * DOWN)
        punchcard[3:7].set_fill(GREY_E, opacity = 2)
        cover = ImageMobject("computer_science.jpg")
        cover.scale(1.5)
        cover.fade(0.6)
        self.add(cover)
        self.add_foreground_mobjects(title, punchcard)

        
        
class AngleIdentity(Scene):
    def construct(self):
        background_image = ImageMobject("angle_identity.png")
        background_image.scale(1.2)
        background_image.fade(0.3)
        self.add(background_image)

        equation = MathTex(
            "\\mathrm{cos}^{", "2}", "(", "\\theta", ")", "=", "{1 \\over 2}", "+", "{1 \\over 2}", "{\\mathrm{cos}", "(", "2", "\\theta", ")}"
        )
        equation.set_color_by_tex('\\mathrm{cos}', DARK_GREY)
        equation.set_color_by_tex('2', DARK_PINK)
        equation.set_color_by_tex('{1 \\over 2}', YELLOW)
        equation.set_color_by_tex('=', BLUE_A)
        equation.set_color_by_tex('+', BLUE_A)
        equation.set_color_by_tex('(', MELON)
        equation.set_color_by_tex(')', MELON)
        equation.set_color_by_tex('\\theta', BLUE_C)
        equation.scale(2.65)
        equation.add_background_rectangle()
        self.add_foreground_mobjects(equation)s
