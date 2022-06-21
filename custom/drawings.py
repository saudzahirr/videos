from manim import *
from custom.functions import *
from custom.constants import *




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
        # for hand in self.hour_hand, self.minute_hand:
        #     #Balance out where the center is
        #     hand.add(VectorizedPoint(-hand.get_end()))

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



def PlayingCard(
    value = None, suit = None, key = None,  # String like "8H" or "KS"
    height = 4, height_to_width = 8 / 5, card_height_to_symbol_height = 7,
    card_width_to_corner_num_width = 10, card_height_to_corner_num_height = 10,
    color = GREY_A, turned_over = False
    ):
    possible_suits = ["heart", "diamond", "spade", "club"],
    possible_values = list(map(str, list(range(2, 11)))) + ["J", "Q", "K", "A"]
    
    card = RoundedRectangle(height = height, width = height / height_to_width)
    card.set_fill(WHITE, 1.2)


    def get_value(value, possible_values):
        if value is None:
            value = random.choice(possible_values)
        value = str(value).upper()
        if value == "1":
            value = "A"
        if value not in possible_values:
            raise Exception("Invalid Card Value!")

        face_card_to_value = {
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }
        try:
            numerical_value = int(value)
        except Exception:
            numerical_value = face_card_to_value[value]
        return value
    
    def get_symbol(suit, possible_suits):
        if suit is None:
            suit = random.choice(possible_suits)
            print(suit)
        if suit not in possible_suits:
            raise Exception("Invalid Suit Value!")

        def SuitSymbol(suit):
            from custom.drawings import Heart, Diamond, Spade, Club
            suit_symbols = {
                "heart": Heart(),
                "diamond": Diamond(),
                "spade": Spade(),
                "club": Club(),
            }
            return suit_symbols[random.choice(suit)]

        symbol_height = float(height) / card_height_to_symbol_height
        symbol = SuitSymbol(suit)
        symbol.scale(0.85)
        
        return symbol
    
    def get_design(card, value, symbol):

        def get_ace_design(card, symbol):
            design = symbol.copy().scale(1.5)
            design.move_to(card)
            return design

        def get_number_design(card, value, symbol):
            num = int(value)
            n_rows = {
                2: 2,
                3: 3,
                4: 2,
                5: 2,
                6: 3,
                7: 3,
                8: 3,
                9: 4,
                10: 4
            }[num]
            n_cols = 1 if num in [2, 3] else 2
            insertion_indices = {
                5: [0],
                7: [0],
                8: [0, 1],
                9: [1],
                10: [0, 2]
            }.get(num, [])
            
            top = card.get_top() + symbol.get_height() * DOWN
            bottom = card.get_bottom() + symbol.get_height() * UP
            column_points = [
                interpolate(top, bottom, alpha)
                for alpha in np.linspace(0, 1, n_rows)
            ]
            design = VGroup(*[
                symbol.copy().move_to(point)
                for point in column_points
            ])
            if n_cols == 2:
                space = 0.2 * card.get_width()
                column_copy = design.copy().shift(space * RIGHT)
                design.shift(space * LEFT)
                design.add(*column_copy)
            design.add(*[
                symbol.copy().move_to(
                    center_of_mass(column_points[i:i + 2])
                )
                for i in insertion_indices
            ])
            for symbol in design:
                if symbol.get_center()[1] < card.get_center()[1]:
                    symbol.rotate(np.pi)
            
            return design

        if value == "A":
            return get_ace_design(card, symbol)
        if value in list(map(str, list(range(2, 11)))):
            return get_number_design(card, value, symbol)
        else:
            return None # self.get_face_card_design(value, symbol)

        
    def get_corner_numbers(card, value, symbol):
        value_mob = Tex(value)
        width = card.get_width() / card_width_to_corner_num_width
        height = card.get_height() / card_height_to_corner_num_height
        value_mob.set_width(width)
        value_mob.stretch_to_fit_height(height)
        value_mob.next_to(
            card.get_corner(UP + LEFT), DOWN + RIGHT,
            buff = MED_LARGE_BUFF * width
        )
        value_mob.set_color(symbol.get_color())
        corner_symbol = symbol.copy()
        corner_symbol.set_width(width)
        corner_symbol.next_to(
            value_mob, DOWN,
            buff = MED_SMALL_BUFF * width
        )
        corner_group = Group(value_mob, corner_symbol)
        opposite_corner_group = corner_group.copy()
        opposite_corner_group.rotate(
            PI, about_point = card.get_center()
        )

        return Group(corner_group, opposite_corner_group)
    
    if turned_over is True:
        card.set_fill(GREY_D)
        card.set_stroke(GREY_B, 0)
        contents = VectorizedPoint(card.get_center())
        card.add(contents)
        return card
    
    else:
        value = get_value(value, possible_values)
        symbol = get_symbol(suit, possible_suits)
        design = get_design(card, value, symbol)
        corner_numbers = get_corner_numbers(card, value, symbol)
        card.add(design)
        card.add(corner_numbers)
        return card
    
    
    
def PascalsTriangle(n):
    triangle = str()
    for a in range(0, n):
        for b in range(0, a + 1):
            triangle += str(C(a, b))
            triangle += " \\ "
        triangle += "\\\\"
        
    return Tex(triangle, tex_template = tex_temp).scale(1.15)



TemplateForMusicTeX = TexTemplate(
    preamble=r"""
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{mtxlatex}
\usepackage{graphicx}
"""
)

def MusicTeX(*tex_strings, **kwargs):
    return Tex(
        *tex_strings,
        tex_template = TemplateForMusicTeX,
        tex_environment = "music", # <- Change enviroment
        **kwargs
    )



class Checkmark(Tex):
    color = GREEN
    def __init__(self, **kwargs):
        super().__init__("\\checkmark")



class Exmark(Tex):
    color = RED
    def __init__(self, **kwargs):
        super().__init__("\\exmark")



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
