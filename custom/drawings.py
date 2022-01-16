from manim import *
from custom.functions import *




class SpeechBubble(SVGMobject):
    file_name = get_svg("bubble-speech.svg")  # "Bubbles_speech.svg"
    direction = LEFT
    center_point = ORIGIN
    content_scale_factor = 0.75
    bubble_center_adjustment_factor = 1. / 8

    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_fill(BLACK, 0.8)
        self.set_stroke(WHITE, 3.5)
        self.set_height(5)
        self.set_width(8)
    
    def get_tip(self):
        # TODO, find a better way
        return self.get_corner(DOWN + self.direction) - 0.6 * self.direction

    def get_bubble_center(self):
        factor = self.bubble_center_adjustment_factor
        return self.get_center() + factor * self.get_height() * UP

    def move_tip_to(self, point):
        mover = VGroup(self)
        if self.content is not None:
            mover.add(self.content)
        mover.shift(point - self.get_tip())
        return self

    def flip(self, axis=UP):
        Mobject.flip(self, axis=axis)
        self.refresh_unit_normal()
        self.refresh_triangulation()
        if abs(axis[1]) > 0:
            self.direction = -np.array(self.direction)
        return self

    def pin_to(self, mobject):
        mob_center = mobject.get_center()
        want_to_flip = np.sign(mob_center[0]) != np.sign(self.direction[0])
        can_flip = not self.direction_was_specified
        if want_to_flip and can_flip:
            self.flip()
        boundary_point = mobject.get_bounding_box_point(UP - self.direction)
        vector_from_center = 1.0 * (boundary_point - mob_center)
        self.move_tip_to(mob_center + vector_from_center)
        return self

    def position_mobject_inside(self, mobject):
        scaled_width = self.content_scale_factor * self.get_width()
        if mobject.get_width() > scaled_width:
            mobject.set_width(scaled_width)
        mobject.shift(
            self.get_bubble_center() - mobject.get_center()
        )
        return mobject

    def add_content(self, mobject):
        self.position_mobject_inside(mobject)
        self.content = mobject
        return self.content

    def write(self, *text):
        self.add_content(TexText(*text))
        return self

    def resize_to_content(self):
        target_width = self.content.get_width()
        target_width += max(MED_LARGE_BUFF, 2)
        target_height = self.content.get_height()
        target_height += 2.5 * LARGE_BUFF
        tip_point = self.get_tip()
        self.stretch_to_fit_width(target_width)
        self.stretch_to_fit_height(target_height)
        self.move_tip_to(tip_point)
        self.position_mobject_inside(self.content)

    def clear(self):
        self.add_content(VMobject())
        return self



class ThoughtBubble(SVGMobject):
    file_name = get_svg("bubble-thought.svg")
    direction = LEFT
    center_point = ORIGIN
    content_scale_factor = 0.75
    bubble_center_adjustment_factor = 1. / 8

    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_fill(BLACK, 0.8)
        self.set_stroke(WHITE, 3.5)
        self.set_height(5)
        self.set_width(8)
    
    def get_tip(self):
        # TODO, find a better way
        return self.get_corner(DOWN + self.direction) - 0.6 * self.direction

    def get_bubble_center(self):
        factor = self.bubble_center_adjustment_factor
        return self.get_center() + factor * self.get_height() * UP

    def move_tip_to(self, point):
        mover = VGroup(self)
        if self.content is not None:
            mover.add(self.content)
        mover.shift(point - self.get_tip())
        return self

    def flip(self, axis=UP):
        Mobject.flip(self, axis=axis)
        self.refresh_unit_normal()
        self.refresh_triangulation()
        if abs(axis[1]) > 0:
            self.direction = -np.array(self.direction)
        return self

    def pin_to(self, mobject):
        mob_center = mobject.get_center()
        want_to_flip = np.sign(mob_center[0]) != np.sign(self.direction[0])
        can_flip = not self.direction_was_specified
        if want_to_flip and can_flip:
            self.flip()
        boundary_point = mobject.get_bounding_box_point(UP - self.direction)
        vector_from_center = 1.0 * (boundary_point - mob_center)
        self.move_tip_to(mob_center + vector_from_center)
        return self

    def position_mobject_inside(self, mobject):
        scaled_width = self.content_scale_factor * self.get_width()
        if mobject.get_width() > scaled_width:
            mobject.set_width(scaled_width)
        mobject.shift(
            self.get_bubble_center() - mobject.get_center()
        )
        return mobject

    def add_content(self, mobject):
        self.position_mobject_inside(mobject)
        self.content = mobject
        return self.content

    def write(self, *text):
        self.add_content(TexText(*text))
        return self

    def resize_to_content(self):
        target_width = self.content.get_width()
        target_width += max(MED_LARGE_BUFF, 2)
        target_height = self.content.get_height()
        target_height += 2.5 * LARGE_BUFF
        tip_point = self.get_tip()
        self.stretch_to_fit_width(target_width)
        self.stretch_to_fit_height(target_height)
        self.move_tip_to(tip_point)
        self.position_mobject_inside(self.content)

    def clear(self):
        self.add_content(VMobject())
        return self
       
    
    
