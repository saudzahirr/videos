"""
Richard Hamming invented codes to investigate automatic error-correction.
Hello, world! = 01001000  01100101  01101100  01101100  01101111  00101100
00100000  01110111  01101111  01110010  01101100  01100100  00100001
"""


from manimce import *


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
        logo_transformation(self)
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

        noise = Tex(r"Noise!")
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
        self.wait(2)

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
        self.wait(2)

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
        self.wait(2)
        self.play(
            Write(noise),
            run_time = 1,
            rate_func = smooth,
            lag_ratio = 0.5
        )
        self.wait(8)
        self.play(
            FadeOut(image_out, year, satellite, voyager, noise)       
        )
        self.play(
            image_in.animate.to_edge(UP + RIGHT),
            run_time = 1.5,
            rate_func = smooth
        )


class ImageGreyScale(ZoomedScene):
    def __init__(self, **kwargs):
        super().__init__(
            zoom_factor=0.1,
            zoomed_display_height=4,
            zoomed_display_width=4,
            image_frame_stroke_width=2,
            zoomed_camera_config={
                "default_frame_stroke_width": 1,
                },
            **kwargs
        )

    def construct(self):
        image = ImageMobject("neptune")
        image.add(SurroundingRectangle(image, color = GREY_E))
        image.scale(0.7)
        image.to_edge(UP + RIGHT)

        self.add(image)
        self.wait()
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame
        zoomed_display.next_to(image, 10 * LEFT)
        zoomed_display.to_edge(0.5 * UP + 4 * LEFT)
        zd_rect = BackgroundRectangle(zoomed_display, fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)
        unfold_camera = UpdateFromFunc(zd_rect, lambda rect: rect.replace(zoomed_display))

        frame.move_to(image)
        self.play(Create(frame))
        self.activate_zooming()
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)
        self.wait(2)

        grey_scale_table = MathTable(
            [[50, 168, 216, 64],
            [198, 185, 140, 78],
            [255, 205, 108, 75]],
            include_outer_lines=True
        )
        grey_scale_table.scale(0.8)
        grey_scale_table.to_edge(0.5 * DOWN + LEFT)

        start = 0

        black = Variable(start, '\\text{Black}', num_decimal_places=0).next_to(grey_scale_table, 5 * RIGHT)
        white = Variable(start, '\\text{White}', num_decimal_places=0).next_to(black, DOWN)
        
        self.play(
            FadeIn(grey_scale_table)
        )
        self.play(
            FadeIn(black, white),
        )
        self.play(
            white.tracker.animate.set_value(255),
            rate_func=linear,
            run_time = 2
        )
        self.wait(2)
        self.clear()

        image.scale(5/7)
        image_copy = image.copy()
        noise = ImageMobject("noise.jpg")
        noise.add(SurroundingRectangle(noise, color = GREY_E))
        noise.scale(0.5)

        image.to_edge(UP + 4 * LEFT),
        image_copy.next_to(image, 4 * RIGHT)
        noise.next_to(image_copy, 4 * RIGHT)

        self.play(
            FadeIn(image, image_copy, noise)
        )
        self.wait()

        frame_1 = self.zoomed_camera.frame
        frame_2 = frame_1.copy()
        frame_3 = frame_1.copy()

        frame_1.move_to(image)
        frame_2.move_to(image_copy)
        frame_3.move_to(noise)

        table_1 = MathTable(
            [[50, 168, 216],
            [198, 185, 140],
            [255, 205, 108]],
            include_outer_lines=True
        )
        table_1.scale(0.6)
        table_2 = table_1.copy()
        table_3 = MathTable(
            [[50, 168, 216],
            [198, 189, 140],
            [255, 205, 108]],
            include_outer_lines=True
        )
        table_3.scale(0.6)

        table_1.next_to(image, 3 * DOWN)
        table_1.to_edge(2.5 * LEFT)
        table_2.next_to(table_1, 2 * RIGHT)
        table_3.next_to(table_2, 2 * RIGHT)

        self.play(
            Create(frame_1),
            FadeIn(table_1)
        )
        self.play(
            Create(frame_2),
            FadeIn(table_2)
        )
        self.play(
            Create(frame_3),
            FadeIn(table_3)
        )
        self.wait()


