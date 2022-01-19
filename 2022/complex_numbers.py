from manimce import *


# Manuscripts.
ars_magna = ImageMobject(get_image("ArsMagna.jpg"))
bombelli_algebra = ImageMobject(get_image("Bombelli_Algebra.jpg"))
infinitorum = ImageMobject(get_image("Introductio_in_analysin_infinitorum.png"))
quaternion_bridge = ImageMobject(get_image("Quaternion_Bridge.jpg"))
internet_archives_logo = SVGMobject(get_svg("Internet_Archive.svg"))


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
names = [
    "Scipione del Ferro",
    "Niccolo Tartaglia",
    "Gerolamo Cardano",
    "Rafael Bombelli",
    "Gottfried Wilhelm Leibniz",
    "Isaac Newton",
    "Leonhard Euler"
]
portraits = [
    "Scipione_del_Ferro.png",
    "Niccolo_Tartaglia.jpg",
    "Cardan.jpg",
    "Rafael_Bombelli.jpeg",
    "Gottfried_Wilhelm_Leibniz.jpg",
    "Isaac_Newton.png",
    "Leonhard_Euler.png"
]
dates = [1526, 1530, 1545, 1572, 1702, 1707, 1770]
events = [
    "Scipione del Ferro solves \\\\ compressed cubic equations.",
    "Niccolo Tartaglia claims \\\\ cubic polynomial solutions.",
    "Gerolamo Cardano publishes \\\\ Tartaglia's work.",
    "Rafael Bombelli publishes complex \\\\ numbers in the form of poem.",
    "Gottfried Wilhelm Leibniz \\\\ works on cubic equations.",
    "Isaac Newton works on the \\\\ numerical method for calculating roots.",
    "Leonhard Euler uses $i = \\sqrt{-1}$ \\\\ for complex numbers."
]


height = 1.3 * ImageMobject(get_portrait(portraits[2])).get_height()
width = 1.5 * ImageMobject(get_portrait(portraits[2])).get_width()
kwargs = {"run_time" : 3, "rate_func" : bezier([0, 0, 1, 1])}


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
    plane.add_coordinates()
    plane.add(SurroundingRectangle(plane, WHITE, buff = 0.0, stroke_width = 2))
    return plane


def get_figure(name, filename):
    name = Tex(name)
    name.set_width(width)
    image = ImageMobject(get_portrait(filename))
    image.set_height(height)
    image.set_width(width)
    image.add(SurroundingRectangle(image, WHITE, buff = 0.0, stroke_width = 2))
    name.next_to(image, DOWN)
    image.add(name)
    return image


class History(Scene):
    def construct(self):
        images = Group()
        for portrait, date, event in zip(portraits, dates, events):
            images.add(self.get_event(portrait, date, event))
        images.arrange(RIGHT, buff = 2*LARGE_BUFF)
        images.move_to(ORIGIN, LEFT)
        self.play(
            images.animate.shift((images.get_width() - 5) * LEFT),
            run_time = 0.25,
            rate_func = smooth
        )
        self.wait()
        self.clear()

        
    def get_event(self, image, date, event):
        event = Tex(event + " (" + str(date) + ")")
        event.set_width(width)
        image = ImageMobject(get_portrait(image))
        image.set_height(height)
        image.set_width(width)
        image.add(SurroundingRectangle(image, WHITE, buff = 0.0, stroke_width = 2))
        event.next_to(image, DOWN)
        image.add(event)
        return image



class CardanFormula(Scene):
    def construct(self):
        cardan = get_figure(names[6], portraits[6])
        cardan.to_corner(UL)
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

        plane = argand_plane(4, 4)
        plane.set_height(5.0)
        plane.to_corner(DR)
        plane.shift(0.5 * UP)
        plane.add(SurroundingRectangle(plane, WHITE, buff = 0.0, stroke_width = 2))

        self.play(
            FadeIn(cardan, plane)
        )
        self.draw_circle(plane.get_center())
        self.wait(2)

        
    def draw_circle(self, center):
        circle = Arc(angle = 2*np.pi, radius = 1)
        radius = Line(ORIGIN, circle.get_points()[0])
        radius.set_color(BLUE)
        circle.set_color(YELLOW)
        VGroup(radius, circle).move_to(center)
        modulus = MathTex("|z| = 1")
        modulus.scale(0.5)
        modulus.next_to(radius, UP)

        self.play(Create(radius), FadeIn(modulus))
        self.play(
            Rotate(radius, 2*np.pi, about_point = radius.get_start()),
            Create(circle),
            MaintainPositionRelativeTo(modulus, radius),
            run_time = 3,
        )
        self.wait(2)
        self.circle_group = VGroup(circle, radius, modulus)



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

        

class EulersPortrait(Scene):
    def construct(self):
        euler = get_figure(names[6], portraits[6])
        euler.scale(1.3)
        euler.to_edge(4 * LEFT)
        self.play(
            FadeIn(euler)
        )
        self.wait(3)

        
        