class Speaker(SVGMobject):
    file_name = get_svg("speaker.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(1.25)
        self.set_color(WHITE)
        self.set_stroke(WHITE, 2)

        
        
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



class Speedometer(VMobject):
    CONFIG = {
        "arc_angle": 4 * np.pi / 3,
        "num_ticks": 8,
        "tick_length": 0.2,
        "needle_width": 0.1,
        "needle_height": 0.8,
        "needle_color": YELLOW,
    }

    def init_points(self):
        start_angle = np.pi / 2 + self.arc_angle / 2
        end_angle = np.pi / 2 - self.arc_angle / 2
        self.add(Arc(
            start_angle=start_angle,
            angle=-self.arc_angle
        ))
        tick_angle_range = np.linspace(start_angle, end_angle, self.num_ticks)
        for index, angle in enumerate(tick_angle_range):
            vect = rotate_vector(RIGHT, angle)
            tick = Line((1 - self.tick_length) * vect, vect)
            label = Tex(str(10 * index))
            label.set_height(self.tick_length)
            label.shift((1 + self.tick_length) * vect)
            self.add(tick, label)

        needle = Polygon(
            LEFT, UP, RIGHT,
            stroke_width=0,
            fill_opacity=1,
            fill_color=self.needle_color
        )
        needle.stretch_to_fit_width(self.needle_width)
        needle.stretch_to_fit_height(self.needle_height)
        needle.rotate(start_angle - np.pi / 2, about_point=ORIGIN)
        self.add(needle)
        self.needle = needle

        self.center_offset = self.get_center()

    def get_center(self):
        result = VMobject.get_center(self)
        if hasattr(self, "center_offset"):
            result -= self.center_offset
        return result

    def get_needle_tip(self):
        return self.needle.get_anchors()[1]

    def get_needle_angle(self):
        return angle_of_vector(
            self.get_needle_tip() - self.get_center()
        )

    def rotate_needle(self, angle):
        self.needle.rotate(angle, about_point=self.get_center())
        return self

    def move_needle_to_velocity(self, velocity):
        max_velocity = 10 * (self.num_ticks - 1)
        proportion = float(velocity) / max_velocity
        start_angle = np.pi / 2 + self.arc_angle / 2
        target_angle = start_angle - self.arc_angle * proportion
        self.rotate_needle(target_angle - self.get_needle_angle())
        return self


# Probability Mobjects.

class ChessBoard(SVGMobject):
    file_name = get_svg("chess.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(3)



class Heart(SVGMobject):
    file_name = get_svg("heart.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_color(RED)
        self.scale(0.5)



class Diamond(SVGMobject):
    file_name = get_svg("diamond.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_color(RED)
        self.scale(0.5)



class Spade(SVGMobject):
    file_name = get_svg("spade.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_color(WHITE)
        self.scale(0.5)



class Clover(SVGMobject):
    file_name = get_svg("clover.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_color(WHITE)
        self.scale(0.5)
    



class BitCoin(SVGMobject):
    file_name = get_svg("bitcoin.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_color_by_gradient(YELLOW_B, YELLOW_A, YELLOW_A)
        self.set_stroke(GREY_BROWN, 3.5)


# Robot Mobjects.

class Robot(SVGMobject):
    file_name = get_svg("robot.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(2)



class Spybot(SVGMobject):
    file_name = get_svg("spybot.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(2)




        
        
        
        
        
        
        
        
"""
The functions in SpeechBubble & ThoughtBubble
are originally made by 3Blue1Brown, I've made
some modifications in it so that one can use
them in Community Version Manim.
"""
