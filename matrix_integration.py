from manim import *

class Title(ThreeDScene):
    def construct(self):

        circle1 = Circle(radius=1,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2)
        title1 = MathTex("\\alpha").scale(4.5)
        name = Text("aljabrak").to_edge(4*DOWN)
        self.add_fixed_in_frame_mobjects(circle1,title1,name)
        self.play(Create(circle1),Write(title1),Write(name), run_time=5)
        self.wait(2)

        circle2 = Circle(radius=0.25,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2).to_edge(0.5*DOWN+0.7*RIGHT)
        title2 = MathTex("\\alpha").to_edge(0.8*DOWN+0.9*RIGHT)
        self.play(Transform(circle1,circle2),Transform(title1,title2),FadeOut(name),run_time=1)

        label = Text("Matrix Integration \n \t \t and \n Matrix Function.")
        label.set_color(BLUE)
        label.scale(0.7)

        label_eq = MathTex("\\int \\mathbf{A}(t) dt = \\left [ \\int a_{ij}(t) dt \\right ]")
        label_eq.scale(0.8)
        label_eq.next_to(label,2*DOWN)

        title = VGroup(label,label_eq).to_edge(4*UP+4*LEFT)

        self.add_fixed_in_frame_mobjects(title)

        M1 = np.array([
            [1.5, 0, 0],
            [0, 1.5, 0],
            [0, 0, 1.5]
        ])

        M2 = np.array([
            [-1, 2, 0],
            [0, 1, 0],
            [2, 1, 0]
        ])

        axes = ThreeDAxes()
        axes.set_color(GRAY)
        self.set_camera_orientation(phi=55 * DEGREES, theta=-45 * DEGREES)

        self.add(axes)
        self.begin_ambient_camera_rotation(rate=0.2)

        cube = Cube(side_length=1.2, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE)

        self.play(
            Write(title),
            run_time = 5
        )
        self.wait(0.25)

        scale_cube = ApplyMatrix(M1, cube)
        self.play(
            scale_cube,
        )
        self.wait(2)

        cube_to_plane = ApplyMatrix(M2,cube)

        self.play(
            cube_to_plane,
        )
        self.wait(2)

        self.play(
            FadeOut(title),
            run_time = 0.5
        )
        self.wait(0.5)
        self.clear()
        self.set_camera_orientation(phi=55 * DEGREES, theta=-45 * DEGREES)
        circle3 = Circle(radius=0.25,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2).to_edge(0.5*DOWN+0.7*RIGHT)
        title3 = MathTex("\\alpha").to_edge(0.8*DOWN+0.9*RIGHT)
        self.add_fixed_in_frame_mobjects(circle3,title3)
        self.add(circle3,title3)
        self.wait(1)