class EulersManuscript(ExternallyAnimatedScene):
    pass



def list_add(l1,l2):
    return [l1[x]+l2[x] for x,_ in enumerate(l1)]


class Introduction(Scene):
    def construct(self):
        def_cn = MathTex(r""" \begin{array}{l}
\textcolor[rgb]{0,0,0}{A\ complex\ number\ is\ any\ number\ of\ the\ form\ z\ =\ a\ +\ ib\ }\\
\textcolor[rgb]{0,0,0}{where\ a\ and\ b\ are\ real\ numbers\ and\ i} \ is\ the\ imaginary\ unit
\end{array}""").scale(0.9)
        def_im=MathTex("i=\sqrt{-1}").set_color(RED).move_to([0 ,-1 ,0])
        head_prp=Tex(r"""\begin{center}
{\Large \textbf{Arithmetic Operations}}
\end{center}
""")
        head_addsub=Tex(r"""\textbf{Addition/Subtraction}""").align_on_border(LEFT).shift(UP).scale(0.85)
        text_asm=MathTex(r"""z_{1} =a_{1} +ib_{1} \ \ \ \ \ \ \ \ \ \ \ \ 
        \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 
        \ \ \ \ \ \ \ \ z_{2} =a_{2} +ib_{2}""").set_color(RED).scale(0.7).move_to(([0,2.1,0]))
        text_addsub1=MathTex(r"""z_{1} \pm z_{2}""")
        text_addsub2 = MathTex(r"""( a_{1} +ib_{1}) \pm ( a_{2} +ib_{2})""")
        text_addsub3 = MathTex(r"""( a_{1} \pm a_{2}) +i( b_{1} \pm b_{2})""").set_color(YELLOW)

        head_mul=Tex(r"""\textbf{Multiplication}""").align_on_border(LEFT).shift(UP).scale(0.85)
        text_mul1=MathTex("( a_{1} +ib_{1})( a_{2} +ib_{2})")
        text_mul2 = MathTex("a_{1} a_{2} +a_{1} ib_{2} +a_{2} ib_{1} +i^{2} b_{1} b_{2}")
        text_mul3 = MathTex("a_{1} a_{2} +a_{1} ib_{2} +a_{2} ib_{1} -b_{1} b_{2}")
        text_mul4 = MathTex("a_{1} a_{2} -b_{1} b_{2} +i( a_{1} b_{2} +a_{2} b_{1})").set_color(YELLOW)

        self.play(Write(def_cn))
        self.wait(3)
        self.play(MoveAlongPath(def_cn,Line([0,0,0],[0, 1, 0])))
        self.play(Create(def_im))
        self.wait(1)
        self.play(FadeOut(def_im))
        self.play(ReplacementTransform(def_cn,head_prp))
        self.play(ScaleInPlace(head_prp,0.8))
        self.play(MoveAlongPath(head_prp,Line([0, 0, 0], [0, 3, 0])))
        self.play(Write(head_addsub))
        self.play(Write(text_asm))
        self.play(Write(text_addsub1))
        self.wait(2)
        self.play(ReplacementTransform(text_addsub1,text_addsub2))
        self.wait(2)
        self.play(ReplacementTransform(text_addsub2, text_addsub3))
        self.wait(2)
        self.play(FadeOut(text_addsub3))
        self.play(ReplacementTransform(head_addsub,head_mul))
        self.play(Write(text_mul1))
        self.wait(2)
        self.play(ReplacementTransform(text_mul1,text_mul2))
        self.wait(2)
        self.play(ReplacementTransform(text_mul2, text_mul3))
        self.wait(2)
        self.play(ReplacementTransform(text_mul3, text_mul4))
        self.wait(2)
        

class ArgandPlane(Scene):
    def construct(self):
        x_err=0.25
        y_err=0.05
        plane=argand_plane(6,3).add_coordinates()
        plane.set_height(7.0)
        d1=Dot(plane.n2p(0),color=YELLOW)
        p1=Arrow(start=plane.n2p(-0.25-0.05j),end=plane.n2p(4.25+1.05j),color=YELLOW,stroke_width=3)
        lblp1=MathTex("(4+i)").scale(0.5).next_to(p1,UR,0.1)

        p2 = Arrow(start=plane.n2p(0.25-0.1j), end=plane.n2p(-4.2 + 2.1j), color=YELLOW, stroke_width=3)
        lblp2=MathTex("(-4+2i)").scale(0.5).next_to(p2,UL,0.1)

        self.play(Create(plane))
        self.play(Create(d1))
        self.play(GrowArrow(p1))
        self.play(Write(lblp1))
        self.wait(2)
        self.play(FadeOut(lblp1))
        self.play(ReplacementTransform(p1,p2))
        self.play(FadeIn(lblp2))
        self.wait(2)



