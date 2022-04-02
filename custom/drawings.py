from manim import *
from custom.functions import *




class Brain(SVGMobject):
    file_name = get_svg("brain.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.85)
        self.set_color(GREY_B)
        self.set_stroke(GREY_D, 2)



class Coins(SVGMobject):
    file_name = get_svg("coins.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(0.5)



class Speaker(SVGMobject):
    file_name = get_svg("speaker.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(1.25)
        self.set_color(WHITE)
        self.set_stroke(WHITE, 2)



class BitCoin(SVGMobject):
    file_name = get_svg("bitcoin.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_color_by_gradient(YELLOW_B, YELLOW_A, YELLOW_A)
        self.set_stroke(GREY_BROWN, 3.5)



class Robot(SVGMobject):
    file_name = get_svg("robot.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(2)



class Piano(VGroup):
    n_white_keys = 52
    black_pattern = [0, 2, 3, 5, 6]
    white_keys_per_octave = 7
    white_key_dims = (0.15, 1.0)
    black_key_dims = (0.1, 0.66)
    key_buff = 0.02
    white_key_color = WHITE
    black_key_color = GREY_E
    total_width = 13

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_white_keys()
        self.add_black_keys()
        self.sort_keys()
        self[:-1].reverse_points()
        self.set_width(self.total_width)

    def add_white_keys(self):
        key = Rectangle(*self.white_key_dims)
        key.set_fill(self.white_key_color, 1)
        key.set_stroke(width=0)
        self.white_keys = key.get_grid(1, self.n_white_keys, buff=self.key_buff)
        self.add(*self.white_keys)

    def add_black_keys(self):
        key = Rectangle(*self.black_key_dims)
        key.set_fill(self.black_key_color, 1)
        key.set_stroke(width=0)

        self.black_keys = VGroup()
        for i in range(len(self.white_keys) - 1):
            if i % self.white_keys_per_octave not in self.black_pattern:
                continue
            wk1 = self.white_keys[i]
            wk2 = self.white_keys[i + 1]
            bk = key.copy()
            bk.move_to(midpoint(wk1.get_top(), wk2.get_top()), UP)
            big_bk = bk.copy()
            big_bk.stretch((bk.get_width() + self.key_buff) / bk.get_width(), 0)
            big_bk.stretch((bk.get_height() + self.key_buff) / bk.get_height(), 1)
            big_bk.move_to(bk, UP)
            for wk in wk1, wk2:
                wk.become(Difference(wk, big_bk).match_style(wk))
            self.black_keys.add(bk)
        self.add(*self.black_keys)

    def sort_keys(self):
        self.sort(lambda p: p[0])



class Clock(VGroup):
    def __init__(self, **kwargs):
        circle = Circle(color=WHITE)
        ticks = []
        for x in range(12):
            alpha = x / 12.
            point = complex_to_R3(
                np.exp(2 * np.pi * alpha * complex(0, 1))
            )
            length = 0.2 if x % 3 == 0 else 0.1
            ticks.append(
                Line(point, (1 - length) * point)
            )
        self.hour_hand = Line(ORIGIN, 0.3 * UP)
        self.minute_hand = Line(ORIGIN, 0.6 * UP)

        VGroup.__init__(
            self, circle,
            self.hour_hand, self.minute_hand,
            *ticks
        )


class ClockPassesTime(Animation):
    run_time = 5
    hours_passed = 12
    rate_func = linear

    def __init__(self, clock, **kwargs):
        assert(isinstance(clock, Clock))
        rot_kwargs = {
            "axis": OUT,
            "about_point": clock.get_center()
        }
        hour_radians = -self.hours_passed * 2 * np.pi / 12
        self.hour_rotation = Rotating(
            clock.hour_hand,
            angle=hour_radians,
            **rot_kwargs
        )
        self.hour_rotation.begin()
        self.minute_rotation = Rotating(
            clock.minute_hand,
            angle=12 * hour_radians,
            **rot_kwargs
        )
        self.minute_rotation.begin()
        Animation.__init__(self, clock, **kwargs)

    def interpolate_mobject(self, alpha):
        for rotation in self.hour_rotation, self.minute_rotation:
            rotation.interpolate_mobject(alpha)



class Speedometer(VMobject):
    def generate_points(self):
        arc_angle = 4 * np.pi / 3
        num_ticks = 8
        tick_length = 0.2
        needle_width = 0.1
        needle_height = 0.8
        needle_color = YELLOW
        
        start_angle = np.pi / 2 + arc_angle / 2
        end_angle = np.pi / 2 - arc_angle / 2
        self.add(Arc(
            start_angle=start_angle,
            angle=-arc_angle
        ))
        tick_angle_range = np.linspace(start_angle, end_angle, num_ticks)
        for index, angle in enumerate(tick_angle_range):
            vect = rotate_vector(RIGHT, angle)
            tick = Line((1 - tick_length) * vect, vect)
            label = Tex(str(10 * index))
            label.set_height(tick_length)
            label.shift((1 + tick_length) * vect)
            self.add(tick, label)

        needle = Polygon(
            LEFT, UP, RIGHT,
            stroke_width=0,
            fill_opacity=1,
            fill_color=needle_color
        )
        needle.stretch_to_fit_width(needle_width)
        needle.stretch_to_fit_height(needle_height)
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



class ChessBoard(SVGMobject):
    file_name = get_svg("chess.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.scale(3)



class Heart(SVGMobject):
    file_name = get_svg("heart.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_fill(RED_E, 2.0)
        self.scale(0.5)



class Diamond(SVGMobject):
    file_name = get_svg("diamond.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_fill(RED_E, 2.0)
        self.scale(0.5)



class Spade(SVGMobject):
    file_name = get_svg("spade.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_fill(BLACK, 2.0)
        self.scale(0.5)



class Club(SVGMobject):
    file_name = get_svg("club.svg")
    def __init__(self, **kwargs):
        SVGMobject.__init__(self, **kwargs)
        self.set_fill(BLACK, 2.0)
        self.scale(0.5)



class Checkmark(Tex):
    color = GREEN
    def __init__(self, **kwargs):
        super().__init__("\\ding{51}")



class Exmark(Tex):
    color = RED
    def __init__(self, **kwargs):
        super().__init__("\\ding{55}")



class SpeechBubble(SVGMobject):
    file_name = get_svg("speech.svg")  # "Bubbles_speech.svg" "bubble-speech.svg"
    direction = LEFT
    center_point = ORIGIN
    content_scale_factor = 1 # 0.75
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
        # self.refresh_unit_normal()
        # self.refresh_triangulation()
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
        self.add_content(Tex(*text))
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
    content_scale_factor = 1 # 0.75
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
        # self.refresh_unit_normal()
        # self.refresh_triangulation()
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
        self.add_content(Tex(*text))
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




        
        
        
        
        
        
        
        
"""
Some Classes like SpeechBubble & ThoughtBubble etc.
are originally made by 3Blue1Brown's Manim, I've made some
modifications in it so that one can use them in 
Community Version Manim.
"""
