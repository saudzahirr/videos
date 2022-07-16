from manimce import *
from custom.drawings import Brain



# Colors.
X_COORD_COLOR = GREEN
Y_COORD_COLOR = ORANGE
VECTOR_COLOR = [BLUE_A, YELLOW, GREEN, ORANGE, MAROON_B, BLUE, PINK, PURPLE]
CURVE_COLOR = YELLOW
DOT_COLOR = YELLOW
TEX_HCOLOR = BLUE
MATH_HCOLOR = YELLOW


# Manuscripts.
ars_magna = ImageMobject(get_image("ArsMagna.jpg"))
bombelli_algebra = ImageMobject(get_image("Bombelli_Algebra.jpg"))
infinitorum = ImageMobject(get_image("Introductio_in_analysin_infinitorum.png"))
plaque = ImageMobject(get_image("Broom_Bridge_Plaque.jpg"))
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
    "Gerolamo_Cardano.jpg",
    "Rafael_Bombelli.jpeg",
    "Gottfried_Wilhelm_Leibniz.jpg",
    "Isaac_Newton.png",
    "Leonhard_Euler.png"
]

dates = [1526, 1530, 1545, 1572, 1702, 1711, 1770]

events = [
    "Scipione del Ferro solves \\\\ compressed cubic equations.",
    "Niccolo Tartaglia claims \\\\ cubic polynomial solutions.",
    "Gerolamo Cardano publishes \\\\ Tartaglia's work.",
    "Rafael Bombelli publishes complex \\\\ numbers in the form of poem.",
    "Gottfried Wilhelm Leibniz \\\\ works on cubic equations.",
    "Isaac Newton works on the \\\\ numerical method for calculating roots.",
    "Leonhard Euler uses $i = \\sqrt{-1}$ \\\\ for complex numbers."
]

number_systems = VGroup(
    Tex(
        "Zero: 0" "\\\\",
        "One: 1" "\\\\",
        "Prime numbers" "\\\\",
        "Composite numbers" "\\\\",
        tex_environment = "flushleft"
    ),
    Tex(
        "Natural: $\\mathbb{N}$" "\\\\",
        "Negative integers",
        tex_environment = "flushleft"
    ).arrange(DOWN, buff = 2),
    Tex(
        "Finite decimal" "\\\\",
        "Dyadic (finite binary)" "\\\\",
        "Repeating decimal",
        tex_environment = "flushleft"
    ),
    Tex(
        "Integer: $\\mathbb{Z}$" "\\\\",
        "Fraction",
        tex_environment = "flushleft"
    ).arrange(DOWN, buff = 3.5),
    Tex(
        "Algebraic" "\\\\",
        "Transcendental",
        tex_environment = "flushleft"
    ),
    Tex(
        "Rational: $\\mathbb{Q}$" "\\\\",
        "Irrational",
        tex_environment = "flushleft"
    ).arrange(DOWN, buff = 5),
    Tex(
        "Real: $\\mathbb{R}$" "\\\\",
        "Imaginary",
        tex_environment = "flushleft"
    ).arrange(DOWN, buff = 7.0),
    Tex(
        "Complex: $\\mathbb{C}$"
    )
)


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
    plane.add(SurroundingRectangle(plane, WHITE, buff = 0.0, stroke_width = 2))
    return plane


