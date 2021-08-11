"""Hello, world! = 01001000  01100101  01101100  01101100  01101111  00101100"""
"""00100000  01110111  01101111  01110010  01101100  01100100  00100001"""

from manim import *
from numpy import *
from random import *
from itertools import *
from logo import *
from thumbnail import *



def get_bit_grid(n_rows, n_cols, bits=None, buff=MED_SMALL_BUFF, height=4):
    bit_pair = VGroup(Integer(0), Integer(1)).scale(1.5)
    bit_mobs = VGroup(*[
        bit_pair.copy()
        for x in range(n_rows * n_cols)
    ])
    bit_mobs.arrange_in_grid(n_rows, n_cols, buff=buff)
    bit_mobs.set_height(height)
    if bits is None:
        bits = np.random.randint(0, 2, len(bit_mobs))

    for bit_mob, bit in zip(bit_mobs, bits):
        bit_mob[1 - bit].set_opacity(0)

    bit_mobs.n_rows = n_rows
    bit_mobs.n_cols = n_cols
    return bit_mobs


def get_image_bits(image, bit_height=0.15/2, buff=MED_SMALL_BUFF):
    bit = Integer(0)
    small_buff = (buff / bit.get_height()) * bit_height
    bit.set_height(bit_height)
    bits = get_bit_grid(
        n_rows=int(image.get_height() / (bit.get_height() + small_buff)),
        n_cols=int(image.get_width() / (bit.get_width() + small_buff)),
        buff=buff
    )
    bits.replace(image)
    return bits


class Voyager2(Scene):
    def construct(self):
        logo(self)
        bits = get_bit_grid(40, 33, height=6)
        bits.scale(0.1)
        bits.set_color(BLACK)

        image_in = ImageMobject("neptune")
        image_in.add(SurroundingRectangle(image_in, color = GREY_E))
        image_in.scale(0.7)
        image_out = ImageMobject("noise")
        image_out.scale(0.7)
        image_out.to_edge(RIGHT)

        in_box = SurroundingRectangle(image_in)
        in_box.set_fill(BLACK, 1)
        in_box.set_stroke(width=0)

        out_box = SurroundingRectangle(image_out)
        out_box.set_fill(BLACK, 1)
        out_box.set_stroke(width=0)

        satellite = SVGMobject("satellite")
        satellite.scale(1.3)
        satellite.set_color(WHITE)
        satellite.next_to(ORIGIN, LEFT)
        satellite.add(bits)

        voyager = Tex(r"Voyager 2")
        voyager.scale(1.3)
        voyager.to_edge(UP)
        voyager.set_color(BLUE)

        year = Tex(r"1977")
        year.scale(2)
        year.to_edge(UP + RIGHT)

        bits_ = get_image_bits(image_out)

        noise = Tex(r"Noise")
        noise.set_color(YELLOW)
        noise.next_to(image_out, DOWN)

        self.play(
            AnimationGroup(
                Animation(image_in),
                ApplyMethod(
                    in_box.stretch, 0, 1, {"about_edge": DOWN}, remover=True,
                    rate_func=linear,
                )
            ),
            voyager.animate,
            year.animate,
            run_time = 4
        )
        self.wait(2)

        self.play(
            image_in.animate.to_edge(LEFT),
            rate_func = smooth,
            run_time = 2
        )

        sender_bits = get_bit_grid(40, 33)
        sender_bits.replace(image_in, stretch=True)
        sender_bits.move_to(image_in)
        sender_bits.set_fill(GREY_B)
        receiver_bits = sender_bits.copy()
        receiver_bits.replace(image_out, stretch=True)
        receiver_bits.move_to(image_out)

        self.play(
            FadeInFromLarge(satellite),
            run_time = 2
        )
        self.wait()

        self.play(
            LaggedStart(
                *[
                    Succession(
                        FadeIn(bit),
                        Transform(bit, choice(bits)),
                        FadeOut(bit),
                    )
                    for bit in sender_bits
                ],
                lag_ratio = 3 / len(sender_bits),
                run_time = 12,
            )
        )
        self.wait()

        self.play(
            LaggedStart(
                *[
                    Succession(
                        GrowFromPoint(
                            bit,
                            choice(bits).get_center(),
                        ),
                        FadeOut(bit),
                    )
                    for bit in receiver_bits
                ],
                lag_ratio = 3 / len(receiver_bits),
                run_time = 12,
            ),
            AnimationGroup(
                Animation(image_out),
                ApplyMethod(      
                    out_box.stretch, 0, 1, {"about_edge": DOWN}, remover=True,
                    rate_func = linear,
                    run_time = 12
                )
            ),
            LaggedStartMap(
            VFadeInThenOut, bits_,
            run_time=12,
            lag_ratio=3 / len(bits_)
            )
        )
        self.play(
            FadeIn(noise),
        )
        self.wait(3)
        self.clear()





