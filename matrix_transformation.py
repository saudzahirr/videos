from manim import *

class LinearTransformation3D(ThreeDScene):
    def create_matrix(self, np_matrix):

        m = Matrix(np_matrix)
        m.scale(0.5)
        m.to_corner(UP + LEFT)

        return m

    def construct(self):

        #LOGO
        circle1 = Circle(radius=1,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2)
        title1 = MathTex("\\alpha").scale(4.5)
        name = Text("aljabrak").to_edge(4*DOWN)
        self.add_fixed_in_frame_mobjects(circle1,title1,name)
        self.play(Create(circle1),Write(title1),Write(name), run_time=5)
        self.wait(2)

        circle2 = Circle(radius=0.25,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2).to_edge(0.5*DOWN+0.7*RIGHT)
        title2 = MathTex("\\alpha").to_edge(0.8*DOWN+0.9*RIGHT)
        self.play(Transform(circle1,circle2),Transform(title1,title2),FadeOut(name),run_time=1)

        #Shear Matrix.
        S = np.array([
            [1, 0, 1],
            [0, 1, 2],
            [0, 0, 1]
        ])

        axes = ThreeDAxes()
        axes.set_color(GRAY)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        #Matrix
        matrix = self.create_matrix(S)
        self.add_fixed_in_frame_mobjects(matrix)
        self.play(
            FadeIn(matrix),
            run_time=1,
        )

        #Axes & Camera Motion.
        self.add(axes)
        self.begin_ambient_camera_rotation(rate=0.2)

        cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE)

        self.play(
            Create(cube)
        )

        self.wait()

        shear = ApplyMatrix(S, cube)

        self.play(
            shear
        )

        self.wait(2)

        exp = Tex(r"This is Shear Transformation","\\\\",
                    "in 3 Dimensional space"
        ).to_edge(UP+LEFT)
        exp[8:27].set_color(BLUE)
        eq = MathTex("S_{z} = \\begin{pmatrix} 1 & 0 & k_{1} \\\\ 0 & 1 & k_{2} \\\\ 0 & 0 & 1 \\end{pmatrix} ")
        eq.next_to(exp,DOWN)
        self.add_fixed_in_frame_mobjects(exp,eq)
        self.play(
            Write(exp),
            ReplacementTransform(matrix,eq),
            run_time=1,
        )
        self.wait(3)