def glow_dot(point, r_min = 0.05, r_max = 0.15, color = YELLOW, n = 20, opacity_mult = 1.0):
    result = VGroup(*(
        Dot(point, radius = interpolate(r_min, r_max, a))
        for a in linspace(0, 1, n)
    ))
    result.set_fill(color, opacity = opacity_mult / n)
    return result


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
        cardan = get_figure(names[2], portraits[2])
        cardan.to_corner(UL)
        history = Tex(
            "Gerolamo Cardano", ", the first mathematician" "\\\\",
            "to use ", "`negative numbers'", ". ", "He published" "\\\\",
            "the solution of a cubic equation of form:"
        )
        history.set_color_by_tex("Gerolamo Cardano", BLUE)
        history.set_color_by_tex("`negative numbers'", YELLOW)
        history.to_edge(RIGHT)
        history.shift(UP)
        quadratic_equation = MathTex("ax^{2} + bx + c = 0")
        quadratic_formula = MathTex("x = \\frac{ -b \\pm \\sqrt{ b^{2} - 4ac } }{2a}")
        cubic_equation = MathTex("x^{3} + px + q = 0").next_to(history, DOWN)
        cardan_formula = MathTex(
            "x = \\sqrt[3]{ -\\frac{ q }{ 2 } + \\sqrt{ {\\frac{ q }{ 4 } }^{2} + {\\frac{ p }{ 27 } }^{3} } } + \\sqrt[3]{ -\\frac{ q }{ 2 } - \\sqrt{ {\\frac{ q }{ 4 } }^{2} + {\\frac{ p }{ 27 } }^{3} } }"
        )
        cardan_formula.shift(2 * DOWN)
        self.play(
            FadeIn(cardan),
            Write(
                history[0:5],
                run_time = 4,
                rate_func = smooth
            )
        )
        self.wait()
        self.play(
            Write(
                history[5:],
                run_time = 3,
                rate_func = smooth
            )
        )
        self.play(Write(cubic_equation))
        self.wait()
        self.play(
            Write(cardan_formula),
            run_time = 3,
            rate_func = smooth
        )
        self.wait(2)

        

class ManyNumberSystem(Scene):
    def construct(self):
        cnum=Ellipse(12,7,fill_color=TEAL_A,stroke_color=WHITE,stroke_width=6,fill_opacity=0.5)
        rnum=Circle(3.5,fill_color=TEAL_A,stroke_color=WHITE,stroke_width=6,fill_opacity=0.5).align_on_border(LEFT)
        inum = Circle(2, fill_color=PURPLE_A, stroke_color=WHITE, stroke_width=6, fill_opacity=0.5).align_on_border(RIGHT)
        cnum_t=Tex("Complex: ","$\\mathbb{C}$").move_to(cnum.get_center())
        rnum_t = Tex("Real: $\\mathbb{R}$").move_to(rnum.get_center())
        inum_t = Tex("Imaginary").move_to(inum.get_center())
        self.play(DrawBorderThenFill(cnum,rate_func=smooth))
        self.play(Write(cnum_t,rate_func=smooth,run_time=2))
        self.wait()
        self.play(FadeOut(cnum_t))
        self.play(TransformMatchingShapes(cnum,VGroup(rnum,inum),transform_mismatches=True))
        self.play(Write(VGroup(rnum_t,inum_t),rate_func=smooth,run_time=2))
        self.wait()
        self.add_foreground_mobjects(cnum, cnum_t[1])
        #self.bring_to_front(VGroup(rnum, inum, rnum_t, inum_t))
        self.play(
            ScaleInPlace(VGroup(rnum, inum, rnum_t, inum_t), 0.75),
            FadeIn(cnum, cnum_t[1]),
            rate_func=smooth
        )
        self.wait()    

        

class NumberSystem(Scene):
    def construct(self):
        title = Tex("Number Systems")
        title.scale(1.5)
        title.to_edge(UP)
        self.add(title)
        number_systems.scale(0.5)
        number_systems.next_to(title, DOWN, buff = 0.5)
        for number_system in number_systems:
            if number_system != number_systems[7]:
                line = Line(UP, DOWN, stroke_width = 8.0).set_height(number_system.get_height())
                line.next_to(number_system, LEFT)
                number_system.add(line)
        number_systems.arrange(LEFT, buff = 0.35)
        number_systems[0].next_to(number_systems[1][0], DR, buff = 0.25).shift(5 * LEFT + 3 * UP)
        number_systems[1].next_to(number_systems[3][0], DR, buff = 0.25).shift(2 * LEFT + 2 * UP)
        number_systems[3].next_to(number_systems[5][0], DR, buff = 0.25).shift(1.5 * UP)
        number_systems[5].next_to(number_systems[6][0], DR, buff = 0.25).shift(1 * UP)
        number_systems[2].next_to(number_systems[3][1], RIGHT)
        number_systems[4].next_to(number_systems[5][1], RIGHT)
        number_systems.shift(3 * RIGHT + DOWN)
        boundary = SurroundingRectangle(number_systems, color = BLUE_B, stroke_width = 5.0, buff = 0.20)
        self.play(
            number_systems.animate,
            run_time = 1,
            rate_func = smooth
        )
        self.wait()

        self.play(
            Create(boundary),
            run_time = 5,
            rate_func = there_and_back_with_pause
        )
        self.wait(2)

        

