"""
Seven Bridges of Königsberg Problem.
"""

from manimce import *
from 2022.SoME2.helpers import *
from custom.drawings import Checkmark, Brain
import numpy as np
import random



class KönigsbergProblem(Scene):
    def construct(self):
        image = ImageMobject(get_image("Königsberg_Karte.jpg"))
        image.set_height(FRAME_HEIGHT)
        image.set_width(FRAME_WIDTH)

        full_rect = FullScreenRectangle()
        full_rect.scale(1.25)
        full_rect.flip()
        full_rect.set_fill(BLACK, opacity = 0.6)

        bridge_diagram = SVGMobject(get_svg("bridge.svg"))
        bridge_diagram.set_stroke(WHITE, 2)
        bridge_diagram.scale(0.85)
        bridge_diagram.shift(DOWN)
        bridge_diagram.shift(0.35 * LEFT)
        bridge_diagram.rotate(-10 * DEGREES)

        title = Tex("Seven Bridges of Königsberg.")
        title.set_color(YELLOW)
        title.set_stroke(BLACK, 3, background = True)
        title.scale(1.5)
        title.to_edge(UP)

        problem = Tex(
            "A walk through the city that would cross" "\\\\",
            "each of those bridges once and only once."
        )
        problem.set_stroke(BLACK, 3, background = True)
        problem.scale(0.85)
        problem.next_to(title, 3 * DOWN)


        self.add(image)
        self.wait(2)

        self.play(
            FadeIn(full_rect),
            rate_func = smooth
        )

        self.add_foreground_mobjects(title)
        self.play(
            Write(title),
            run_time = 6,
            rate_func = smooth
        )
        self.wait(3)

        self.add_foreground_mobjects(bridge_diagram, problem)
        self.play(
            Write(bridge_diagram),
            Write(problem),
            run_time = 8,
            rate_func = smooth
        )
        self.wait(6)
        self.clear()
        logo(self)



