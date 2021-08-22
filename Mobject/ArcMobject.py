from manim import *


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
        self.set_color(BLUE_A)
