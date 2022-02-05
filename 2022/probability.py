from manimce import *
from custom.drawings import Heart, Diamond, Spade, Club



class PlayingCard(VMobject):
    def __init__(self, **kwargs):
        VMobject.__init__(self, **kwargs)
        body = RoundedRectangle(
            height = 5, width = 3, fill_color = WHITE, fill_opacity = 1.0, corner_radius = 0.10, stroke_width = 5
        ).scale(0.75)
        heart = Heart().scale(0.5)
        diamond = Diamond().scale(0.5)
        spade = Spade().scale(0.5)
        club = Club().scale(0.5)
        
        body.add(
            club.next_to(
                body.get_corner(UL), DR,
                buff = MED_LARGE_BUFF * 1/4
            ),
            club.copy().next_to(
                body.get_corner(DR), UL,
                buff = MED_LARGE_BUFF * 1/4
            ),
        )
        self.add(body)



class Test(Scene):
    def construct(self):
        self.play(
            DrawBorderThenFill(
                PlayingCard()
            )
        )
        self.wait()
