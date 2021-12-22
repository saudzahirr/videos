from manimce import *

"""
Poem on Moser's Circle Problem by 3blue1brown.
https://www.3blue1brown.com/blog/poems#mosers-circle-problem
"""


class CircleProblem(Scene):
    poem = VGroup(
    Tex(
        "Take two points on a circle," "\\\\",
        "and draw a line straight through." "\\\\",
        "The space that was encircled" "\\\\",
        "is divided into two."
    ),

    Tex(
        "To these points add a third one," "\\\\",
        "which gives us two more chords." "\\\\",
        "The space through which these lines run" "\\\\",
        "has been fissured into four."
    ),

    Tex(
        "Continue with a fourth point," "\\\\",
        "and three more lines drawn straight." "\\\\",
        "The new number of disjoint" "\\\\",
        "regions sums, in all, to eight."
    ),

    Tex(
        "A fifth point and its four lines" "\\\\",
        "support this pattern gleaned." "\\\\",
        "Counting sections, one divines" "\\\\",
        "that there are now sixteen."
    ),

    Tex(
        "This pattern here of doubling" "\\\\",
        "does seems a sturdy one." "\\\\",
        "But one more step is troubling" "\\\\",
        "as the sixth gives thirty-one."
    )
    )
    def construct(self):
        self.add_sound("youtube 2.wav", time_offset = 6)
        # logo_transformation(self)
        aljabrak(self)
        
        
        poem = self.poem
        poem.set_color(BLUE_B)
        title = Tex("Moser's Circle Problem")
        title.scale(1.5)
        title.to_edge(UP)
        circle = Circle(radius = 2, color = YELLOW)
        circle.to_edge(LEFT)
        points = circle.get_points_defining_boundary()
        poem.next_to(circle, 2 * RIGHT)

        line_1 = Line(points[0], points[5], color = GREY_C)
        line_2 = Line(points[5], points[9], color = GREY_C)
        line_3 = Line(points[9], points[0], color = GREY_C)
        line_4 = Line(points[13], points[0], color = GREY_C)
        line_5 = Line(points[5], points[13], color = GREY_C)
        line_6 = Line(points[9], points[13], color = GREY_C)
        line_7 = Line(points[3], points[0], color = GREY_C)
        line_8 = Line(points[3], points[5], color = GREY_C)
        line_9 = Line(points[3], points[9], color = GREY_C)
        line_10 = Line(points[3], points[13], color = GREY_C)
        line_11 = Line(points[11], points[13], color = GREY_C)
        line_12 = Line(points[11], points[9], color = GREY_C)
        line_13 = Line(points[11], points[5], color = GREY_C)
        line_14 = Line(points[11], points[3], color = GREY_C)
        line_15 = Line(points[11], points[0], color = GREY_C)

        self.play(
            Create(circle),
            Write(
                title,
                run_time = 3,
                rate_func = smooth,
                lag_ratio = 0.1
            )
        )
        self.wait()

        dots = Group()
        for point in points:
            dots.add(Dot(point, color = BLUE_C))

        #self.add_foreground_mobject(dots)
        self.play(
            GrowFromPoint(line_1, points[0]),
            Create(dots[0]),
            Create(dots[5]),
            FadeIn(poem[0]),
            run_time = 3,
            rate_func = smooth
        )
        self.wait(5)

        self.play(
            GrowFromPoint(line_2, points[5]),
            GrowFromPoint(line_3, points[9]),
            Create(dots[9]),
            TransformMatchingTex(poem[0], poem[1]),
            run_time = 2,
            rate_func = smooth
        )
        self.wait(5)

        self.play(
            GrowFromPoint(line_4, points[13]),
            GrowFromPoint(line_5, points[5]),
            GrowFromPoint(line_6, points[9]),
            Create(dots[13]),
            TransformMatchingTex(poem[1], poem[2]),
            run_time = 2,
            rate_func = smooth
        )
        self.wait(5)

        self.play(
            GrowFromPoint(line_7, points[3]),
            GrowFromPoint(line_8, points[3]),
            GrowFromPoint(line_9, points[3]),
            GrowFromPoint(line_10, points[3]),
            Create(dots[3]),
            TransformMatchingTex(poem[2], poem[3]),
            run_time = 2,
            rate_func = smooth
        )
        self.wait(5)

        self.play(
            GrowFromPoint(line_11, points[11]),
            GrowFromPoint(line_12, points[11]),
            GrowFromPoint(line_13, points[11]),
            GrowFromPoint(line_14, points[11]),
            GrowFromPoint(line_15, points[11]),
            Create(dots[11]),
            TransformMatchingTex(poem[3], poem[4]),
            run_time = 2,
            rate_func = smooth
        )
        self.wait(5)
