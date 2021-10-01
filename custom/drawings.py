class SpeechBubble(SVGMobject):
    file_name = "Bubbles_speech.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_fill(BLACK, 0.8)
        self.set_stroke(WHITE, 3.5)
        self.set_height(5)
        self.set_width(8)



class ThoughtBubble(SVGMobject):
    file_name = "Bubbles_thought.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_fill(BLACK, 0.8)
        self.set_stroke(WHITE, 3.5)
        self.set_height(5)
        self.set_width(8)
        

# Optical Mobjects.

class ConvexLens(Arc):
    def generate_points(self):
        arc_1 = Arc(radius = 2, angle = np.pi/2)
        arc_2 = Arc(radius = 2, angle = np.pi/2)
        arc_2.rotate(np.pi)
        arc_1.rotate(-np.pi/4)
        arc_2.rotate(-np.pi/4)

        self.append_points(arc_1.points)
        self.append_points(arc_2.points)
        self.move_to(ORIGIN)
        self.set_color(BLUE_B)



class ConcaveLens(VMobject):
    def generate_points(self):
        line_up = Line(start=np.array([-0.5, 1, 0]), end=np.array([0.5, 1, 0]))

        arc_1 = ArcBetweenPoints(start=np.array([0.5, 1, 0]),
                                              end=np.array([0.5, -1, 0]),
                                              angle=TAU / 6)

        line_down = Line(start=np.array([0.5, -1, 0]), end=np.array([-0.5, -1, 0]))

        arc_2 = ArcBetweenPoints(start=np.array([-0.5, -1, 0]),
                                              end=np.array([-0.5, 1, 0]),
                                              angle=TAU / 6)

        self.append_points(line_up.points)
        self.append_points(arc_1.points)
        self.append_points(line_down.points)
        self.append_points(arc_2.points)
        self.add(line_up, arc_1, line_down, arc_2)
        self.move_to(ORIGIN)
        self.set_color(BLUE_B)


# Probability Mobjects.

class ChessBoard(SVGMobject):
    file_name = "chess.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(3)



class Heart(SVGMobject):
    file_name = "heart.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_color(RED)
        self.scale(0.5)



class Diamond(SVGMobject):
    file_name = "diamond.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_color(RED)
        self.scale(0.5)



class Spade(SVGMobject):
    file_name = "spade.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_color(WHITE)
        self.scale(0.5)



class Clover(SVGMobject):
    file_name = "clover.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_color(WHITE)
        self.scale(0.5)
    



class BitCoin(SVGMobject):
    file_name = "bitcoin.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_color_by_gradient(YELLOW_B, YELLOW_A, YELLOW_A)
        self.set_stroke(GREY_BROWN, 3.5)


# Robot Mobjects.

class Robot(SVGMobject):
    file_name = "robot.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(2)



class Spybot(SVGMobject):
    file_name = "spybot.svg"
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(2)




class ExternallyAnimatedScene(Scene):
    pass
