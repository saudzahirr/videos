from manimce import *


class Introduction(Scene):
    def construct(self):
        vertices = ['A', 'B', 'C', 'D']
        edges = [('A', 'B'), ('B', 'D'), ('D', 'C'), ('C', 'A')]
        graph = Graph(
            vertices, edges, layout = "circular",
            layout_scale = 3, labels = True
        )
        self.play(
            Create(graph)
        )
        self.wait()