class History(Scene):
    def construct(self):
        euler_portrait = ImageMobject(get_portrait("Euler3.jpg"))
        euler_portrait.scale(0.65)
        euler_portrait.add(SurroundingRectangle(euler_portrait, WHITE, buff = 0.0, stroke_width = 2))
        euler_portrait.to_edge(LEFT)
        leonhard_euler = Tex("Leonhard Euler")
        leonhard_euler.set_width(euler_portrait.get_width())
        leonhard_euler.next_to(euler_portrait, DOWN)


        ehler_portrait = Rectangle(height = 3, width = 2.5, stroke_color = WHITE, fill_color = BLACK, fill_opacity = 0.8)
        ehler_portrait.add(Tex("No Image.").scale(0.85).set_color(GREY_B))
        ehler_portrait.set_height(euler_portrait.get_height())
        ehler_portrait.set_width(euler_portrait.get_width())
        ehler_portrait.to_edge(RIGHT)
        carl_ehler = Tex("Carl Gottlieb Ehler")
        carl_ehler.set_width(ehler_portrait.get_width())
        carl_ehler.next_to(ehler_portrait, DOWN)

        year = Tex("1736")
        year.scale(1.35)
        year.to_edge(UL)
        self.add(year)

        # calligraphy = TexTemplate(
        #     preamble = r"""
        #     \usepackage{calligra}
        #     """
        # )

        # letters = VGroup(
        #     Tex(
        #         "Ehler: You would render to me and our friend Kuhn a most" "\\\\",
        #         "valuable service, putting us greatly in your debt, most" "\\\\",
        #         "learned sir, if you would send us the solution, which" "\\\\",
        #         "you know well, to the problem of the seven Konigsberg bridges" "\\\\",
        #         "together with a proof. It would prove to an outstanding example" "\\\\",
        #         "of the calculus of position [calculi situs] worthy of your" "\\\\",
        #         "great genius. I have added a sketch of the said bridges.",
        #         tex_template = calligraphy
        #     ),
        #     Tex(
        #         "Euler: Thus you see, most noble sir, how this type of" "\\\\",
        #         "solution bears little relationship to mathematics and I do not" "\\\\",
        #         "understand why you expect a mathematician to produce it" "\\\\",
        #         "rather than anyone else, for the solution is based on" "\\\\",
        #         "reason alone, and its discovery does not depend on any" "\\\\",
        #         "mathematical principle. Because of this, I do not know why" "\\\\",
        #         "even questions which bear so little relationship to mathematics" "\\\\",
        #         "are solved more quickly by mathematicians than by others." "\\\\",
        #         "In the meantime most noble sir, you have a assigned this question" "\\\\",
        #         "to the geometry of position but I am ignorant as to what this new" "\\\\",
        #         "discipline involves, and as to which types of problem Leibniz and" "\\\\",
        #         "Wolff expected to see expressed this way.",
        #         tex_template = calligraphy
        #     )
        # )

        # for letter in letters:
        #     letter.scale(0.5)
        
        eulers_letter = Tex(
            "Euler: Thus you see, most noble sir," "\\\\",
            "how this type of solution bears little" "\\\\",
            "relationship to mathematics", "...",
        )
        eulers_letter.scale(0.75)


        self.play(
            FadeIn(
                Group(ehler_portrait, euler_portrait),
                shift = UP
            ),
            FadeIn(
                VGroup(carl_ehler, leonhard_euler)
            ),
            rate_func = smooth
        )
        self.wait(4)

        self.play(
            Write(eulers_letter),
            run_time = 3,
            rate_func = smooth
        )
        self.wait(2)

        self.play(
            eulers_letter[1:3].animate.set_color(YELLOW),
            run_time = 4,
            lag_ratio = 0.5,
            rate_func = smooth
        )
        self.wait(4)

        self.play(
            FadeOut(eulers_letter),
            FadeOut(
                Group(ehler_portrait, carl_ehler)
            ),
            rate_func = smooth
        )
        self.wait()


        # Geometry of Position (Graph Theory)

        title = Tex("Geometry of Position")
        title[0].set_color(BLUE)
        title.scale(1.5)
        title.to_edge(UP)

        short_note = Tex(
            "$^{*}${It is now known as graph theory.}",
            tex_environment = "flushleft"
        )
        short_note.set_stroke(GREY_B, 1.25)
        short_note[0].set_stroke(GREY_B, 1.5)
        short_note.scale(0.45)
        short_note.to_edge(DR)

        self.play(
            Write(title),
            run_time = 2,
            rate_func = smooth
        )
        self.wait(2)

        self.add(short_note)
        self.wait(2)

        self.play(
            FadeOut(short_note),
            rate_func = smooth
        )

        manuscripts = Group(
            ImageMobject(get_image("Solutio_problematis_ad_geometriam_situs_pertinentis,_Fig._1.png")),
            ImageMobject(get_image("Solutio_problematis_ad_geometriam_situs_pertinentis,_Fig._2.png"))
        )
        manuscripts.arrange(DOWN, buff = 0.25)
        manuscripts.next_to(euler_portrait, RIGHT, buff = 2.0)

        for manuscript in manuscripts:
            manuscript.scale(0.75)

        seminal_paper = Tex(
            "\\textit{Solutio problematis ad geometriam situs pertinentis.}" "\\\\",
            "(The solution of a problem relating to the geometry of position)"
        )
        seminal_paper[0].set_color(YELLOW)
        seminal_paper.scale(0.75)
        seminal_paper[1].scale(0.85, about_edge = UP)
        seminal_paper.next_to(manuscripts[1], DOWN)

        self.play(
            FadeIn(manuscripts),
            rate_func = smooth
        )
        self.play(
            Write(seminal_paper),
            run_time = 4,
            rate_func = smooth
        )
        self.wait(4)

        self.play(
            FadeOut(title[0], year, euler_portrait, leonhard_euler, manuscripts, seminal_paper)
        )
        self.clear()



