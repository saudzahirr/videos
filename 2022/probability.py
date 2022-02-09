from manimce import *
from custom.drawings import Heart, Diamond, Spade, Club



class PlayingCard(VMobject):
    def __init__(self, turned_over, value = None, suit = None, key = None):
        VMobject.__init__(self)
        self.value = value
        self.suit = suit
        self.key = key
        self.turned_over = turned_over
        self.suit = suit
        self.value = value
        possible_suits = ["hearts", "diamonds", "spades", "clubs"]
        possible_values = list(map(str, list(range(2, 11)))) + ["J", "Q", "K", "A"]

        body = RoundedRectangle(
            height = 5, width = 3, fill_color = WHITE, fill_opacity = 1.0, corner_radius = 0.10, stroke_width = 5
        ).scale(0.75)

        if self.turned_over == True:
            body.set_fill(GREY_D)
            body.set_stroke(GREY_B)
            contents = VectorizedPoint(self.get_center())
            body.add(contents)
            
        else:
            value = self.get_value(possible_values)
            symbol = self.get_symbol(possible_suits)
            # design = self.get_design(value, symbol)
            design = Dot(0.0)
            corner_numbers = self.get_corner_numbers(value, symbol, body)
            contents = VGroup(design, corner_numbers)
            body.add(contents)
        self.add(body)
    
    def get_value(self, possible_values):
        value = self.value
        if value is None:
            if self.key is not None:
                value = self.key[:-1]
            else:
                value = choice(possible_values)
        value = str(value).upper()
        if value == "1":
            value = "A"
        if value not in possible_values:
            raise Exception("Invalid card value!")

        face_card_to_value = {
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }
        try:
            self.numerical_value = int(value)
        except Exception:
            self.numerical_value = face_card_to_value[value]
        return value

    def get_symbol(self, possible_suits):
        suit = self.suit
        if suit is None:
            if self.key is not None:
                suit = dict([
                    (s[0].upper(), s)
                    for s in possible_suits
                ])[self.key[-1].upper()]
            else:
                suit = choice(possible_suits)
        if suit not in possible_suits:
            raise Exception("Invalid suit value!")
        self.suit = suit
        symbol = None
        heart = Heart().scale(0.5)
        diamond = Diamond().scale(0.5)
        spade = Spade().scale(0.5)
        club = Club().scale(0.5)

        if suit is "hearts":
            symbol = heart
        elif suit is "diamonds":
            symbol = diamond
        elif suit is "spades":
            symbol = spade
        elif suit is "clubs":
            symbol = club
        return symbol
    
    def get_corner_numbers(self, value, symbol, body):
        value_mob = Tex(value).set_color(BLACK)
        mob = VGroup(
            value_mob.next_to(symbol, UP, buff = 0.10), symbol
        )
        mobject = VGroup(
            mob.next_to(
                body.get_corner(UL), DR,
                buff = MED_LARGE_BUFF * 1/4
            ),
            mob.copy().rotate(PI).next_to(
                body.get_corner(DR), UL,
                buff = MED_LARGE_BUFF * 1/4
            ),
        )
        return mobject
        



class Test(Scene):
    def construct(self):
        card = PlayingCard(turned_over = False, value = "Q", suit = "hearts")
        self.play(
            DrawBorderThenFill(card),
        )
        self.wait()