class History(Scene):
    def construct(self):
        thumbnail(self)

        dated_events = [
            {
                "date" : 1940, 
                "text": "Richard Hamming invented \\\\ codes to investigate \\\\ automatic error-correction.",
                "picture" : "Bell_Relay_Computer.png"
            }
        ]
        speical_dates = [2021] + [
            obj["date"] for obj in dated_events
        ]
        centuries = list(range(1850, 2050, 10))
        timeline = NumberLine(
            (centuries[0], centuries[-1], 2),
            numbers_with_elongated_ticks=centuries,
        )
        timeline.add_numbers(centuries)
        centers = [
            Point(timeline.number_to_point(year))
            for year in speical_dates
        ]
        timeline.add(*centers)
        timeline.shift(-centers[0].get_center())

        self.add(timeline)
        self.wait()
        run_times = iter([3, 1])
        for point, event in zip(centers[1:], dated_events):

            clock = Circle(radius = 2, color = WHITE)
            clock.add(Dot(ORIGIN))

            for vect in compass_directions(12):
                clock.add(Line(1.8*vect, 2*vect, color = WHITE))

            hour_hand = Line(ORIGIN, UP)
            minute_hand = Line(ORIGIN, 1.5*UP)
            clock.add(hour_hand, minute_hand)
            hour_hand.get_center = lambda : clock.get_center()
            minute_hand.get_center = lambda : clock.get_center()
            clock.scale(0.5)
            clock.to_edge(2*RIGHT+DOWN)
            self.add(clock)

            self.play(
                Rotating(hour_hand, radians = 2*np.pi, about_point = clock.get_center(), run_time = 2),
                Rotating(minute_hand, radians = 12*2*np.pi, about_point = clock.get_center(), run_time = 2),    
                ApplyMethod(
                timeline.shift, -point.get_center(),
                run_time = 3,
                rate_func = linear)
            )

            event_mob = Tex(event["text"])
            event_mob.shift(2*LEFT+2*UP)
            date_mob = Tex(str(event["date"]) + str('s'))
            date_mob.scale(0.5)
            date_mob.shift(1*DOWN)
            picture = ImageMobject(event["picture"], invert = False)
            picture.scale(0.45)
            picture.add(Tex("Model V Relay Computers.").set_color(YELLOW).scale(0.5).next_to(picture, 0.5*DOWN))
            picture.next_to(event_mob, RIGHT)
            line = Arrow(event_mob.get_bottom(), 0.2*UP)
            self.play(
                FadeIn(event_mob),
                FadeIn(line),
                FadeIn(date_mob)
            )
            self.play(FadeIn(picture), run_time = 2)
            self.wait(2)
            self.play(*list(map(FadeOut, [event_mob, date_mob, line, picture])))
        self.wait(1)
        self.remove(clock)
        self.remove(timeline)
        self.clear()


        p1 = ImageMobject("page1.jpg")
        p1.scale(0.85)
        p2 = ImageMobject("page2.jpg")
        p2.scale(0.85)
        p2.next_to(p1, 0.25 * DOWN)
        paper = Group(p1, p2)
        paper.to_edge(2 * UP)
        self.add(paper)
        self.wait(2)
        self.play(
            paper.animate.shift(22 * UP),
            run_time = 10
        )
        self.wait(1)
        self.play(
            paper.animate.shift(12 * UP),
            run_time = 8
        )
        self.wait(1)
        self.play(
            FadeOut(paper)
        )

        thumbnail(self)
        self.wait(0.1)

        hamming_image = ImageMobject("Richard_Hamming.jpg")
        hamming_image.scale(2.3)
        hamming_name = Tex("\\large Richard Hamming")
        hamming_name.match_width(hamming_image)
        hamming_image.add(SurroundingRectangle(hamming_image, color = GREY))
        hamming_name.next_to(hamming_image, DOWN, MED_SMALL_BUFF)
        hamming = Group(hamming_image, hamming_name)
        hamming.to_corner(UL)

        bell_logo = SVGMobject("BellTelephoneLaboratories")
        bell_logo.scale(1.5)
        bell_logo.to_edge(5*RIGHT+UP)

        bell_system = Tex(r"Bell Telephone Laboratories.")
        bell_system.next_to(bell_logo, DOWN)
        bell_logo.add(bell_system)

        punchcard = SVGMobject("punch-card")
        punchcard.set_stroke(width=0)
        punchcard.set_opacity(0.75)
        punchcard.scale(1.35)
        punchcard.next_to(bell_logo, DOWN)

        self.play(
            LaggedStartMap(FadeIn, hamming),
            Write(bell_logo),
            rate_func = smooth,
            run_time = 5
        )
        self.wait()
        self.play(
            FadeIn(punchcard[0]),
            Write(punchcard[1:], lag_ratio=0.5, run_time=10)
        )
        self.wait(3)
        self.play(
            FadeOut(hamming, bell_logo, punchcard),
            run_time = 0.5
        )





class BenEater(Scene):
    def construct(self): 
        thumbnail(self)

        self.camera.background_color = GREY_E
        data = Tex(r"\large{Data Transmission.}")
        data.set_color(BLUE)
        data.scale(1.3)
        data.to_edge(UP)

        error = Tex(r"\large{Error Detection.}")
        error.set_color(BLUE)
        error.scale(1.3)
        error.to_edge(UP)

        screen = ScreenRectangle(stroke_width=4,stroke_color=WHITE,fill_opacity=1,fill_color=BLACK)
        screen.scale(1.3)
        screen.next_to(data, 3 * DOWN)

        self.add(screen)
        self.play(
            data.animate,
        )
        self.wait(3)

        self.play(
            TransformMatchingTex(data, error),
            rate_func = smooth,
            run_time = 1.5
        )
        self.wait(4)
        self.clear()
