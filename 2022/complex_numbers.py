from manimce import *

# Manuscripts.
ars_magna = ImageMobject(get_image("ArsMagna.jpg"))
bombelli_algebra = ImageMobject(get_image("Bombelli_Algebra.jpg"))
infinitorum = ImageMobject(get_image("Introductio_in_analysin_infinitorum.png"))
quaternion_bridge = ImageMobject(get_image("Quaternion_Bridge.jpg"))

bombelli_poem = """
Plus by plus of minus, makes plus of minus."
Minus by plus of minus, makes minus of minus."
Plus by minus of minus, makes minus of minus."
Minus by minus of minus, makes plus of minus."
Plus of minus by plus of minus, makes minus."
Plus of minus by minus of minus, makes plus."
Minus of minus by plus of minus, makes plus."
Minus of minus by minus of minus makes minus"
"""
events = [
    "Ferro solves compressed \\\\ cubic equations.",
    "Tartaglia claims cubic \\\\ polynomial solutions.",
    "Cardano publishes \\\\ Tartaglia's work.",
    "Bombelli invents \\\\ complex numbers.",
    "Leibniz works on \\\\ cubic equations.",
    "Euler defines \\\\ $i = \\sqrt{-1}$"
]
portraits = [
    "Scipione_del_Ferro.png",
    "Niccolo_Tartaglia.jpg",
    "Cardan.jpg",
    "Rafael_Bombelli.jpeg",
    "Gottfried_Wilhelm_Leibniz.jpg",
    "Leonhard_Euler.png"
]
dates = [1520, 1530, 1545, 1572, 1702, 1770]

height = ImageMobject(get_portrait(portraits[2])).get_height()
width = ImageMobject(get_portrait(portraits[2])).get_width()
kwargs = {"run_time" : 20, "rate_func" : bezier([0, 0, 1, 1])}

def argand_plane(x, y):
    plane = ComplexPlane(
        x_range = [-x, x],
        y_range = [-y, y],
        x_length = 2*x,
        y_length = 2*y,
        background_line_style = {
            "stroke_width": 1,
        },
        faded_line_ratio = 2,
    )
    plane.add(SurroundingRectangle(plane, WHITE, buff = 0.0, stroke_width = 2))
    return plane


def get_figure(name, filename):
    image = ImageMobject(get_portrait(filename))
    image.add(SurroundingRectangle(image, WHITE, buff = 0.0, stroke_width = 1))
    name.next_to(image, DOWN)
    image.add(name)
    return image



class History(MovingCameraScene):
    def construct(self):
        frame = self.camera.frame
        frame.save_state()
        time_range = (1480, 2000)
        timeline = NumberLine(
            (*time_range, 1),
            tick_size = 0.025,
            longer_tick_multiple = 4,
            numbers_with_elongated_ticks = range(*time_range, 10),
        )
        timeline.stretch(0.25, 0)
        timeline.add_numbers(
            range(*time_range, 10),
            group_with_commas = False,
        )
        frame.move_to(timeline.n2p(1526))
        timeline.set_y(-3)
        self.add(timeline)
        for portrait, date, event in zip(portraits, dates, events):
            self.get_event(portrait, date, event, timeline)
        self.wait()
        self.play(
            frame.animate.shift(5 * FRAME_WIDTH * RIGHT),
            **kwargs
        )
        self.play(
            FadeOut(timeline),
            run_time = 2
        )
        self.clear()

    def get_event(self, image, date, event, timeline):
        event = Tex(event)
        event.scale(0.7)
        image = ImageMobject(get_portrait(image))
        image.set_height(height)
        image.set_width(width)
        image.add(SurroundingRectangle(image, WHITE, buff = 0.0, stroke_width = 1))
        image.next_to(timeline.n2p(date), UP, buff = 2.0)
        event.next_to(image, DOWN)
        image.add(event)
        if date == 1520:
            date = 1526
            arrow = Arrow(event.get_right(), timeline.n2p(date))
            self.add(arrow)
        date = Tex("(" + str(date) + ")")
        date.next_to(event, DOWN)
        image.add(date)
        self.add(image)



