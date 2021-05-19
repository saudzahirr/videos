from manim import *

class MatrixTransformation(ThreeDScene):
    def create_matrix(self, np_matrix):

        m = Matrix(np_matrix)
        m.scale(0.7)
        m.to_corner(UP + LEFT)

        return m

    def construct(self):
        
        #Shear Matrix.
        S = np.array([
            [1, 0, 1],
            [0, 1, 2],
            [0, 0, 1]
        ])

        axes = ThreeDAxes()
        axes.set_color(GRAY)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        #Axes & Camera Motion.
        self.add(axes)
        self.begin_ambient_camera_rotation(rate=0.2)

        cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE)

        #Matrix
        matrix = self.create_matrix(S)
        self.add_fixed_in_frame_mobjects(matrix)

        self.play(
            Create(cube),
            Write(matrix),
            run_time=1,
        )

        self.wait()

        shear = ApplyMatrix(S, cube)

        self.play(
            shear
        )

        self.wait(2)

        eq = MathTex("S_{z} = \\begin{bmatrix} 1 & 0 & k_{1} \\\\ 0 & 1 & k_{2} \\\\ 0 & 0 & 1 \\end{bmatrix} ")
        eq.to_edge(UP+LEFT)
        self.add_fixed_in_frame_mobjects(eq)
        exp = Tex(r"This is ","Shear Transformation""\\\\",
                    " in ","3-Dimensional Space."
        ).next_to(matrix,DOWN)
        exp.set_color_by_tex('Shear Transformation',BLUE)
        exp.set_color_by_tex('3-Dimensional Space.',YELLOW)
        exp.to_edge(LEFT+4*DOWN)
        self.play(
            Write(exp),
            run_time=2
        )
        self.add_fixed_in_frame_mobjects(exp)
        self.play(
            ReplacementTransform(matrix,eq),
            run_time=0.25,
        )
        self.wait(3)
