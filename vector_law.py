from manim import *

class VectorLaw(Scene):
  def construct(self):
    vector1 = Arrow(tip_length=0.3,stroke_width=4,start = ORIGIN,end = np.array([1,2,0])).scale(1.3).set_color(PURPLE_B)
        vector2 = Arrow(tip_length=0.3,stroke_width=4,start = ORIGIN,end = np.array([2,-1,0])).scale(1.3).set_color(PINK)
        vector3 = Arrow(tip_length=0.3,stroke_width=4,start = ORIGIN,end = np.array([3,1,0])).scale(1.2).set_color(RED_E)
        vector4 = Arrow(tip_length=0.3,stroke_width=4,start = np.array([2,-1,0]),end = np.array([3,1,0])).scale(1.3).set_color(PURPLE_B)

        self.play(Create(vector1))
        self.play(Create(vector2))
        self.wait()
        self.play(Create(vector3))
        self.wait(2)
        self.play(Transform(vector1,vector4))
        self.wait(3)