class CardanFormula(Scene):
    def construct(self):
        history = Tex(
            "Gerolamo Cardano, the first mathematician" "\\\\",
            "to use 'negative numbers'." "\\\\",
            "He published the solution of" "\\\\",
            "a cubic equation of form:"
        )
        quadratic_equation = MathTex("ax^{2} + bx + c = 0")
        quadratic_formula = MathTex("x = \\frac{ -b \\pm \\sqrt{ b^{2} - 4ac } }{2a}")
        cubic_equation = MathTex("x^{3} + px + q = 0")
        cardan_formula = MathTex(
            "x = \\sqrt[3]{ -\\frac{ q }{ 2 } + \\sqrt{ {\\frac{ q }{ 4 } }^{2} + {\\frac{ p }{ 27 } }^{3} } } + \\sqrt[3]{ -\\frac{ q }{ 2 } - \\sqrt{ {\\frac{ q }{ 4 } }^{2} + {\\frac{ p }{ 27 } }^{3} } }"
        )

        plane = argand_plane(3, 4)
        plane.set_height(5.0)
        plane.to_corner(DR)
        plane.shift(0.5 * UP)
        plane.add(SurroundingRectangle(plane, WHITE, buff = 0.0, stroke_width = 2))

        self.play(
            FadeIn(plane)
        )
        self.wait(2)



class CasusIrreducibilis(Scene):
    def construct(self):
        year = Tex("1545")
        year.scale(1.5)
        year.to_edge(UP + 2 * LEFT)
        
        equations = VGroup(
            MathTex("x^{2} + 2x + 2 = 0"),
            MathTex("x^{3} = 6x + 4")
        )
        equations.arrange(RIGHT, buff = 3.0)

        roots = VGroup(
            MathTex("-1 \\pm \\sqrt{-1}",),
            MathTex("\\sqrt[3]{2 + \\sqrt{-2}}  + \\sqrt[3]{2 - \\sqrt{-2}} ")
        )
        roots.arrange(RIGHT, buff = 3.0)

        self.play(
            Write(year),
            rate_func = smooth
        )
        for equation, root in zip(equations, roots):
            root.next_to(equation, DOWN, buff = 1.0)
            self.play(
                Write(equation),
                rate_func = smooth
            )
            self.wait(0.5)
            self.play(
                Write(root),
                rate_func = smooth
            )
            self.wait(1)
        self.wait(2)

        self.play(
            FadeOut(year, equations, roots[0]),
            roots[1].animate.next_to(ORIGIN, 0.25 * RIGHT)
        )
        self.wait()


        casus_irreducibilis = Tex(r"Casus Irreducibilis")
        casus_irreducibilis.scale(1.2)
        casus_irreducibilis.next_to(roots[1], UP, buff = 1.5)
        translation = Tex("Latin for ", "“the irreducible case”")
        translation.set_color_by_tex("“the irreducible case”", YELLOW)
        translation.set_color(GREY_B)
        translation.next_to(casus_irreducibilis, DOWN, buff = 0.25)
        bombelli.scale(1.5)
        bombelli.to_edge(LEFT)
        bombelli.shift(DOWN)
        rafael_bombelli.next_to(bombelli, DOWN)


        self.play(
            Write(casus_irreducibilis)
        )
        self.wait()
        self.play(
            Write(translation)
        )
        self.wait(2)

        self.play(
            FadeIn(bombelli, rafael_bombelli),
            rate_func = smooth,
            run_time = 2
        )
        self.wait()


        speech = SpeechBubble()
        speech.next_to(bombelli.get_right(), UP)
        words = Tex(
            "Plus by plus of minus," "\\\\",
            "makes plus of minus." "\\\\",
            "Minus by plus of minus," "\\\\",
            "makes minus of minus." "\\\\"
        )
        speech.add_content(words)
        speech.position_mobject_inside(words)
        speech.resize_to_content()
        speech.move_tip_to(bombelli.get_right())


        self.play(
            Create(speech),
            Write(words, run_time = 3, rate_func = smooth),
            rate_func = smooth
        )
        self.wait(2)


        bombelli_rules = Tex(
            "“plus of minus” for $i = \\sqrt{-1}$" "\\\\",
            "“minus of minus” for $-i = -\\sqrt{-1}$",
        )
        bombelli_rules.set_color(YELLOW)
        bombelli_rules.next_to(roots[1], DOWN, buff = 1.0)

        self.play(
            Write(bombelli_rules),
            rate_func = smooth,
            run_time = 3
        )
        self.wait()

        
        
class EulersManuscript(ExternallyAnimatedScene):
    pass





