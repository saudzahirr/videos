from manim import *
from itertools import *

# Circuit Mobjects.

class Resistor(Line):
    def __init__(self, **kwargs):
        Line.__init__(self, **kwargs)
        midpoints = [
            interpolate(self.start, self.end, alpha)
            for alpha in [0.25]+list(np.arange(0.3, 0.71, 0.1))+[0.75]
        ]
        perp = rotate_vector(self.end-self.start, np.pi/2)
        for midpoint, n in zip(midpoints[1:-1], count()):
            midpoint += 0.1*((-1)**n)*perp
        points = [self.start]+midpoints+[self.end]
        self.set_points_as_corners(points)



class LongResistor(SVGMobject):
    file_name = "resister.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.25)
        self.set_stroke(WHITE, 4)



class Inductor(SVGMobject):
    file_name = "inductor.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.25)
        self.set_stroke(WHITE, 4)

    

class Capacitor(SVGMobject):
    file_name = "capacitor.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_stroke(WHITE, 4)



class Transformer(Inductor):
    def __init__(self, **kwargs):
        Inductor.__init__(self, **kwargs)
        self.rotate(90*DEGREES)
        self.flip(UP)
        self.add(Line().scale(2).rotate(90*DEGREES).shift(0.75*RIGHT))
        self.add(Dot(self.get_top()).shift(0.5*DOWN))
        self.shift(1.5*LEFT)
        copy = self.copy()
        copy.flip(UP)
        copy.shift(1.5*RIGHT)
        self.add(copy)



class Source(VMobject):
   def __init__(self, **kwargs):
        VMobject.__init__(self, **kwargs)
        self.add(Circle(color = self.color))
        self.add(Tex("$+$").scale(1.5).set_color(GREEN).shift(0.5*UP))
        self.add(Tex("$-$").scale(1.5).set_color(RED).shift(0.5*DOWN))
        self.set_height(1)        
        self.add(Line(self.get_top(), self.get_top()+UP))
        self.add(Line(self.get_bottom(), self.get_bottom()+DOWN))



class EarthGround(SVGMobject):
    file_name = "earth_ground.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.5)
        self.set_stroke(WHITE, 4)



class SignalGround(SVGMobject):
    file_name = "signal_ground.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.5)
        self.set_stroke(WHITE, 4)



class ChassisGround(SVGMobject):
    file_name = "chassis_ground.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.5)
        self.set_stroke(WHITE, 4)



class Diode(SVGMobject):
    file_name = "diode.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.5)
        self.set_stroke(WHITE, 4)



class ZenerDiode(SVGMobject):
    file_name = "zener_diode.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.5)
        self.set_stroke(WHITE, 4)



class NPN(SVGMobject):
    file_name = "NPN.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.5)
        self.set_stroke(WHITE, 4)



class Buffer(SVGMobject):
    file_name = "buffer.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.5)
        self.set_stroke(WHITE, 4)



class NotGate(SVGMobject):
    file_name = "not.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.5)
        self.set_stroke(WHITE, 4)



class OrGate(SVGMobject):
    file_name = "or.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.5)
        self.set_stroke(WHITE, 4)
        


class AndGate(SVGMobject):
    file_name = "and.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.5)
        self.set_stroke(WHITE, 4)



class NorGate(SVGMobject):
    file_name = "nor.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.5)
        self.set_stroke(WHITE, 4)



class NandGate(SVGMobject):
    file_name = "nand.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.5)
        self.set_stroke(WHITE, 4)



class XorGate(SVGMobject):
    file_name = "xor.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.5)
        self.set_stroke(WHITE, 4)



class XnorGate(SVGMobject):
    file_name = "xnor.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.5)
        self.set_stroke(WHITE, 4)



        
        
        
        
        
        