class IntroduceGraphTheory(Scene):
    def construct(self):
        # Introduction to Graph Theory.
        # question = Tex("What is a graph?", stroke_width = 2)
        # question.scale(2)
        # self.play(
        #     Write(question),
        #     run_time = 2,
        #     rate_func = smooth
        # )
        # self.wait()
        # self.clear()

        blob = VMobject()
        blob.set_fill(BLUE_E, 1)
        blob.set_stroke(width=0)
        blob.set_points_as_corners([
            (1 + 0.3 * random.random()) * p
            for p in compass_directions(12)
        ])
        blob.add_line_to(blob.get_subpaths()[-1][0])
        blob.set_height(3)
        blob.set_width(1.0)
        blob.move_to(2 * RIGHT)
        blob.apply_complex_function(lambda z: np.exp(z))
        blob.make_smooth()
        blob.rotate(90 * DEGREES)
        blob.center()
        blob.set_height(4)
        blob.insert_n_curves(50)

        outline = blob.copy()
        outline.set_fill(opacity = 0)
        outline.set_stroke(WHITE, 2)
        blob.add(outline)
        
        self.add(blob, Checkmark())
        self.wait(2)
        self.clear()

        vertices = [0, 1, 2, 3, 4, 5, 6, 7]
        edges = edges = [
            (0, 1), (0, 2), (3, 1), (3, 2),
            (4, 5), (4, 6), (7, 5), (7, 6),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]
        graph = Graph(vertices, edges, layout = "planar")
        graph.scale(1.5)
        self.play(
            Create(graph),
            rate_func = smooth,
            run_time = 2
        )
        self.wait()


class UnderstandingGraphs(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6]
        edges = [
            (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
            (6, 1), (1, 3), (2, 5), (3, 5), (3, 6), (4, 6)
        ]
        graph = Graph(vertices, edges, layout = "circular")
        graph.scale(1.5)
        self.play(
            Create(graph),
            rate_func = smooth,
            run_time = 2
        )
        self.wait()

        edges = VGroup()
        vertices = VGroup()

        for a, part in zip(range(0, 17), graph):
            if a <= 5:
                vertices.add(part)
            else:
                edges.add(part)

        vertice = glow_dot(vertices[3].get_points())
        edges[4:6].set_color(BLUE)
        self.add(vertice)
        self.wait(2)
        edges[4:6].set_color(WHITE)
        self.remove(vertice)
        self.wait(4)

        degree_of_vertices = Group(
            VGroup(edges[0], edges[5], edges[6]),
            VGroup(edges[0], edges[1], edges[7]),
            VGroup(edges[1], edges[2], edges[6], edges[8], edges[9]),
            VGroup(edges[2], edges[3], edges[10]),
            VGroup(edges[3], edges[4], edges[7], edges[8]),
            VGroup(edges[4], edges[5], edges[9], edges[10])
        )

        for vertice, deg in zip(vertices, degree_of_vertices):
            vertice = glow_dot(vertice.get_points())
            self.add(vertice)
            deg.set_color(BLUE)
            self.wait()
            deg.set_color(WHITE)
            self.remove(vertice)
        self.wait(2)



class PregelRiverScene(Scene):
    def construct(self):
        self.camera.background_color = BLUE_D
        bank1 = Rectangle(width = 2 * FRAME_WIDTH, height = 2)
        bank1.set_fill(GREY_BROWN, 1)
        bank1.set_stroke(WHITE, 2)
        bank1.to_edge(UP, buff = 0)
        bank2 = bank1.copy()
        bank2.to_edge(DOWN, buff = 0)

        islands = VGroup(
            Ellipse(),
            Ellipse()
        )

        for island in islands:
            island.scale(2)
            island.set_fill(GREY_BROWN, 1)
            island.set_stroke(WHITE, 2)
        islands.arrange(RIGHT, buff = 2)

        self.add_foreground_mobjects(bank1, bank2, islands)
        self.wait()



class EulersTheorem(Scene):
    def construct(self):
        self.camera.background_color = GREY_E
        screen = ScreenRectangle(stroke_width = 2, stroke_color = WHITE, fill_opacity = 1, fill_color = BLACK)
        screen.to_edge(UR)
        self.add(screen)
        theorem = Tex(
            "Theorem" "\\\\",
            "\\emph{A non-trivial connected graph has}" "\\\\",
            "\\emph{an Euler circuit iff each vertex}" "\\\\",
            "\\emph{has an even degree.}",
            tex_environment = "flushleft"
        )
        theorem[0].set_color(YELLOW)
        theorem[0].set_stroke(YELLOW, 1.25)
        theorem[0].scale(1.25)
        theorem[1:].scale(0.75)
        theorem[1:].next_to(theorem[0], DOWN)
        theorem.to_edge(UL)

        self.play(
            Write(theorem),
            run_time = 4,
            rate_func = smooth
        )
        self.wait(2)

        proof = Tex(
            "Proof: If $G$ has an Euler circuit" "\\\\",
            "$x_{1} x_{2} \\cdots x_{m}$ and $x$ occurs $k$ times" "\\\\",
            "in the sequence $x_{1}, x_{2}, \\cdots, x_{m}$ then" "\\\\",
            "$d(x) = 2k$.",
            tex_to_color_map = {
                "$G$" : BLUE,
                "$d(x) = 2k$" : YELLOW
            },
            tex_environment = "flushleft"
        )
        proof.scale(0.65)
        proof.to_edge(LEFT)
        proof.shift(1/2 * DOWN)

        self.play(
            Write(proof),
            run_time = 4,
            rate_func = smooth
        )
        self.wait(2)



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



class CubeScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 75 * DEGREES)
        title = Tex("Cube")
        title.set_stroke(BLACK, 5, background = True)
        title.scale(2)
        title.to_edge(UP)

        grid = number_plane(10, 10)
        grid.shift(2 * IN)

        vertex_coords = [
            [1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1],
            [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]
        ]
        edge_list=[
            [0, 1], [0, 2], [0, 4], [1, 3],
            [1, 5], [2, 6], [2, 3], [3, 7],
            [4, 6], [4, 5], [7, 5], [7, 6]
        ]
        faces_list=[
            [1, 3, 7, 5], [0, 1, 3, 2], [4, 5, 7, 6],
            [1, 5, 4, 0], [3, 7, 6, 2], [2, 0, 4, 6]
        ]
        
        cube = Polyhedron(vertex_coords, faces_list, graph_config = {"edge_config" : {"stroke_color": WHITE}})
        cube.scale(2.5)
        cube.faces.set_fill(GREY_BROWN, 0.75)
        
        self.add(grid, cube)
        self.add_fixed_in_frame_mobjects(title)
        self.begin_ambient_camera_rotation(rate = 0.1)
        self.wait(8)



class DodecahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 75 * DEGREES)
        title = Tex("Dodecahedron")
        title.set_stroke(BLACK, 5, background = True)
        title.scale(2)
        title.to_edge(UP)

        grid = number_plane(10, 10)
        grid.shift(2 * IN)

        dodecahedron = Dodecahedron(edge_length = 2.5)
        dodecahedron.faces.set_fill(BLUE_D, 0.75)

        self.add(grid, dodecahedron)
        self.add_fixed_in_frame_mobjects(title)
        self.begin_ambient_camera_rotation(rate = 0.1)
        self.wait(8)



class IcosahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 75 * DEGREES)
        title = Tex("Icosahedron")
        title.set_stroke(BLACK, 5, background = True)
        title.scale(2)
        title.to_edge(UP)

        grid = number_plane(10, 10)
        grid.shift(2 * IN)

        icosahedron = Icosahedron(edge_length = 3.75, graph_config = {"edge_config" : {"stroke_color": WHITE}})
        icosahedron.faces.set_fill(MAROON_B, 0.75)

        self.add(grid, icosahedron)
        self.add_fixed_in_frame_mobjects(title)
        self.begin_ambient_camera_rotation(rate = 0.1)
        self.wait(8)



class OctahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 75 * DEGREES)
        title = Tex("Octahedron")
        title.set_stroke(BLACK, 5, background = True)
        title.scale(2)
        title.to_edge(UP)

        grid = number_plane(10, 10)
        grid.shift(2 * IN)

        octahedron = Octahedron(edge_length = 4.5, graph_config = {"edge_config" : {"stroke_color": WHITE}})
        octahedron.faces.set_fill(PURPLE, 0.75)

        self.add(grid, octahedron)
        self.add_fixed_in_frame_mobjects(title)
        self.begin_ambient_camera_rotation(rate = 0.1)
        self.wait(8)



class TetrahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 75 * DEGREES)
        title = Tex("Tetrahedron")
        title.set_stroke(BLACK, 5, background = True)
        title.scale(2)
        title.to_edge(UP)

        grid = number_plane(10, 10)
        grid.shift(2 * IN)

        tetrahedron = Tetrahedron(edge_length = 6.5, graph_config = {"edge_config" : {"stroke_color": WHITE}})
        tetrahedron.faces.set_fill(GREEN_C, 0.75)

        self.add(grid, tetrahedron)
        self.add_fixed_in_frame_mobjects(title)
        self.begin_ambient_camera_rotation(rate = 0.1)
        self.wait(8)



class SquarePyramidScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 75 * DEGREES, theta = 30 * DEGREES)
        title = Tex("Square Pyramid")
        title.set_stroke(BLACK, 5, background = True)
        title.scale(2)
        title.to_edge(UP)

        grid = number_plane(10, 10)
        grid.shift(2 * IN)

        vertex_coords = [
            [1, 1, 0],
            [1, -1, 0],
            [-1, -1, 0],
            [-1, 1, 0],
            [0, 0, 2]
        ]
        faces_list = [
            [0, 1, 4],
            [1, 2, 4],
            [2, 3, 4],
            [3, 0, 4],
            [0, 1, 2, 3]
        ]
        square_pyramid = Polyhedron(vertex_coords, faces_list, graph_config = {"edge_config" : {"stroke_color": WHITE}})
        square_pyramid.faces.set_fill(TEAL_C, 0.75)
        square_pyramid.scale(2.5)

        self.add(grid, square_pyramid)
        self.add_fixed_in_frame_mobjects(title)
        self.begin_ambient_camera_rotation(rate = 0.1)
        self.wait(8)



class PlatonicSolidsAnimation(Scene):
    def construct(self):
        self.add(
            FullScreenRectangle(stroke_width = 2, stroke_color = GREY_D, fill_opacity = 1, fill_color = BLACK),
            Line(DOWN, UP).set_stroke(GREY_D, 4).set_height(FRAME_HEIGHT),
            Line(LEFT, RIGHT).set_stroke(GREY_D, 4).set_width(FRAME_WIDTH)
        )
        self.wait(8)



