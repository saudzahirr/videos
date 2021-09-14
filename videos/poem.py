from manimce import *

"""
Poem 1-1+1-1+... by 3blue1brown.
https://www.3blue1brown.com/blog/poems
"""

class MathPoetry(Scene):
    poem = Tex(
        "When one takes one from one",
        "plus one from one plus one",
        "and on and on but ends",
        "anon then starts again,",
        "then some sums sum to one,",
        "to zero other ones.",
        "One wonders who'd have won",
        "had stopping not been done;",
        "had he summed every bit",
        "until the infinite.",
        
        "Lest you should think that such",
        "less well-known sums are much",
        "ado about nonsense",
        "I do give these two cents:",
        "The universe has got",
        "an answer which is not",
        "what most would first surmise,",
        "it is a compromise,",
        "and though it seems a laugh",
        "the universe gives “half”."
    )
    def construct(self):
        logo_transformation(self)
        poem = self.poem
        poem.arrange(DOWN)
        poem[0].move_to(ORIGIN)
        poem[1:].move_to(poem[0])

        for line in poem:
            self.play(
                Write(line),
            )
            self.wait()
            self.play(
                FadeOut(line, shift = UP)
            )
            
        self.wait()