class History(MovingCameraScene):
    def construct(self):
        timeline = NumberLine(
            x_range = [1935, 1965],
            numbers_with_elongated_ticks = list(range(1935, 1965, 5)),
            color = BLUE_D,
        )
        timeline.stretch_to_fit_width((16*8)/9 - 5)
        timeline.add_numbers(timeline.numbers_with_elongated_ticks, group_with_commas=False)

        year = {
            1940 : "Hamming Codes.",
            1948 : "C.E. Shannon publishes a paper on \\\\ ``The Mathematical Theory of Communication.''",
            1960 : "Reed-Solomon Codes."
        }
        arrow_1 = Vector(DOWN, color = WHITE)
        arrow_1.next_to(timeline.number_to_point(1940), UP)
        word_1 = Tex(year[1940])
        word_1.next_to(arrow_1, UP)

        arrow_2 = Vector(UP, color = WHITE)
        arrow_2.next_to(timeline.number_to_point(1948), 2.25 * DOWN)
        word_2 = Tex(year[1948])
        word_2.scale(0.8)
        word_2.next_to(arrow_2, DOWN)

        arrow_3 = Vector(DOWN, color = WHITE)
        arrow_3.next_to(timeline.number_to_point(1960), UP)
        word_3 = Tex(year[1960])
        word_3.next_to(arrow_3, UP)

        timeline.scale(13/10)
        
        self.play(
            FadeIn(timeline),
        )
        self.play(
            timeline.animate.scale(10/13),
            GrowArrow(arrow_1),
            Write(word_1),
            GrowArrow(arrow_2),
            Write(word_2),
            GrowArrow(arrow_3),
            Write(word_3),
            run_time = 4
        )
        self.wait(4)
        self.play(
            FadeOut(timeline, arrow_1, word_1, arrow_2, word_2, arrow_3, word_3)
        )
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
        self.wait(2)
        self.play(
            FadeOut(paper)
        )
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
            FadeIn(punchcard),
            run_time = 2
            #Write(punchcard[1:], lag_ratio=0.5, run_time=10)
        )
        self.wait(3)
        self.play(
            FadeOut(hamming, bell_logo, punchcard),
            run_time = 0.5
        )
        self.clear()
        
        picture = "Bell_Relay_Computer.png"
        bell_labs = ImageMobject(picture)
        bell_labs.add(Tex("Archive: Model V Relay Computers.").scale(0.7).set_color(YELLOW).next_to(bell_labs, 0.5*DOWN).shift(2 * RIGHT))
        bell_labs.scale(0.9)

        script = Tex(
            "Richard Hamming invented\\\\",
            "codes to investigate\\\\",
            "automatic error-correction.",
        )
        # script.set_color(BLACK)
        # script.set_stroke(WHITE, 2, background=True)
        script.to_edge(UP + LEFT)

        self.play(
            FadeIn(bell_labs)
        )
        self.wait()
        self.add(BackgroundRectangle(script).scale(1.5))
        self.add_foreground_mobject(script)
        self.play(
            Write(script),
            run_time = 6,
            #lag_ratio = 0.1
        )
        self.wait(2)



class HammingCode(Scene):
    pass


class BenEater(Scene):
    def construct(self): 
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

      
    

    
def disk():
    inner_r = 1
    outer_r = 3
    annulus = Annulus(
        inner_radius=inner_r * 0.90,
        outer_radius=outer_r * 1.02,
        fill_color=GREY_D,
    )
    annulus.set_fill(color=[RED, YELLOW_B, GREEN_B, BLUE_B, WHITE], opacity=0.5)
    annulus.set_gloss(0.5)
    annulus.add(
        Annulus(
            inner_radius=inner_r * 0.50,
            outer_radius=outer_r * 0.30,
            fill_color=GREY_D,
            )
        )
    ring = Annulus(
            inner_radius=0.9,
            outer_radius=1.0,
            fill_color=GREY_D,
            fill_opacity=0.5
            )
    annulus.add(ring)
    dvd = SVGMobject("dvd")
    dvd.scale(0.5)
    dvd.set_color(GREY_D)
    dvd.set_opacity(0.65)
    dvd.next_to(ring, 2 * DOWN)
    annulus.add(dvd)

    cd = annulus.scale(0.75)
    return cd

class ReedSolomonCodes(Scene):
    def construct(self):
        title = Tex("Reed-Solomon Codes.")
        title.scale(1.5)
        title.to_edge(UP)
        self.play(
            FadeIn(title)
        )
        self.wait()

        qr_code = SVGMobject("qr")
        qr_code.scale(0.75)
        qr_code.set_color(WHITE)
        barcode = SVGMobject("barcode")
        barcode.scale(0.75)
        barcode.set_color(WHITE)
        cd = disk()

        identifier_codes = VGroup(qr_code, barcode)
        identifier_codes.arrange(2 * DOWN)
        identifier_codes.next_to(cd, 2 * LEFT)

        self.play(
            GrowFromCenter(cd, run_time = 2),
        )
        self.wait(3)

        for code in identifier_codes:
            self.play(
                FadeIn(code)
            )
            self.wait(0.5)
        self.wait(2)

        voyager2 = ImageMobject("voyager2.jpg")
        voyager2.scale(0.70)
        voyager2.next_to(cd, 2 * RIGHT)

        screen = SurroundingRectangle(voyager2, color = GREY)
        screen.add(Tex(r"Voyager 2.").set_color(BLUE).next_to(screen, UP))
        voyager2.add(screen)

        self.play(
            FadeIn(voyager2),
        )
        self.wait(2)

        self.play(
            VFadeInThenOut(
                Tex(r"Cyclic Polynomial Codes!").set_color(YELLOW).next_to(cd, 2 * DOWN),
                run_time = 10
            )
        )
        self.wait(2)

        self.play(
            FadeOut(title, cd, identifier_codes, voyager2),
            run_time = 1
        )
        self.wait(0.125)
