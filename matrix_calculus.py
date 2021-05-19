from manim import *

class MatrixIntegration(Scene):
    def construct(self):
      
        label = Text("Matrix Integration \n \t \t and \n Matrix Function.")
        label.set_color(BLUE)
        label.scale(0.8)
        label.to_edge(4*UP)

        label_eq = MathTex("\\int \\mathbf{A}(t) dt = \\left [ \\int a_{ij}(t) dt \\right ]")
        label_eq.scale(1.2)
        label_eq.next_to(label,2*DOWN)

        self.play(
            FadeIn(label),
            Write(label_eq),
            run_time = 2
        )
        self.wait(2)

        matrix_ = Text("What is a Matrix Function?")
        matrix_.scale(0.8)
        
        self.play(
            FadeOut(label_eq),
            ReplacementTransform(label,matrix_),
            run_time = 1
        )
        self.wait(2)

        matrix_func_text = Text("Matrix Function")
        matrix_func_text.set_color(BLUE)
        matrix_func_text.scale(0.8)
        matrix_func_text.to_edge(UP+LEFT)
        matrix_func_def = Tex(r"Let ","$\\mathbf{A}(t) = \\left [ a_{ij}(t) \\right ]$"," be an ",
                            "$n \\cross n$"," matrix""\\\\",
                            "whose entries are all functions of $t$:""\\\\",
                            "$\\mathbf{Q}(t)$"," is called a"," Matrix Function",".",
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
        matrix_ex1 = MathTex("\\mathbf{A}(t) = \\begin{bmatrix} \\mathrm{sin}(2t) & 0 & 0 \\\\0 & 1 & -t \\\\ 0 & te^{-t^{2}} & {t\\over t^{2}+1} \\end{bmatrix}")
        matrix_ex1.next_to(matrix_ex0,DOWN)
        matrix_equation = VGroup(matrix_ex0,matrix_ex1)

        self.play(
            Write(matrix_equation),
            run_time = 5
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
            run_time = 0.5
        )
        self.wait(2)
