from manim import *

class LinearTransformation(LinearTransformationScene):

    def construct(self):
        
        vector1 = Vector([1,2])
        vector1.set_color(RED_B)
        vtext1 = MathTex("\\vec{u}").next_to(vector1,UP)
        vector2 = Vector([2,-1])
        vector2.set_color(GREEN_B)
        vtext2 = MathTex("\\vec{v}").next_to(vector2,DOWN)
        vector3 = Vector([3,1])
        vector3.set_color(YELLOW)
        resultant = MathTex("\\vec{w} = \\vec{u} + \\vec{v}").next_to(vector3,RIGHT)
        
        matrix = [[1, 3], [0, 1]]

        self.add_vector(vector1)
        self.add_vector(vector2)
        self.play(Write(vtext1),Write(vtext2),run_time=1)
        self.add_vector(vector3)
        self.play(Write(resultant))
        self.wait(3)
        self.play(FadeOut(vtext1),FadeOut(vtext2),FadeOut(resultant),run_time=0.1)

        ex = Text("Applying Shear Transformation").scale(0.7).to_edge(UP)
        self.play(Write(ex),run_time=2)
        self.wait()
        self.play(Uncreate(ex),run_time=0.1)

        self.apply_matrix(matrix)

        text1 = Text("Shear Matrix").to_edge(UP+LEFT).scale(0.7).set_color(BLUE)
        rotation = MathTex("\\begin{bmatrix}1 & 3\\\\0 & 1 \\end{bmatrix}").to_edge(2.2*UP+4*LEFT).scale(1.1)
        b1 = BackgroundRectangle(text1)
        b2 = BackgroundRectangle(rotation)
        self.add(b1,b2)
        self.play(Write(text1),Write(rotation),run_time=2)

        self.wait()
