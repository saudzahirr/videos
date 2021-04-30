from manim import *

class CubicFormula(Scene):
    def construct(self):
        #LOGO
        circle1 = Circle(radius=1,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2)
        title1 = MathTex("\\alpha").scale(4.5)
        name = Text("aljabrak").to_edge(4*DOWN)
        self.play(Create(circle1),Write(title1),Write(name), run_time=5)
        self.wait(2)

        circle2 = Circle(radius=0.25,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2).to_edge(0.5*DOWN+0.7*RIGHT)
        title2 = MathTex("\\alpha").to_edge(0.8*DOWN+0.9*RIGHT)
        self.play(Transform(circle1,circle2),Transform(title1,title2),FadeOut(name),run_time=1)


        text1 = Text("You all are familiar with the quadratic equation!"
                    "\n" 
                    "and its formula...").scale(0.7)
        text2 = Text("But do you know there is a formula"
                    "\n"
                    "for cubic equation too!").scale(0.7)
        text3 = Text("Known as Cardan's Formula!").scale(0.7)
        text3[7:23].set_color(BLUE)
        text4 = Text("In this video we will see how to solve a cubic equation.").scale(0.7)
        self.play(Write(text1),run_time=3)
        self.wait(3)
        self.play(ReplacementTransform(text1,text2),run_time=1)
        self.wait(3)
        self.play(ReplacementTransform(text2,text3),run_time=1)
        self.wait(3)
        self.play(ReplacementTransform(text3,text4),run_time=1)
        self.wait(3)
        self.play(FadeOut(text4),run_time=0.3)

        
        eq1 = MathTex("ax^{2} + bx + c = 0").to_edge(DOWN+3.8*LEFT)
        name1 = Text("Quadratic Equation").to_edge(2*DOWN+LEFT).scale(0.5)

        eq2 = MathTex("x^{3} + px + q = 0").to_edge(DOWN+2.8*LEFT)
        name2 = Text("Cubic Equation").to_edge(2*DOWN+LEFT).scale(0.5)

        quadratic = FunctionGraph(
            lambda x : x**2+2*x+1
        )
        quadratic.set_color(YELLOW)

        cubic = FunctionGraph(
            lambda x : x**3-3*x+1
        )
        cubic.set_color(ORANGE)

        grid = NumberPlane()

        self.play(Create(grid))
        self.play(Create(quadratic),Write(eq1),Write(name1), run_time=3)
        self.wait(3)
        self.play(Transform(quadratic,cubic),Transform(eq1,eq2),Transform(name1,name2), run_time=2)
        self.wait(3)
        self.play(FadeOut(grid),FadeOut(quadratic),FadeOut(cubic),FadeOut(eq1),FadeOut(eq2),FadeOut(name1),FadeOut(name2),run_time=0.3)
        self.wait(2)

        history = Text("Gerolamo Cardano, the first mathematician""\n""to use 'negative numbers'.""\n"
                "He published the solution of""\n""a cubic equation of form:"
                ).scale(0.7)
        history[0:16].set_color(BLUE)
        history[41:58].set_color(BLUE)
        cardano = MathTex("x^{3} + px + q = 0").to_edge(5*DOWN)
        ted = MathTex("x = \\sqrt[3]{ -\\frac{ q }{ 2 } + \\sqrt{ {\\frac{ q }{ 4 } }^{2} + {\\frac{ p }{ 27 } }^{3} } } + \\sqrt[3]{ -\\frac{ q }{ 2 } - \\sqrt{ {\\frac{ q }{ 4 } }^{2} + {\\frac{ p }{ 27 } }^{3} } }").to_edge(5*DOWN)
        cardan = ImageMobject("Cardan").to_edge(UP+LEFT)
        self.play(FadeIn(cardan),Write(history),run_time=8)
        self.play(Write(cardano),run_time=3)
        self.wait(2)
        self.play(FadeOut(cardan),FadeOut(history),FadeOut(cardano),run_time=1)
        ted2 = cardano.to_edge(2*UP)
        ted3 = Text("where Cardan's Formula is;").to_edge(5*UP).scale(0.5)
        ted3[5:20].set_color(BLUE)
        self.play(Write(ted2),Write(ted3),Write(ted),run_time=8)
        self.wait(2)
        self.play(FadeOut(ted3),run_time=0.3)
        text5 = Text("See the similarity and symmetry!").scale(0.5).to_edge(5.5*UP).set_color_by_gradient(YELLOW)
        self.play(FadeIn(text5),run_time=1.2)
        self.wait(2)
        quad = MathTex("ax^{2} + bx + c = 0").to_edge(3*UP)
        equa = MathTex("x = \\frac{ -b \\pm \\sqrt{ b^{2} - 4ac } }{2a}").to_edge(5*DOWN)
        self.wait(2)
        self.play(ReplacementTransform(ted2,quad),ReplacementTransform(ted,equa),run_time=1.5)
        self.wait(2)
        ted3 = MathTex("x^{3} + px + q = 0").to_edge(5*DOWN).to_edge(3*UP)
        ted1 = MathTex("x = \\sqrt[3]{ -\\frac{ q }{ 2 } + \\sqrt{ {\\frac{ q }{ 4 } }^{2} + {\\frac{ p }{ 27 } }^{3} } } + \\sqrt[3]{ -\\frac{ q }{ 2 } - \\sqrt{ {\\frac{ q }{ 4 } }^{2} + {\\frac{ p }{ 27 } }^{3} } }").to_edge(5*DOWN)
        self.play(ReplacementTransform(quad,ted3),ReplacementTransform(equa,ted1),run_time=1.5)
        self.wait(3)
        self.play(FadeOut(text5),FadeOut(ted3),FadeOut(ted1))
