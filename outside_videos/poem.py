from manimce import *

"""
Poem 1-1+1-1+... by 3blue1brown.
https://www.3blue1brown.com/blog/poems
"""

class MathPoetry(Scene):
    grandi_sum = Group(
        Tex(
            "$1 - 1$",
            "$  +  1$",
            "$  -  1 + 1 - 1$",
            "$  +  1 - 1$",
            "$  + \\cdots$"
        ),

        Tex(
            "${1 \\over {1  +  x}}$",
            "$  = 1 - x + x^{2} - x^{3} + O(x^{4})$" "\\\\",
            ".",
            ".",
            "."
        ),

        Tex(
            "$1 - 1 + 1^{2} - 1^{3} + \\cdots$",
            "$ = {1 \\over {1  +  1}}$" "\\\\",
            ".",
            ".",
            "."
        ),

        Tex(
            ".",
            ".",
            ".",
            "$1 - 1 + 1 - 1 + 1 - 1 + \\cdots$",
            "$ = {1 \\over 2}$"
        )
    )
    poem = Group(
        Tex(
            "When one takes one from one" "\\\\",
            "plus one from one plus one" "\\\\",
            "and on and on but ends" "\\\\",
            "anon then starts again," "\\\\",
            "then some sums sum to one,"
        ),

        Tex(
            "to zero other ones." "\\\\",
            "One wonders who'd have won" "\\\\",
            "had stopping not been done;" "\\\\",
            "had he summed every bit" "\\\\",
            "until the infinite."
        ),
        
        Tex(
            "Lest you should think that such" "\\\\",
            "less well-known sums are much" "\\\\",
            "ado about nonsense" "\\\\",
            "I do give these two cents:" "\\\\",
            "The universe has got"
        ),

        Tex(
            "an answer which is not" "\\\\",
            "what most would first surmise," "\\\\",
            "it is a compromise," "\\\\",
            "and though it seems a laugh" "\\\\",
            "the universe gives “half”."
        )
    )
    def construct(self):
        logo_transformation(self)
        self.camera.background_color = GREY_E
        speech_bubble = SpeechBubble()
        poem = self.poem
        series = self.grandi_sum
        series[1][2:].set_color(GREY_E)
        series[2][2:].set_color(GREY_E)
        series[3][:3].set_color(GREY_E)
        speech_bubble.to_edge(DOWN)

        self.play(
            DrawBorderThenFill(speech_bubble)
        )

        for lines, equations in zip(poem, series):
            lines.scale(0.85)
            lines.move_to(speech_bubble)
            lines.shift(0.566*UP)
            equations.scale(2)
            for line, equation in zip(lines, equations):
                equation.to_edge(UP)
                self.play(
                    Write(line),
                    Write(equation),
                    lag_ratio = 0.05,
                    run_time = 3,
                    rate_func = smooth
                )
                self.wait(0.75)

                if line is poem[3][4]:
                    self.play(
                        Flash(series[3][4])
                    )

            self.wait()
            self.play(
                FadeOut(lines),
                FadeOut(equations),
                run_time = 0.5
                #speech_bubble.animate.flip(UP)
            )
        
        self.play(
            FadeOut(speech_bubble),
            run_time = 0.25
        )
        self.clear()
