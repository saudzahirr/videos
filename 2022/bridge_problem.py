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
