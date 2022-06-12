"""
Seven Bridges of Königsberg Problem.
"""

from manimce import *



class Introduction(Scene):
    def construct(self):
        image = ImageMobject(get_image("Königsberg_Karte.jpg"))
        image.set_height(FRAME_HEIGHT)
        image.set_width(FRAME_WIDTH)

        full_rect = FullScreenRectangle()
        full_rect.scale(1.25)
        full_rect.flip()
        full_rect.set_fill(BLACK, opacity = 0.6)

        bridge_diagram = SVGMobject(get_svg("bridge.svg"))
        bridge_diagram.set_stroke(WHITE, 2)
        bridge_diagram.scale(0.85)
        bridge_diagram.shift(DOWN)
        bridge_diagram.shift(0.35 * LEFT)
        bridge_diagram.rotate(-10 * DEGREES)

        title = Tex("Seven Bridges of Königsberg.")
        title.set_color(YELLOW)
        title.set_stroke(BLACK, 3, background = True)
        title.scale(1.5)
        title.to_edge(UP)

        problem = Tex(
            "A walk through the city that would cross" "\\\\",
            "each of those bridges once and only once."
        )
        problem.set_stroke(BLACK, 3, background = True)
        problem.scale(0.85)
        problem.next_to(title, 3 * DOWN)


        self.add(image)
        self.wait(2)

        self.play(
            FadeIn(full_rect),
            rate_func = smooth
        )

        self.add_foreground_mobjects(title)
        self.play(
            Write(title),
            run_time = 6,
            rate_func = smooth
        )
        self.wait(3)

        self.add_foreground_mobjects(bridge_diagram, problem)
        self.play(
            Write(bridge_diagram),
            Write(problem),
            run_time = 8,
            rate_func = smooth
        )
        self.wait(6)
        self.clear()
        logo(self)
        
        
 
class History(Scene):
    def construct(self):
        euler_portrait = ImageMobject(get_portrait("Euler3.jpg"))
        euler_portrait.scale(0.65)
        euler_portrait.add(SurroundingRectangle(euler_portrait, WHITE, buff = 0.0, stroke_width = 2))
        euler_portrait.to_edge(LEFT)
        leonhard_euler = Tex("Leonhard Euler")
        leonhard_euler.set_width(euler_portrait.get_width())
        leonhard_euler.next_to(euler_portrait, DOWN)


        ehler_portrait = Rectangle(height = 3, width = 2.5, stroke_color = WHITE, fill_color = BLACK, fill_opacity = 0.8)
        ehler_portrait.add(Tex("No Image.").scale(0.85).set_color(GREY_B))
        ehler_portrait.set_height(euler_portrait.get_height())
        ehler_portrait.set_width(euler_portrait.get_width())
        ehler_portrait.to_edge(RIGHT)
        carl_ehler = Tex("Carl Gottlieb Ehler")
        carl_ehler.set_width(ehler_portrait.get_width())
        carl_ehler.next_to(ehler_portrait, DOWN)

        year = Tex("1736")
        year.scale(1.35)
        year.to_edge(UL)
        self.add(year)

        # calligraphy = TexTemplate(
        #     preamble = r"""
        #     \usepackage{calligra}
        #     """
        # )

        # letters = VGroup(
        #     Tex(
        #         "Ehler: You would render to me and our friend Kuhn a most" "\\\\",
        #         "valuable service, putting us greatly in your debt, most" "\\\\",
        #         "learned sir, if you would send us the solution, which" "\\\\",
        #         "you know well, to the problem of the seven Konigsberg bridges" "\\\\",
        #         "together with a proof. It would prove to an outstanding example" "\\\\",
        #         "of the calculus of position [calculi situs] worthy of your" "\\\\",
        #         "great genius. I have added a sketch of the said bridges.",
        #         tex_template = calligraphy
        #     ),
        #     Tex(
        #         "Euler: Thus you see, most noble sir, how this type of" "\\\\",
        #         "solution bears little relationship to mathematics and I do not" "\\\\",
        #         "understand why you expect a mathematician to produce it" "\\\\",
        #         "rather than anyone else, for the solution is based on" "\\\\",
        #         "reason alone, and its discovery does not depend on any" "\\\\",
        #         "mathematical principle. Because of this, I do not know why" "\\\\",
        #         "even questions which bear so little relationship to mathematics" "\\\\",
        #         "are solved more quickly by mathematicians than by others." "\\\\",
        #         "In the meantime most noble sir, you have a assigned this question" "\\\\",
        #         "to the geometry of position but I am ignorant as to what this new" "\\\\",
        #         "discipline involves, and as to which types of problem Leibniz and" "\\\\",
        #         "Wolff expected to see expressed this way.",
        #         tex_template = calligraphy
        #     )
        # )

        # for letter in letters:
        #     letter.scale(0.5)
        
        eulers_letter = Tex(
            "Euler: Thus you see, most noble sir," "\\\\",
            "how this type of solution bears little" "\\\\",
            "relationship to mathematics", "...",
        )
        eulers_letter.scale(0.75)


        self.play(
            FadeIn(
                Group(ehler_portrait, euler_portrait),
                shift = UP
            ),
            FadeIn(
                VGroup(carl_ehler, leonhard_euler)
            ),
            rate_func = smooth
        )
        self.wait(4)

        self.play(
            Write(eulers_letter),
            run_time = 3,
            rate_func = smooth
        )
        self.wait(2)

        self.play(
            eulers_letter[1:3].animate.set_color(YELLOW),
            run_time = 4,
            lag_ratio = 0.5,
            rate_func = smooth
        )
        self.wait(4)

        self.play(
            FadeOut(eulers_letter),
            FadeOut(
                Group(ehler_portrait, carl_ehler)
            ),
            rate_func = smooth
        )
        self.wait()


        # Geometry of Position (Graph Theory)

        title = Tex(
            "Geometry of Position", "$^{*}$"
        )
        title[0].set_color(BLUE)
        title.scale(1.5)
        title.to_edge(UP)

        label = Tex("$^{*}$Now known as graph theory.")
        label.set_width(6)
        label.scale(0.55)
        label.to_edge(DR)

        self.play(
            Write(title[0]),
            run_time = 2,
            rate_func = smooth
        )
        self.wait(2)

        self.play(
            Write(title[1]),
            Write(label),
            run_time = 2,
            rate_func = smooth
        )
        self.wait(2)

        self.play(
            FadeOut(label, title[1]),
            rate_func = smooth
        )

        manuscipts = Group(
            ImageMobject(get_image("Solutio_problematis_ad_geometriam_situs_pertinentis,_Fig._1.png")),
            ImageMobject(get_image("Solutio_problematis_ad_geometriam_situs_pertinentis,_Fig._2.png"))
        )
        manuscipts.arrange(DOWN, buff = 0.5)
        manuscipts.next_to(euler_portrait, RIGHT, buff = 2.0)

        for manuscipt in manuscipts:
            manuscipt.scale(0.75)

        seminal_paper = Tex(
            "\\textit{Solutio problematis ad geometriam situs pertinentis.}" "\\\\",
            "(The solution of a problem relating to the geometry of position)"
        )
        seminal_paper.scale(0.75)
        seminal_paper[1].scale(0.6, about_edge = UP)
        # seminal_paper.set_width(manuscipts[1].get_width())
        seminal_paper.next_to(manuscipts[1], DOWN)

        self.play(
            FadeIn(manuscipts),
            Write(seminal_paper),
            run_time = 2,
            rate_func = smooth
        )
        self.wait(2)
        
        
        