class MatrixIntegration(Scene):
    def construct(self):
        #LOGO
        circle2 = Circle(radius=0.25,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2).to_edge(0.5*DOWN+0.7*RIGHT)
        title2 = MathTex("\\alpha").to_edge(0.8*DOWN+0.9*RIGHT)
        self.add(circle2,title2)
        self.wait(1)

        matrix_ = Text("What is a Matrix Function?")
        matrix_.scale(0.8)
        
        self.play(
            Write(matrix_),
            run_time = 4
        )
        self.wait(2)

        matrix_func_text = Text("Matrix Function")
        matrix_func_text.set_color(BLUE)
        matrix_func_text.scale(0.8)
        matrix_func_text.to_edge(UP+LEFT)
        matrix_func_def = Tex(r"Let ","$\\mathbf{A}(t) = \\left [ a_{ij}(t) \\right ]$"," be an ",
                            "$n \\cross n$"," matrix""\\\\",
                            "whose entries are all functions of $t$:""\\\\",
                            "$\\mathbf{A}(t)$"," is called a"," Matrix Function",".",
        )
        matrix_func_def.to_edge(2.2*UP+LEFT)

        self.play(
            ReplacementTransform(matrix_,matrix_func_text),
            run_time = 1.5
        )
        self.wait(1)
        self.play(
            Write(matrix_func_def),
            run_time = 5
        )
        self.wait(2)

        matrix_ex0 = MathTex("\\mathbf{A}(t) = \\begin{bmatrix} t^{2} & {1\\over(t+1)}\\\\4 & e^{-t} \\end{bmatrix}")
        matrix_ex1 = MathTex("\\mathbf{B}(t) = \\begin{bmatrix} \\mathrm{sin}(2t) & 0 & 0 \\\\0 & 1 & -t \\\\ 0 & te^{-t^{2}} & {t\\over t^{2}+1} \\end{bmatrix}")
        matrix_ex1.next_to(matrix_ex0,DOWN)
        matrix_equation = VGroup(matrix_ex0,matrix_ex1)

        self.play(
            Write(matrix_equation),
            run_time = 8
        )
        self.wait(2)

        self.play(
            Indicate(matrix_equation,color = BLUE)
        )
        self.wait(2)

        self.play(
            FadeOut(matrix_func_text),
            FadeOut(matrix_func_def),
            FadeOut(matrix_equation),
            run_time = 1
        )
        self.wait(1.5)

        integration_text = Tex(r"The ","integration"," of a ","matrix function""\\\\",
                            " is defined componentwise."
        )
        integration_text.set_color_by_tex('integration',BLUE)
        integration_text.set_color_by_tex('matrix',BLUE)
        
        self.play(
            Write(integration_text),
            run_time = 4
        )
        self.wait(2)

        update = Tex(r"The ","integration"," of a ","matrix function""\\\\",
                            " is defined componentwise."
        ).to_edge(3*UP)
        update.set_color_by_tex('integration',BLUE)
        update.set_color_by_tex('matrix',BLUE)
        self.play(
            Transform(integration_text,update),
        )
        self.wait(1)

        int_eq = MathTex("\\int \\mathbf{A}(t) dt = \\left [ \\int a_{ij}(t) dt \\right ]")
        int_eq.scale(1.2)
        int_eq.next_to(integration_text,3*DOWN)

        self.play(
            Write(int_eq),
            run_time = 5
        )
        self.wait(2)

        box = SurroundingRectangle(int_eq)
        self.play(
            Create(box),
        )
        self.wait()
        self.play(
            FadeOut(box),
            run_time = 1
        )

        matrix1 = MathTex("\\mathbf{A}(t) = \\begin{bmatrix} t^{2} & {1\\over(t+1)}\\\\4 & e^{-t} \\end{bmatrix}").to_edge(5*UP)

        int_eq1 = MathTex("\\int \\mathbf{A}(t) dt")
        int_eq1.scale(1.2)
        int_eq1.next_to(matrix1,2*DOWN)

        self.play(
            ReplacementTransform(integration_text,matrix1),
            ReplacementTransform(int_eq,int_eq1),
            run_time = 1
        )
        self.wait(2)

        int_eq2 = MathTex("\\int \\begin{bmatrix} t^{2} & {1\\over(t+1)}\\\\4 & e^{-t} \\end{bmatrix} dt")
        int_eq2.scale(1.2)
        int_eq2.to_edge(4*UP)

        self.play(
            ReplacementTransform(matrix1,int_eq2),
            FadeOut(int_eq1),
        )
        self.wait(2)

        int_eq3 = MathTex("= \\begin{bmatrix} \\int { t^{2} } dt & \\int { {dt\\over(t+1)} } \\\\ \\\\ \\int {4} dt & \\int { e^{-t} } dt \\end{bmatrix} ")
        int_eq3.scale(1.2)
        int_eq3.next_to(int_eq2,3*DOWN)

        self.play(
            FadeIn(int_eq3),
            run_time = 1
        )
        self.wait(2)

        int_eq4 = MathTex("= \\begin{bmatrix} {t^{3} \\over 3} + c_{1} & \\mathrm{ln}(t+1) + c_{2} \\\\ 4t + c_{3} & -e^{-t} + c_{4} \\end{bmatrix} ")
        int_eq4.scale(1.2)
        int_eq4.next_to(int_eq2,3*DOWN)

        self.play(
            ReplacementTransform(int_eq3,int_eq4),
        )
        self.wait(2)

        int_eq5 = MathTex("= \\begin{bmatrix} {t^{3} \\over 3} & \\mathrm{ln}(t+1) \\\\ 4t & -e^{-t} \\end{bmatrix} ",
                        "+\\begin{bmatrix} c_{1} & c_{2} \\\\ c_{3} & c_{4} \\end{bmatrix}"
        )
        int_eq5.scale(1.2)
        int_eq5.next_to(int_eq2,3*DOWN)

        self.play(
            ReplacementTransform(int_eq4,int_eq5),
        )
        self.wait(2)

        int_eq6 = MathTex("= \\begin{bmatrix} {t^{3} \\over 3} & \\mathrm{ln}(t+1) \\\\ 4t & -e^{-t} \\end{bmatrix} ",
                        "+ \\mathbf{C}"
        )
        int_eq6.scale(1.2)
        int_eq6.next_to(int_eq2,3*DOWN)

        self.play(
            ReplacementTransform(int_eq5,int_eq6),
        )
        self.wait(2)

        self.play(
            FadeOut(int_eq2),
            FadeOut(int_eq6),
            run_time = 1
        )
        self.wait(2)

        book = Text("Book:").to_edge(5*UP)
        book.scale(0.8)
        book_name = Text("Introduction to Linear Algebra. \n \t\t\t\t (8th Ed.) \n \t\t by Bernard Kolman.").next_to(book,DOWN)
        book_name[0:28].scale(0.8)
        book_name[28:].scale(0.5)
        book_name[:28].set_color(YELLOW)
        book_name[38:52].set_color(BLUE)

        self.play(
            FadeIn(book_name),
            FadeIn(book),
            run_time = 4
        )
        self.wait(2)

        self.play(
            FadeOut(book_name),
            FadeOut(book),
        )
        self.wait(2)
