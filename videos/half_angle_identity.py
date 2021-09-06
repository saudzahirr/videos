from manim import *

class HalfAngleIdentity(Scene):
    def construct(self):
        circle = Circle(radius = 2, color = GREY_B)
        points = circle.get_all_points()
        point = circle.get_top()
        center = circle.get_center()
        diameter = Line(circle.get_left(), circle.get_right(), color = YELLOW)
        cricle_radius = Line(circle.get_center(), circle.get_right()),
        chord = Line(start = points[15], end = points[3], color = BLUE_C)
        line = Line(start = points[3], end = points[0], color = BLUE_E)
        unit_circle = BraceLabel(diameter, "1", DOWN)

        self.play(
            Create(circle),
        )
        self.wait()

        self.play(GrowFromPoint(diameter, point = circle.get_right()))
        self.play(GrowFromPoint(chord, point = points[15]))
        self.play(GrowFromPoint(line, point = points[3]))
        self.wait()

        self.play(
            Write(unit_circle)
        )
        self.wait()

        right_angle = RightAngle(line, Line(start = points[3], end = points[15]), length = 0.2)
        self.play(
            Create(right_angle)
        )
        self.wait()

        half_angle = half_angle = Angle(diameter, chord, radius = 0.65)
        theta = MathTex("\\theta").next_to(half_angle, 1.5 * RIGHT)
        theta.shift(0.1 * UP)

        self.play(
            Create(half_angle)
        )
        self.wait(0.75)
        self.play(
            Write(theta)
        )
        self.wait()

        triangle = VGroup(diameter.copy(), chord.copy(), line.copy(), right_angle.copy(), half_angle.copy())
        circle.add(diameter, chord, line, right_angle, half_angle, half_angle)

        self.play(
            triangle.animate.to_edge(LEFT)
        )
        self.play(
            triangle.animate.rotate(- 203 * DEGREES),
            run_time = 2,
            rate_func = smooth
        )
        self.play(
            triangle.animate.shift(0.5 * DOWN)
        )
        self.wait()

        angle_theta = theta.copy()
        angle_theta.next_to(triangle[4], 1.5 * LEFT)
        angle_theta.shift(0.1 * UP)

        self.play(
            Write(angle_theta)
        )
        self.wait()

        cos = BraceLabel(triangle[1], "\\mathrm{cos}(\\theta)", DOWN)
        self.play(
            Write(cos)
        )
        self.wait()
