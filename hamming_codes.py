from manim import *
from numpy import *
from random import *
from itertools import *

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

def get_image_bits(image, bit_height=0.15, buff=MED_SMALL_BUFF):
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

def image_reveal_animation(image, bit_height=0.1):
    box = SurroundingRectangle(image)
    box.set_fill(BLACK, 1)
    box.set_stroke(width=0)
    bits = get_image_bits(image, bit_height=bit_height)

    return AnimationGroup(
        Animation(image),
        ApplyMethod(
            box.stretch, 0, 1, {"about_edge": DOWN}, remover=True,
            rate_func=linear,
        ),
        LaggedStartMap(
            VFadeInThenOut, bits,
            run_time=1,
            lag_ratio=3 / len(bits)
        )
    )

def string_to_bools(message):
    as_int = int.from_bytes(message.encode(), 'big')
    bits = "{0:b}".format(as_int)
    bits = (len(message) * 8 - len(bits)) * '0' + bits
    return [bool(int(b)) for b in bits]

def string_to_bits(message):
    return [int(b) for b in string_to_bools(message)]

def get_sound_wave():
    sound = VGroup(*[
        Line(DOWN, UP).set_height(
            (0.3 + 0.8 * random()) * abs(np.sin(x))
        )
        for x in np.linspace(0, 3 * PI, 100)
    ])
    sound.arrange(RIGHT, buff=0.05)
    return sound

class Decode(Scene):
    def construct(self):
        #LOGO
        circle_1 = Circle(radius=1,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2)
        title_1 = MathTex("\\alpha")
        title_1.scale(4.5)
        logo = VGroup(circle_1, title_1)
        logo.scale(1.3)
        logo_name = Text("aljabrak")
        logo_name.scale(1.2)
        logo_name.next_to(logo, 1.5*DOWN)
        self.play(Write(logo), Write(logo_name), run_time = 5)
        self.wait(2)

        circle_2 = Circle(radius=0.25,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2)
        title_2 = MathTex("\\alpha")
        thumbnail = VGroup(circle_2, title_2)
        thumbnail.scale(1.1)
        thumbnail.to_edge(0.5*DOWN+0.5*RIGHT)
        self.play(Transform(logo, thumbnail), FadeOut(logo_name), run_time = 1)

        image = ImageMobject("Starry_Night")
        image.add(SurroundingRectangle(image, color = BLUE_B))
        image.set_opacity(0.99)
        image.scale(0.75)
        self.play(
            image_reveal_animation(image),
            run_time = 4,
            rate_func = smooth
        )
        image.set_opacity(1)
        self.wait(2)