class EulerPolyhedralFormula(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 45 * DEGREES)
        cube = Cube(side_length = 3)
        cube.set_fill(BLUE, 0)
        cube.set_stroke(WHITE, 2)
        
        formula = Tex("$V - E + F = 2$")
        formula.scale(1.25)
        formula.to_edge(UL)

        explanation = Tex(
            "Dots $\\rightarrow$ Vertices" "\\\\",
            "Lines $\\rightarrow$ Edges" "\\\\",
            "Regions $\\rightarrow$ Faces",
            tex_to_color_map = {
                "V" : YELLOW,
                "E" : YELLOW,
                "F" : YELLOW
            },
            tex_environment = "flushleft"
        )
        explanation.to_edge(DL)

        example = Group(
            Count(0),
            MathTex("-"),
            Count(0),
            Tex("0", fill_opacity = 0).scale(0.25),  # Defined default text for spacing.
            MathTex("+"),
            Count(0),
            MathTex("="),
            MathTex("2")
        )

        for part in example:
            part.scale(1.25)
        example.arrange(RIGHT)
        example.next_to(formula, DOWN)

        # points = []
        # for vect in UR, UL, DR, DL:
        #     points.append(cube.get_boundary_point(vect))
        #     print(cube.get_boundary_point(vect))
        
        points = [
            [1.5, 1.5, -1.5], [-1.5, 1.5, -1.5],
            [-1.5, -1.5, -1.5], [1.5, -1.5, -1.5],
            [2.775, 2.775, -1.5], [-2.775, 2.775, -1.5],
            [-2.775, -2.775, -1.5], [2.775, -2.775, -1.5]
        ]

        dots = VGroup()
        for point in points:
            dots.add(
                Dot(point)
            )
        
        lines = VGroup(
            Line([1.5, 1.5, -1.5], [-1.5, 1.5, -1.5]),
            Line([-1.5, 1.5, -1.5], [-1.5, -1.5, -1.5]),
            Line([-1.5, -1.5, -1.5], [1.5, -1.5, -1.5]),
            Line([1.5, 1.5, -1.5], [1.5, -1.5, -1.5]),
            Line([2.775, 2.775, -1.5], [-2.775, 2.775, -1.5]),
            Line([-2.775, 2.775, -1.5], [-2.775, -2.775, -1.5]),
            Line([-2.775, -2.775, -1.5], [2.775, -2.775, -1.5]),
            Line([2.775, 2.775, -1.5], [2.775, -2.775, -1.5]),
            Line([1.5, 1.5, -1.5], [2.775, 2.775, -1.5]),
            Line([-1.5, 1.5, -1.5], [-2.775, 2.775, -1.5]),
            Line([-1.5, -1.5, -1.5], [-2.775, -2.775, -1.5]),
            Line([1.5, -1.5, -1.5], [2.775, -2.775, -1.5])
        )
        
        for line in lines:
            line.set_stroke(YELLOW, 3)
        
        regions = Group()
        for a, face, color in zip(range(len(cube)), cube, ["#3B528B", WHITE, TEAL_E, MAROON_B, GREY_BROWN, GREEN_D]):
            if a == 1:
                face.set_fill(BLUE, 0)
            else:
                regions.add(
                    face.copy().set_fill(color, 1)
                )
        
        screen = FullScreenRectangle(stroke_width = 2, stroke_color = BLACK, fill_opacity = 1, fill_color = BLACK)
        screen.set_fill(BLUE_D, 1)
        regions.add(screen)


        self.add_foreground_mobject(cube)
        self.begin_ambient_camera_rotation(rate = 0.2)
        self.wait(5)
        self.move_camera(phi = 0, gamma = 0, theta = -90 * DEGREES, focal_distance = 5, run_time = 2)
        self.stop_ambient_camera_rotation()
        self.wait(2)
        # self.add(screen)
        # self.wait(2)

        self.add_foreground_mobjects(formula)
        self.play(
            Write(formula),
            run_time = 2,
            rate_func = smooth
        )
        self.wait(2)
        self.add_fixed_in_frame_mobjects(explanation)
        self.play(
            Write(explanation),
            run_time = 4,
            lag_ratio = 0.5
        )

        self.wait()
        self.add_foreground_mobjects(example[0])
        self.play(
            LaggedStart(
                *[
                    Draw(dot)
                    for dot in dots
                ]
            ),
            example[0].tracker.animate.set_value(8),
            rate_func = smooth
        )
        self.wait()
        self.play(
            LaggedStart(
                *[
                    FadeOut(dot)
                    for dot in dots
                ]
            ),
            run_time = 1,
            rate_func = smooth
        )
        self.add_foreground_mobjects(example[2])
        self.play(
            Write(example[1]),
            LaggedStart(
                *[
                    Draw(line)
                    for line in lines
                ]
            ),
            example[2].tracker.animate.set_value(12),
            rate_func = smooth
        )
        self.add_foreground_mobjects(example[5])
        self.bring_to_back(regions[len(regions) - 1])
        self.add_foreground_mobjects(regions[:len(regions) - 1])
        self.play(
            Write(example[4]),
            LaggedStart(
                *[
                    FadeIn(region)
                    for region in regions
                ]
            ),
            example[5].tracker.animate.set_value(6),
            rate_func = smooth
        )
        self.wait()
        self.play(
            LaggedStart(
                *[
                    Write(text)
                    for text in example[6:]
                ]
            ),
            rate_func = smooth
        )
        self.wait(4)


class Test(Scene):
    def construct(self):
        pass
