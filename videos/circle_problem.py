from manimce import *

"""
Poem on Moser's Circle Problem by 3blue1brown
https://www.3blue1brown.com/blog/poems#mosers-circle-problem
"""

class CircleProblem(Scene):
    poem = """
    Take two points on a circle,
    and draw a line straight through.
    The space that was encircled
    is divided into two.

    To these points add a third one,
    which gives us two more chords.
    The space through which these lines run
    has been fissured into four.

    Continue with a fourth point,
    and three more lines drawn straight.
    The new number of disjoint
    regions sums, in all, to eight.
    
    A fifth point and its four lines
    support this pattern gleaned.
    Counting sections, one divines
    that there are now sixteen.
    
    This pattern here of doubling
    does seems a sturdy one.
    But one more step is troubling
    as the sixth gives thirty-one.
    """
    def construct(self):
        poem = Tex(self.poem)
        self.play(
            Write(poem)
        )
