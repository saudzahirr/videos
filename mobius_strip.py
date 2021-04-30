from manim import *

class ThreeD(ThreeDScene):
    def construct(self):

        circle2 = Circle(radius=0.25,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2).to_edge(0.5*DOWN+0.7*RIGHT)
        title2 = MathTex("\\alpha").to_edge(0.8*DOWN+0.9*RIGHT)

        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=120 * DEGREES)
        
        strip = Text("Mobius Strip").to_edge(UP+LEFT).scale(0.7).set_color(BLUE)
        equation = MathTex("\\begin{bmatrix} x(u,v) \\\\ y(u,v) \\\\ z(u,v) \\end{bmatrix} = \\begin{bmatrix} \\{ 1+\\frac{u}{2}cos(\\frac{v}{2}) \\} cos(v) \\\\ \\{ 1+\\frac{u}{2}cos(\\frac{v}{2}) \\} sin(v) \\\\ \\frac{u}{2}sin(\\frac{v}{2})  \\end{bmatrix} ").to_edge(2.2*UP+LEFT)
        mobius = ParametricSurface(
            lambda s , t : np.array([ (1+(s/2)*np.cos(t/2))*np.cos(t) , (1+(s/2)*np.cos(t/2))*np.sin(t) , (s/2)*np.sin(t/2) ])
            , v_max=TAU , resolution=(10,30) , checkerboard_colors=[MAROON_A,MAROON_C] ,
        )
        self.add_fixed_in_frame_mobjects(circle2)
        self.add_fixed_in_frame_mobjects(title2)

        mobius.to_edge(5*DOWN)
        self.play(Create(mobius), run_time=2)
        self.add_fixed_in_frame_mobjects(strip)
        self.add_fixed_in_frame_mobjects(equation)
        self.wait(3)