class HammingIntroduction(Scene):
    def construct(self):
        #LOGO
        circle_2 = Circle(radius=0.25,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2)
        title_2 = MathTex("\\alpha")
        thumbnail = VGroup(circle_2, title_2)
        thumbnail.scale(1.1)
        thumbnail.to_edge(0.5*DOWN+0.5*RIGHT)
        self.add(thumbnail)


        dated_events = [
            {
                "date" : 1940, 
                "text": "Richard Hamming invented \\\\ codes to investigate \\\\ automatic error-correction.",
                "picture" : "Bell_Relay_Computer"
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

        # self.play(
        #     FadeIn(timeline),
        #     run_time = 2
        # )
        self.add(timeline)
        self.wait()
        run_times = iter([3, 1])
        for point, event in zip(centers[1:], dated_events):

            clock = Circle(radius = 2, color = WHITE)
            clock.add(Dot(ORIGIN))
            # clock.add(Circle(radius = 2.2, color = GREY_A))
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
                Rotating(hour_hand, radians = -2*np.pi, about_point = clock.get_center(), run_time = 2),
                Rotating(minute_hand, radians = -12*2*np.pi, about_point = clock.get_center(), run_time = 2),    
                ApplyMethod(
                timeline.shift, -point.get_center(),
                # run_time = next(run_times)
                run_time = 2,
                rate_func = smooth)
            )

            event_mob = Tex(event["text"])
            event_mob.shift(2*LEFT+2*UP)
            # paper = event_mob.get_part_by_tex('Quantum Information Theory')
            # paper.set_color(YELLOW)
            date_mob = Tex(str(event["date"]) + str('s'))
            date_mob.scale(0.5)
            date_mob.shift(1*DOWN)
            picture = ImageMobject(event["picture"], invert = False)
            # picture.set_width(2)
            # picture.to_corner(UP+3*RIGHT)
            picture.scale(0.45)
            picture.add(Tex("Model V Relay Computers.").set_color(YELLOW).scale(0.5).next_to(picture, 0.5*DOWN))
            #picture.set_color(BLACK)
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
        # self.play(
        #     FadeOut(timeline),
        #     run_time = 0.25
        # )
        self.remove(timeline)

        hamming_image = ImageMobject("Richard_Hamming")
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
        #punchcard.set_fill(WHITE, 1)
        punchcard.next_to(bell_logo, DOWN)
        #punchcard.remove(*punchcard[23:])

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
        self.wait()
        self.play(
            FadeOut(hamming, bell_logo, punchcard),
            run_time = 0.5
        )

class HammingMatrix(Scene):
    def construct(self):
        #LOGO
        circle_2 = Circle(radius=0.25,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2)
        title_2 = MathTex("\\alpha")
        thumbnail = VGroup(circle_2, title_2)
        thumbnail.scale(1.1)
        thumbnail.to_edge(0.5*DOWN+0.5*RIGHT)
        self.add(thumbnail)
        tex = [
            Tex("01001000"), Tex("01100101"), Tex("01101100"), Tex("01101100"),
            Tex("01101111"), Tex("00100000"), Tex("01010111"), Tex("01101111"),
            Tex("01110010"), Tex("01101100"), Tex("01100100"), Tex("00100001")
        ]
        binary = VGroup(*tex)
        binary.scale(1.6)
        binary.arrange(RIGHT, buff=LARGE_BUFF)
        text = Tex(r"Hello World!")
        text.scale(2)
        text.to_edge(4*UP)
        for item, color in zip(binary, cycle([BLUE_A, BLUE_B, BLUE, BLUE_C, BLUE_D, BLUE_E])):
            item.set_color(color)

        binary.move_to(ORIGIN, LEFT)
        self.play(
            Write(text),
            run_time = 5
        )
        self.play(binary.animate.shift((binary.get_width() - 5) * LEFT), run_time=12)
        self.wait()

        self.play(
            tex[10].animate.set_color(BLUE_A).scale(1.3125)
        )
        #self.play(FadeOut(tex[11], run_time = 25/len(tex)))
        for i in range(0, 3):
            if i != 1:
                self.play(
                    FadeOut(tex[11-i]),
                    run_time = 5/len(tex)
                )
        for i in range(0, 8):
            self.play(
                FadeOut(tex[7-i]),
                run_time = 1/len(tex)**3
            )
        self.play(
            tex[10].animate.next_to(text, 3.5*DOWN),
            text.animate.to_edge(UP),
        )
        self.wait(0.35)

        bit_vector = Tex("0","1","1","0","0","1","0","0")
        bit_vector.set_color(BLUE_A)
        bit_vector.scale(2.1)
        bit_vector.move_to(tex[10])
        
        self.play(
            bit_vector.animate,
            FadeOut(tex[10])
        )
        self.wait(0.75)
        
        self.play(
            bit_vector[4:].animate.next_to(bit_vector[3], 2*RIGHT),
            #bit_vector[5:7].animate.shift(0.5*RIGHT),
            bit_vector[0:4].animate.shift(0.5*LEFT)
        )
        self.wait(0.75)
        
        brace = Brace(bit_vector[0:4])
        brace_label = Tex("Message Bits.").next_to(brace, DOWN)
        self.play(
            brace.animate,
            Write(brace_label, run_time=3)
        )
        self.wait(0.5)

        self.play(
            bit_vector[4:].animate.set_color(BLACK),
            FadeOut(brace, brace_label)
        )
        self.wait(0.5)

        self.play(
            bit_vector[0:4].animate.move_to(ORIGIN),
        )
        self.wait(0.75)

        message_bits = MathTex("\\textbf{b} = \\begin{pmatrix} 0 & 1 & 1 & 0 \\end{pmatrix}")
        message_bits.scale(1.5)

        self.play(
            FadeTransform(bit_vector, message_bits),
        )
        self.wait()

        frame_vec = SurroundingRectangle(message_bits).scale(1.2)
        frame_vec.add(Tex(r"This is Message Bit Vector.").next_to(frame_vec, UP))
        self.play(
            FadeIn(frame_vec),
        )
        self.wait()
        self.play(
            FadeOut(frame_vec)
        )
        self.wait()

        self.play(
            FadeOut(text),
            message_bits.animate.to_edge(UP)
        )
        self.wait()

        encode_text = Tex(
            "Encoding Message Vector." "\\\\",
            "bbbb" "\\\\",
            "$e(\\textbf{b}) = $ C$\\textbf{b}^{\\small{\\text{T}}} = \\textbf{v}$" "\\\\",
            "bbbb" "\\\\",
            "Here $\\textbf{v}$ is codeword vector \\\\ and C is code matrix."
        )
        encode_text.next_to(message_bits, 3*DOWN)
        encode_text[1].scale(0.25)
        encode_text[2].scale(1.5)
        encode_text[3].scale(0.25)
        encode_text[1].set_color(BLACK)
        encode_text[2].set_color(BLUE)
        encode_text[3].set_color(BLACK)

        self.play(
            Write(encode_text[0:3]),
            run_time=4
        )
        self.wait(0.5)

        self.play(
            Write(encode_text[4]),
            run_time=5
        )
        self.wait()

        self.play(
            FadeOut(message_bits, encode_text),
        )
        self.wait(1)

        explanation = Tex(
            "Hamming ", "H(7,4) ", "Error Correction."
        ).to_edge(UP)
        explanation.scale(1.3)
        explanation[0].set_color(YELLOW)
        explanation[1].set_color(BLUE_B)
        explanation[2].set_color(YELLOW)
        
        code_matrix = Tex(
            "C $ =$ ","$\\begin{bmatrix} 1 & 1 & 0 & 1 \\\\ 1 & 0 & 1 & 1 \\\\ 1 & 0 & 0 & 0 \\\\ 0 & 1 & 1 & 1 \\\\ 0 & 1 & 0 & 0 \\\\ 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & 1 \\end{bmatrix}$",
        )#.next_to(explanation, 5*DOWN)

        message_bits = MathTex("\\begin{bmatrix} 0\\\\1\\\\1\\\\0 \\end{bmatrix}").next_to(code_matrix[1], RIGHT)
        codeword = MathTex("=", "\\begin{bmatrix} 1\\\\1\\\\0\\\\0\\\\1\\\\1\\\\0 \\end{bmatrix}")#.next_to(message_bits, RIGHT)
        codeword.shift(2*RIGHT)
        encode = MathTex("e\\left( \\begin{bmatrix} 0\\\\1\\\\1\\\\0 \\end{bmatrix} \\right) = ").next_to(code_matrix, 4*LEFT)

        self.play(
            Write(explanation),
            run_time=2
        )
        self.play(
            FadeIn(code_matrix)
        )
        self.wait(0.5)

        code_label = Tex("H(7,4) Code Matrix.").set_color(MAROON_B).next_to(code_matrix, 3*DOWN)

        self.play(
            Indicate(code_matrix, color=BLUE_B),
            FadeIn(code_label, run_time=3),
            run_time=2
        )
        self.wait(0.5)
        self.play(FadeOut(code_label))
        self.wait()

        self.play(
            FadeOut(code_matrix[0]),
            FadeTransform(explanation, encode_text[2].move_to(explanation)),
            TransformFromCopy(code_matrix[0], encode),
            code_matrix[1].animate.shift(2*LEFT),
            message_bits.animate.shift(2*LEFT)
        )
        self.wait()

        self.play(
            TransformFromCopy(message_bits, codeword)
        )
        self.wait()

        hamming_matrix = MathTex(
            "\\begin{bmatrix} 0 & 0 & 0 & 1 & 1 & 1 & 1 \\\\ 0 & 1 & 1 & 0 & 0 & 1 & 1 \\\\ 1 & 0 & 1 & 0 & 1 & 0 & 1 \\end{bmatrix}",
            "= \\begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\end{bmatrix}"
        )
        hamming_matrix[0].move_to(code_matrix[1])
        hamming_matrix[1].next_to(codeword[1], RIGHT)
        hamming_check = Tex("H$\\textbf{v} = \\textbf{0}$")
        hamming_check.set_color(BLUE)
        hamming_check.scale(1.5)
        hamming_check.move_to(encode_text[2])

        self.play(
            FadeTransform(encode_text[2], hamming_check),
            FadeOut(encode, codeword[0], message_bits),
            FadeTransform(code_matrix[1], hamming_matrix[0]),
            codeword[1].animate.shift(0.5*LEFT),
        )
        self.play(
            hamming_matrix[1].animate.shift(0.35*LEFT),
        )
        self.wait(0.5)
        brace_syndrome_vec = Brace(hamming_matrix[1], color=BLUE_A)
        brace_syndrome_vec.add(Tex("No Error!"))
        brace_syndrome_vec.next_to(hamming_matrix[1], RIGHT)
        
        self.play(
            FadeIn(brace_syndrome_vec),
            run_time=2
        )
        self.wait(0.5)
        self.play(FadeOut(brace_syndrome_vec))
        self.wait(0.85)

        noise = Tex("Due to ", "\\large{Noise and Interference!}" "\\\\", "Some of the bits get ", "flipped!")
        noise[1].set_color(YELLOW)
        noise[3].set_color(BLUE_C)
        noise.to_edge(UP+LEFT)

        codeword_trans = MathTex("\\begin{bmatrix} 1\\\\1\\\\1\\\\0\\\\1\\\\1\\\\0 \\end{bmatrix}")
        codeword_trans.move_to(codeword[1])

        self.play(
            FadeOut(hamming_check),
            run_time=0.5
        )
        self.play(
            Write(noise),
            run_time=4,
            lag_ratio=0.5
        )
        self.wait(0.2)
        self.play(
            ApplyWave(noise[1]),
            Wiggle(noise[3]),
            run_time=2
        )
        self.play(
            ReplacementTransform(codeword[1], codeword_trans)
        )
        self.wait()
