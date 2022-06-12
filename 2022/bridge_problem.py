"""
Seven Bridges of Königsberg Problem.
"""

from manimce import *



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
