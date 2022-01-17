from manim import Scene

class ExternallyAnimatedScene(Scene):
    def construct(self):
        raise Exception("Externally Animated!")