class EulersSolution(Scene):
    def construct(self):
        image = ImageMobject(get_image("Konigsberg.jpg"))
        image.set_height(FRAME_HEIGHT)
        image.set_width(FRAME_WIDTH)

        full_rect = FullScreenRectangle()
        full_rect.scale(1.25)
        full_rect.flip()
        full_rect.set_fill(BLACK, opacity = 0.6)

        self.add(image)
        self.play(
            FadeIn(full_rect),
        )
        self.wait()

        points = [[-1.5, 0, 0], [0, -1.5, 0], [0, 1.5, 0], [1.5, 0, 0]]
        dots = VGroup()
        labels = Group()
        
        for point in points:
            dots.add(
                Dot(point, color = YELLOW)
            )

        for dot, pos, text in zip(dots, [LEFT, DOWN, UP, RIGHT], ["A", "B", "C", "D"]):
            labels.add(Tex(text).next_to(dot, pos))
        
        for label in labels:
            label.set_stroke(BLACK, 3, background = True)

        
        paths = VGroup(
            Line(start = [-1.5, 0, 0], end = [1.5, 0, 0]),
            Line(start = [1.5, 0, 0], end = [0, 1.5, 0]),
            Line(start = [1.5, 0, 0], end = [0, -1.5, 0]),
            ArcBetweenPoints(start = [-1.5, 0, 0], end = [0, 1.5, 0]),
            ArcBetweenPoints(start = [-1.5, 0, 0], end = [0, -1.5, 0]),
            ArcBetweenPoints(start = [0, 1.5, 0], end = [-1.5, 0, 0]),
            ArcBetweenPoints(start = [0, -1.5, 0], end = [-1.5, 0, 0])
        )

        self.add_foreground_mobjects(dots, paths, labels)
        self.play(
            LaggedStart(
                *[
                    Write(path)
                    for path in paths
                ]
            ),
            LaggedStart(
                *[
                    Write(label)
                    for label in labels
                ]
            ),
            FadeIn(dots)
        )
        self.wait()
