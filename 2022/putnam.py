from manimce import *


use_opengl_renderer = True


P = [
    0, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/10, 1/11, 1/12, 1/13,
    2/14, 2/15, 2/16, 2/17, 2/18, 2/19, 2/20, 2/21, 2/22, 2/23, 3/24, 3/25,
    3/26, 3/27, 3/28, 3/29, 3/30, 3/31, 3/32, 4/33, 4/34, 4/35, 4/36, 4/37,
    4/38, 4/39, 4/40, 4/41, 4/42, 4/43, 4/44, 4/45, 4/46, 5/47, 5/48, 5/49,
    5/50, 5/51, 5/52, 5/53, 5/54, 5/55, 5/56, 5/57, 5/58, 5/59, 5/60, 5/61,
    5/62, 6/63, 6/64, 6/65, 7/66, 7/67, 7/68, 7/69, 8/70, 8/71, 8/72, 9/73,
    9/74, 9/75, 9/76, 10/77, 10/78, 10/79, 10/80, 10/81, 11/82, 11/83, 11/84,
    11/85, 11/86, 11/87, 11/88, 12/89, 12/90, 12/91, 13/92, 13/93, 13/94, 13/95,
    13/96, 13/97, 13/98, 13/99, 13/100
]

# count = [
#     0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
#     1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0,
#     2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0,
#     3.0, 3.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0,
#     4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 5.0, 5.0, 5.0, 5.0,
#     5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
#     5.0, 5.0, 6.0, 6.0, 6.0, 7.0, 7.0, 7.0, 7.0, 8.0,
#     8.0, 8.0, 9.0, 9.0, 9.0, 9.0, 10.0, 10.0, 10.0, 10.0,
#     10.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 12.0, 12.0, 
#     12.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0
# ]


class IntroductiontoPutnam(Scene):
    def construct(self):
        pass


class Probabilities(Scene):
    def construct(self):
        self.camera.background_color = GREEN_SCREEN


        probability = dict(
            [
                (p, MathTex("\\text{Probability} = %.3f"%float(p), stroke_width = 1.15).scale(1.25))
                for p in P

                # (c, MathTex("\\text{Probability} = %.3f"%float(c / (count.index(c) + 1))))
                # for c in count
                #
                # (c, MathTex("\\text{Probability} = %.3f"%float(c / (n + 1))))
                # for c, n in zip(count, range(100))
            ]
        )

        for p in P:
            probability[p].to_corner(UL)
            
            self.add(probability[p])
            self.wait()
            self.remove(probability[p])


class QuestionPaper(ExternallyAnimatedScene):
    # Do it in editor.
    pass

class RandomTetrahedronInSphere(ExternallyAnimatedScene):
    pass
