from manimce import *



class Introduction(Scene):
    def construct(self):
        euler = ImageMobject(get_portrait("Leonhard_Euler"))
        self.play(
            FadeIn(euler)
        )
        self.wait()
