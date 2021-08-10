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


class Neptune(Scene):
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
