from manim import *

class PascalTriangle(Scene):
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

        text = Tex(
            r"Pascal's Triangle"
        ).to_edge(UP).set_color(BLUE)
        self.play(Write(text))
        
        row1 = Text("1").to_edge(3*UP).scale(0.6)
        row2 = Text("1 \t 1").next_to(row1,DOWN).scale(0.6)
        row3 = Text("1 \t 2 \t 1").next_to(row2,DOWN).scale(0.6)
        row4 = Text("1 \t 3 \t 3 \t 1").next_to(row3,DOWN).scale(0.6)
        row5 = Text("1 \t 4 \t 6 \t 4 \t 1").next_to(row4,DOWN).scale(0.6)
        row6 = Text("1 \t 5 \t 10 \t 10 \t 5 \t 1").next_to(row5,DOWN).scale(0.6)
        row7 = Text("1 \t 6 \t 15 \t 20 \t 15 \t 6 \t 1").next_to(row6,DOWN).scale(0.6)
        row8 = Text("1 \t 7 \t 21 \t 35 \t 35 \t 21 \t 7 \t 1").next_to(row7,DOWN).scale(0.6)

        self.play(FadeIn(row1), 
                FadeIn(row2),
                FadeIn(row3),
                FadeIn(row4),
                FadeIn(row5),
                FadeIn(row6),
                FadeIn(row7),
                FadeIn(row8), 
                lag_ratio=0.3,run_time=3 
        )

        self.wait()
        self.play(FadeOut(row1), 
                FadeOut(row2),
                FadeOut(row3),
                FadeOut(row4),
                FadeOut(row5),
                FadeOut(row6),
                FadeOut(row7),
                FadeOut(row8), 
                run_time=0.5 
        )

        #binomial theorem.
        
        binomial = Tex(r"Binomial Theorem").set_color(BLUE).to_edge(UP)
        binomial_theorem = MathTex("(a+b)^{n} = \\sum_{k=0}^{n} \\binom{n}{k}a^{n-k}b^{k}").to_edge(5*UP).scale(1.2)
        frame = SurroundingRectangle(binomial_theorem,color=TEAL)
        eq2 = MathTex("a \\ + \\ b").to_edge(3*UP)
        eq3 = MathTex("a^{2} \\ + \\  2ab \\ + \\ b^{2}").next_to(eq2,DOWN)
        eq4 = MathTex("a^{3} \\ + \\  3a^{2}b \\ + \\ 3ab^{2} \\ + \\ b^{3}").next_to(eq3,DOWN)
        eq5 = MathTex("a^{4} \\ + \\  4a^{3}b \\ + \\ 6a^{2}b^{2} \\ + \\ 4ab^{3} \\ + \\ b^{4}").next_to(eq4,DOWN)
        eq6 = MathTex("a^{5} \\ + \\  5a^{4}b \\ + \\ 10a^{3}b^{2} \\ + \\ 10a^{2}b^{3} \\ + \\ 4ab^{4} \\ + \\ b^{5}").next_to(eq5,DOWN)
        eq7 = MathTex("a^{6} \\ + \\  6a^{5}b \\ + \\ 15a^{4}b^{2} \\ + \\ 20a^{3}b^{3} \\ + \\ 15a^{2}b^{4} \\ + \\ 6ab^{5} \\ + \\ b^{6}").next_to(eq6,DOWN)
        eq8 = MathTex("a^{7} \\ + \\  7a^{6}b \\ + \\ 21a^{5}b^{2} \\ + \\ 35a^{4}b^{3} \\ + \\ 35a^{3}b^{4} \\ + \\ 21a^{2}b^{5} \\ + \\ 7ab^{6} \\ + \\ b^{7}").next_to(eq7,DOWN)
        
        theorem = VGroup(eq2, eq3, eq4, eq5, eq6, eq7, eq8)
        theorem.scale(0.85)

        self.play(
            ReplacementTransform(text,binomial)
        )
        self.play(Write(binomial_theorem),run_time=3)
        self.wait(1)
        self.play(Create(frame))
        self.wait(0.25)
        self.play(FadeOut(frame),run_time=1)
        self.wait(1)
        self.play(FadeOut(binomial_theorem))
        self.wait(1)

        self.play(
            Write(theorem),
            run_time=10
        )
        self.wait()

        see = Tex(r"See the coefficients","\\\\"
                " of Binomial Theorem","\\\\"
                "are numbers of","\\\\" 
                "Pascal's Triangle!").set_color(YELLOW).to_edge(UP+RIGHT).scale(0.75)
        self.play(Write(see),
                run_time=6
        )
        self.wait(2)
        self.play(FadeOut(see),run_time=0.5)
        self.wait(1)
        self.play(FadeOut(theorem),FadeOut(binomial))
        self.wait(2)
