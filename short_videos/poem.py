from manimce import *

"""
Poem 1-1+1-1+... by 3blue1brown.
https://www.3blue1brown.com/blog/poems
"""

class MathPoetry(Scene):
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
        poem = self.poem
        speech_bubble = SpeechBubble()

        self.play(
            DrawBorderThenFill(speech_bubble)
        )

        for lines in poem:
            lines.scale(0.85)
            lines.move_to(speech_bubble)
            lines.shift(0.566*UP)
            for line in lines:
                self.play(
                    Write(line),
                    lag_ratio = 0.05,
                    run_time = 3,
                    rate_func = smooth
                )
                self.wait(0.75)

            self.wait()
            self.play(
                FadeOut(lines),
                #speech_bubble.animate.flip(UP)
            )
        
        self.play(
            FadeOut(speech_bubble)
        )
        self.clear()