class CompletingSquareMethod(Scene):
    def construct(self):
        quadratic_equation = Tex(
            "$x^{2} + 2x + 2 = 0$" "\\\\",
            "$x^{2} + 2x = -2$"
        ).scale(1.5)
        quadratic_equation[1].move_to(quadratic_equation[0])
        quadratic_equation[0].to_edge(UP)
        quadratic_equation[1].to_edge(UP)
        equation = Tex(
            "$x^{2}$", "$+$", "$2x$", "$x$", "$x$", "$1$", "$1$", "=", "$-2$", "$-1$", "+"
        )
        square = Square(side_length = 2, color = BLUE, fill_color = BLUE, fill_opacity = 0.5)
        square.shift(2 * LEFT)
        rectangle = Rectangle(height = 2.0, width = 1.0, color = GREY_BROWN, fill_color = GREY_BROWN, fill_opacity = 0.5)
        rectangle.next_to(square, RIGHT, buff = 0.75)
        rect_1 = Rectangle(height = 2.0, width = 0.5, color = GREY_BROWN, fill_color = GREY_BROWN, fill_opacity = 0.5)
        rect_1.next_to(square, RIGHT, buff = 0.0)
        rect_2 = Rectangle(height = 2.0, width = 0.5, color = GREY_BROWN, fill_color = GREY_BROWN, fill_opacity = 0.5)
        rect_2.next_to(rect_1, RIGHT, buff = 0.10)
        small_square = Square(side_length = 0.5, color = YELLOW, fill_color = YELLOW, fill_opacity = 0.5)
        small_square.next_to(rect_1, RIGHT, buff = 0.75)
        
        equal_square = Square(side_length = 1, color = RED_A, fill_color = RED_A, fill_opacity = 0.5)
        equal_square.next_to(square, RIGHT, buff = 3.5)
        small_sq_copy = small_square.copy()
        small_sq_copy.next_to(equal_square, RIGHT, buff = 0.75)
        negative_area = Square(side_length = 1.25, color = RUBY, fill_color = RUBY, fill_opacity = 0.5).move_to(equal_square)
        
        equation[0].move_to(square)
        equation[1].next_to(square, RIGHT)
        equation[2].move_to(rectangle)
        equation[3].move_to(rect_1)
        equation[6].move_to(small_sq_copy)
        equation[7].next_to(rectangle, RIGHT, buff = 0.35)
        equation[8].move_to(equal_square)
        equation[9].move_to(negative_area)
        equation[10].next_to(equal_square, RIGHT)

        self.play(
            Write(quadratic_equation[0])
        )
        self.play(
            quadratic_equation[0].animate.become(quadratic_equation[1]),
            rate_func = smooth
        )
        self.wait()
        self.play(
            DrawBorderThenFill(square)
        )
        self.wait()
        self.play(
            Write(equation[0]),
            rate_func = smooth
        )
        self.play(
            Write(equation[1], rate_func = smooth),
            Write(equation[7], rate_func = smooth),
            DrawBorderThenFill(rectangle),
            DrawBorderThenFill(equal_square)
        )
        self.play(
            Write(equation[2]),
            Write(equation[8]),
            rate_func = smooth
        )
        rectangle.add(equation[2])
        self.play(
            FadeOut(equation[1]),
            rectangle.animate.next_to(square, RIGHT, buff = 0.0),
            rate_func = smooth
        )
        self.wait()
        self.play(
            TransformMatchingShapes(rectangle, VGroup(rect_1, rect_2)),
            rate_func = smooth
        )
        self.play(
            rect_2.animate.rotate(PI/2).next_to(square, DOWN, buff = 0.0),
            rate_func = smooth
        )
        equation[1].next_to(rect_1, RIGHT)
        equation[4].move_to(rect_2)
        self.play(
            Write(equation[3:5]),
            rate_func = smooth
        )
        self.wait()
        self.play(
            Write(equation[1], rate_func = smooth),
            DrawBorderThenFill(small_square),
            Write(equation[10], rate_func = smooth),
            DrawBorderThenFill(small_sq_copy)
        )
        equation[5].move_to(small_square)
        self.play(
            Write(equation[5:7]),
            rate_func = smooth
        )
        self.wait()
        small_square.add(equation[5])
        self.play(
            FadeOut(equation[1], equation[6], equation[8]),
            TransformMatchingShapes(VGroup(equal_square, small_sq_copy, equation[10]), negative_area),
            small_square.animate.next_to(rect_1, DOWN, buff = 0.0)
        )
        self.play(
            Write(equation[9]),
            equation[7].animate.shift(0.25 * LEFT).scale(1.25),
            rate_func = smooth
        )
        self.wait(2)

        complete_square = SurroundingRectangle(VGroup(square, rect_1, rect_2, small_square), color = WHITE, buff = 0.0)
        negative_sq = SurroundingRectangle(negative_area, color = WHITE, buff = 0.0)

        self.play(
            Create(complete_square),
            Create(negative_sq),
            rate_func = smooth
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
        bombelli = get_figure(names[3], portraits[3])
        bombelli.to_edge(LEFT)
        bombelli.shift(DOWN)

        self.play(
            Write(casus_irreducibilis)
        )
        self.wait()
        self.play(
            Write(translation)
        )
        self.wait(2)

        self.play(
            FadeIn(bombelli),
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
        euler.to_edge(3.0 * RIGHT)
        self.play(
            FadeIn(euler, shift = UP)
        )
        self.wait()



class EulersManuscript(ExternallyAnimatedScene):
    pass



class EulersIdentity(Scene):
    def construct(self):
        plane = argand_plane(3.5, 3.5)
        plane.add_coordinates()

        self.play(
            Create(plane)
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
        modulus.scale(0.8)
        modulus.add_background_rectangle()
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



def list_add(l1,l2):
    return [l1[x]+l2[x] for x,_ in enumerate(l1)]


class BombelliPoem(Scene):
    def construct(self):
        plusominus=Tex('Plus of Minus ','$\displaystyle =\ i$' ).align_on_border(UP*2)
        minusominus = Tex('Minus of Minus ', '$\displaystyle =\ -i$').next_to(plusominus,DOWN)
        bombelli_poem=Tex('Plus by plus of minus, makes plus of minus\\\\',
                            'Minus by plus of minus, makes minus of minus\\\\',
                            'Plus by minus of minus, makes minus of minus\\\\',
                            'Minus by minus of minus, makes plus of minus\\\\',
                            'Plus of minus by plus of minus, makes minus\\\\',
                            'Plus of minus by minus of minus, makes plus\\\\',
                            'Minus of minus by plus of minus, makes plus\\\\',
                            'Minus of minus by minus of minus makes minus').scale(0.75).shift(DOWN)
        interpr=MathTex(r'(+1) \cdotp  i   = +i\\',
                        r'(-1) \cdotp  i   = -i\\',
                        r'(+1) \cdotp(-i)  = -i\\',
                        r'(-1) \cdotp(-i)  = +i\\',
                        r'(+i) \cdotp(i)   = -1\\',
                        r'(+i) \cdotp(-i)  =  1\\',
                        r'(-i) \cdotp(+i)  =  1\\',
                        r'(-i) \cdotp(-i)  = -1').scale(0.75).shift(DOWN)
        defs=VGroup(plusominus,minusominus).set_color(TEX_HCOLOR)
        self.play(Write(bombelli_poem),rate_func=smooth,run_time=6)
        self.play(Write(defs), rate_func=smooth, run_time=2)
        self.wait()
        for i in range(0,len(bombelli_poem)):
            self.play(ReplacementTransform(bombelli_poem[i],interpr[i]),rate_func=smooth,run_time=2)
        self.wait()

        

class Introduction(Scene):
    def basic_defs(self):
        def_cn = Tex(r"""A complex number is any number of the form \\""", r""" $\displaystyle
                z=a+ib$""", r"""\\ where $\displaystyle a$ and $\displaystyle b$ are real numbers and""",
                     r"""$\displaystyle \ i$ """, r"""is the imaginary unit.""")
        def_cn[1::2].set_color(TEX_HCOLOR)
        def_im = MathTex("i=\sqrt{-1}").set_color(MATH_HCOLOR).next_to(def_cn.get_center(),2*DOWN)

        def_alt = Tex(r"""Complex Numbers can also be represented as a vector """, r"""$\displaystyle z=re^{i\theta }$"""
                      , r"\\ where ", "$\displaystyle r=\sqrt{a^{2} +b^{2}}$", r" is the magnitude of the vector and \\",
                      r"""$\displaystyle \theta =\arctan\left(\frac{b}{a}\right)$""", r""" is the angle with 
                      respect to $x$-axis.""")
        def_alt[1::2].set_color(TEX_HCOLOR)

        # Argand Plane.
        plane=argand_plane(6.5,3.5).add_coordinates().scale(0.6).align_on_border(DOWN)
        vect=Arrow(plane.n2p(0),plane.n2p(4+2j),buff=0,stroke_width=3,tip_length=0.2).set_color(VECTOR_COLOR[2])
        lbl_mag=MathTex("r").scale(0.5).next_to(vect.get_center(),UP)
        ang=Angle(Line(plane.n2p(0),plane.n2p(5)),Line(plane.n2p(0),plane.n2p(4+2j)),radius=0.5,stroke_width=2)
        lbl_ang=MathTex(r"\theta ").scale(0.5).next_to(ang.get_center(),0.5*RIGHT)
        x_proj = DashedLine(start=plane.n2p(0),end=plane.n2p(4)).set_color(X_AXIS_COLOR)
        y_proj = DashedLine(start=plane.n2p(4), end=plane.n2p(4 + 2j)).set_color(Y_AXIS_COLOR)
        x_lbl = MathTex("a").scale(0.5).next_to(x_proj.get_center(),0.7*DOWN)
        y_lbl = MathTex("b").scale(0.5).next_to(y_proj.get_center(), 0.7*RIGHT)

        self.play(Write(def_cn,rate_func=smooth,run_time=3))
        self.play(MoveAlongPath(def_cn, Line([0, 0, 0], [0, 1, 0])))
        self.play(Write(def_im,rate_func=smooth,run_time=2))
        self.wait()
        self.play(FadeOut(def_im,def_cn))
        self.play(Write(def_alt,rate_func=smooth,run_time=3))
        self.play(ScaleInPlace(def_alt,0.75))
        self.play(MoveAlongPath(def_alt,Line([0,0,0],[0,2,0])))
        self.wait()
        self.play(Create(plane))
        self.play(GrowArrow(vect),FadeIn(VGroup(lbl_mag,ang,lbl_ang)))
        self.play(Create(VGroup(x_lbl,x_proj,y_lbl,y_proj)))
        self.wait(2)
        self.play(FadeOut(VGroup(def_alt,vect,lbl_mag,ang,lbl_ang,x_lbl,x_proj,y_lbl,y_proj,plane)))
        self.wait()

    def operations(self):
        head_prp = Tex(r"Arithmetic Operations").scale(1.5)
        text_asm = MathTex(r""" \begin{array}{l}
        z_{1} =a_{1} +ib_{1} =r_{1} e^{i\theta _{1}}\\
        z_{2} =a_{2} +ib_{2} =r_{2} e^{i\theta _{2}}
        \end{array}""").set_color(MATH_HCOLOR).scale(0.75).move_to(([-4.5, 2.1, 0]))
        head_addsub = Tex(r"""Addition""").next_to(text_asm,1.5*DOWN)
        plane=argand_plane(6.5,3.5).add_coordinates().scale(0.7).next_to(text_asm,DR)
        vec1=Arrow(plane.n2p(0),plane.n2p(1+2j),tip_length=0.15,stroke_width=3,buff=0).set_color(VECTOR_COLOR[4])
        vec11 = Arrow(plane.n2p(1-1j), plane.n2p(2 + 1j), tip_length=0.15, stroke_width=3, buff=0).set_color(VECTOR_COLOR[4])
        vec2 = Arrow(plane.n2p(0),plane.n2p(1-1j), tip_length=0.15, stroke_width=3,buff=0).set_color(VECTOR_COLOR[2])
        vec22 = Arrow(plane.n2p(1 + 2j), plane.n2p(2 + 1j), tip_length=0.15, stroke_width=3, buff=0).set_color(VECTOR_COLOR[2])
        vec3 = Arrow(plane.n2p(0),plane.n2p(2+1j), tip_length=0.15, stroke_width=3,buff=0).set_color(VECTOR_COLOR[1])
        vec4 = Arrow(plane.n2p(0), plane.n2p(3+1j), tip_length=0.15, stroke_width=3,buff=0).set_color(VECTOR_COLOR[1])

        lblv1 = MathTex("( a_{1} ,b_{1})").scale(0.5).next_to(vec1.get_end(), RIGHT)
        lblv2 = MathTex("( a_{2} ,b_{2})").scale(0.5).next_to(vec2.get_end(), RIGHT)
        lblv3 = MathTex("( a_{1}+a_{2} ,b_{1}+b_{2})").scale(0.5).next_to(vec3.get_end(), RIGHT)

        magv1 = MathTex("r_{1}").scale(0.5).next_to(vec1.get_end(), 0.1*UR)
        magv2 = MathTex("r_{2}").scale(0.5).next_to(vec2.get_end(), 0.1*UR)
        magv4 = MathTex("r_{1}r_{2}") .scale(0.5).next_to(vec4.get_end(), 0.1*UR)
        angv1= Angle(Line(plane.n2p(0),plane.n2p(1)),Line(plane.n2p(0),plane.n2p(1+2j)),radius=0.4,stroke_width=2)
        angv2 = Angle(Line(plane.n2p(0), plane.n2p(1 - 1j)),Line(plane.n2p(0),plane.n2p(1)), radius=0.5,stroke_width=2)
        angv4 = Angle(Line(plane.n2p(0), plane.n2p(1)), Line(plane.n2p(0), plane.n2p(3 + 1j)), radius=1,stroke_width=2)
        valv1 = MathTex(r"\theta_{1}").scale(0.5).next_to(angv1.get_top(),0.5*RIGHT)
        valv2 = MathTex(r"\theta_{2}").scale(0.5).next_to(angv2.get_bottom(),0.5*RIGHT)
        valv4 = MathTex(r"\theta_{1}+\theta_{2}").scale(0.5).next_to(angv4, 0.5 * RIGHT)
        mul_grp=VGroup(magv1,magv2,angv1,angv2,valv1,valv2)
        mul2_grp=VGroup(magv4,angv4,valv4)

        text_addsub1 = MathTex(r"""z_{1} + z_{2}""").scale(0.75).next_to(head_addsub,DOWN)
        text_addsub2 = MathTex(r"""( a_{1} +ib_{1}) + ( a_{2} +ib_{2})""").scale(0.75).next_to(head_addsub,DOWN)
        text_addsub3 = MathTex(r"""( a_{1} + a_{2}) +i( b_{1} + b_{2})""").scale(0.75).next_to(head_addsub,DOWN)

        head_mul = Tex(r"""Multiplication""").next_to(text_addsub3,1.5*DOWN)
        text_mul1 = MathTex("z_{1} \cdotp z_{2}").next_to(head_mul,DOWN).scale(0.75)
        text_mul2 = MathTex(r"r_{1}e^{i\theta_{1}} \cdotp r_{2}e^{i\theta_{2}}").scale(0.75).next_to(head_mul,DOWN)
        text_mul3 = MathTex(r"r_{1}r_{2}e^{i(\theta_{1}+\theta_{2})}").scale(0.75).next_to(head_mul,DOWN)

        head_comm=Tex("Commutativity").move_to([0 ,3 ,0])
        text_addsub4=MathTex("z_{1}+z_{2}=z_{2}+z_{1}").scale(0.75).move_to(text_addsub3)
        text_mul4 = MathTex("z_{1} \cdotp z_{2}=z_{2}\cdotp z_{1}").scale(0.75).move_to(text_mul3)

        self.play(Write(head_prp,rate_func=smooth,run_time=2))
        self.play(ScaleInPlace(head_prp, 0.8))
        self.play(MoveAlongPath(head_prp, Line([0, 0, 0], [0, 3, 0])))
        self.play(Write(text_asm,rate_func=smooth,run_time=2))
        self.play(Write(head_addsub,rate_func=smooth,run_time=2))
        self.play(Create(VGroup(plane,vec1,vec2,lblv1,lblv2)))
        self.play(Write(text_addsub1,rate_func=smooth,run_time=2))
        self.wait()
        self.play(FadeTransform(text_addsub1, text_addsub2))
        self.wait(2)
        self.play(FadeOut(lblv2))
        self.play(TransformMatchingShapes(vec2, vec22,True))
        self.wait(2)
        self.play(TransformMatchingShapes(text_addsub2, text_addsub3))
        self.play(Indicate(text_addsub3, color=MATH_HCOLOR))
        self.wait()
        self.play(GrowArrow(vec3))
        self.play(Write(lblv3))
        self.wait()
        self.play(FadeOut(VGroup(vec3,lblv3,lblv1)))
        self.play(TransformMatchingShapes(vec22,vec2,True))

        self.play(Create(mul_grp))
        self.play(Write(head_mul,rate_func=smooth,run_time=2))
        self.play(Write(text_mul1,rate_func=smooth,run_time=2))
        self.wait()
        self.play(FadeTransform(text_mul1, text_mul2,run_time=2))
        self.wait()
        self.play(TransformMatchingShapes(text_mul2, text_mul3))
        self.play(Indicate(text_mul3,color=MATH_HCOLOR))
        self.play(GrowArrow(vec4))
        self.play(Write(mul2_grp,rate_func=smooth,run_time=2))
        self.wait()
        self.play(FadeOut(mul2_grp), FadeOut(mul_grp),FadeOut(vec4))
        # Commutativity.

        self.play(FadeTransform(head_prp, head_comm))
        self.play(FadeTransform(text_addsub3, text_addsub4))
        self.play(FadeTransform(text_mul3, text_mul4))
        self.play(Indicate(text_addsub4,color=MATH_HCOLOR))
        self.play(Create(vec22),Create(vec11))
        self.play(FadeIn(VGroup(lblv2,lblv1)))
        self.play(GrowArrow(vec3),FadeIn(lblv3))
        self.play(Indicate(text_mul4,color=MATH_HCOLOR))



    def construct(self):
        self.basic_defs()
        self.operations()


class ArgandPlane(Scene):
    def construct(self):
        title = Tex(r"Complex Plane")
        title.scale(1.5)
        title.to_edge(UP)
        plane = argand_plane(6.5, 3.5)
        plane.add_coordinates()
        plane.set_height(6)
        plane.next_to(title, DOWN)
        c = Dot(plane.n2p(0), color = DOT_COLOR)
        d1 = glow_dot(plane.n2p(4 + 1j))
        d2 = glow_dot(plane.n2p(-4 + 2j))
        p1=Arrow(plane.n2p(-0.25 - 0.05j), plane.n2p(4.27 + 1.06j), color = VECTOR_COLOR[1], stroke_width = 3)
        lblp1 = MathTex("4+i").scale(0.75).next_to(p1, UR, 0.1)
        lblp1.add_background_rectangle()

        p2 = Arrow(plane.n2p(0.25 - 0.10j), plane.n2p(-4.25 + 2.14j), color = VECTOR_COLOR[1], stroke_width = 3)
        lblp2 = MathTex("-4+2i").scale(0.75).next_to(p2, UL, 0.1)
        lblp2.add_background_rectangle()

        self.play(
            Write(title),
            Create(plane),
            run_time = 2,
            rate_func = smooth
        )
        self.play(Create(c))
        self.play(GrowArrow(p1))
        self.play(
            FadeIn(lblp1, d1)
        )
        self.play(FadeOut(d1))
        self.wait(2)
        self.play(FadeOut(lblp1))
        self.play(ReplacementTransform(p1, p2))
        self.play(
            FadeIn(lblp2, d2)
        )
        self.play(FadeOut(d2))
        self.wait(2)
        self.play(
            FadeOut(title, c, p2, lblp2),
            rate_func = smooth
        )
        self.play(
            ShrinkToCenter(plane),
            rate_func = smooth
        )
        self.wait()
        
        
        
        
        
        
       
