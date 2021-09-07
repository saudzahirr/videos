from manimce import *

class HalfAngleIdentity(MovingCameraScene):
    def construct(self):
        frame = self.camera.frame
        logo_transformation(self)
        theorem = Tex(r"Inscribed Angle Theorem")
        theorem.scale(1.5)
        theorem.to_edge(UP)

        circle = Circle(radius = 2, color = GREY_B)
        points = circle.get_all_points()
        point = circle.get_top()
        center = circle.get_center()
        diameter = Line(circle.get_left(), circle.get_right(), color = YELLOW)
        dot = Dot(center, radius = 0.05)
        cricle_radius = Line(circle.get_center(), circle.get_right()),
        chord = Line(start = points[15], end = points[3], color = BLUE_C)
        line = Line(start = points[3], end = points[0], color = BLUE_E)
        unit_circle = BraceLabel(diameter, "1", DOWN)

        line_1 = Line(start = points[15], end = points[3], color = BLUE_C)
        line_2 = Line(start = points[15], end = points[-4], color = BLUE_C)
        line_3 = Line(start = center, end = points[3], color = YELLOW)
        line_4 = Line(start = center, end = points[-4], color = YELLOW)

        self.play(
            Create(circle),
        )
        self.play(
            Write(theorem),
            run_time = 3,
            lag_ratio = 0.1
        )
        self.wait()
        self.play(
            FadeIn(dot),
            GrowFromPoint(line_1, points[15]),
            GrowFromPoint(line_2, points[15]),
            GrowFromPoint(line_3, center),
            GrowFromPoint(line_4,center)
        )
        self.wait()

        half_angle = Angle(line_2, line_1, radius = 0.4, color = WHITE)
        angle = Angle(line_4, line_3, radius = 0.5, color = WHITE)

        self.play(
            Create(half_angle),
            Create(angle)
        )
        self.wait()

        theta = MathTex("\\theta").next_to(half_angle, 0.5 * RIGHT)
        double_theta = MathTex("2 \\cdot \\theta").next_to(angle, 0.5 * RIGHT)

        self.play(
            Write(theta)
        )
        self.wait(0.75)
        self.play(
            Write(double_theta)
        )
        self.wait(2)

        inscribed_angle_theorem = VGroup(
            circle.copy(),
            dot.copy(),
            line_1.copy(),
            line_2.copy(),
            line_3.copy(),
            line_4.copy(),
            half_angle.copy(),
            angle.copy(),
            theta.copy(),
            double_theta.copy()
        )

        self.play(
            inscribed_angle_theorem.animate.to_edge(RIGHT)
        )
        self.play(
            inscribed_angle_theorem.animate.scale(0.75),
            FadeOut(
                theorem,
                line_1,
                line_2,
                line_3,
                line_4,
                half_angle,
                angle,
                theta,
                double_theta
            )
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

        self.play(
            frame.animate.shift(4.25 * LEFT),
            run_time = 2,
            rate_func = smooth
        )

        angle_theta = theta.copy()
        angle_theta.next_to(triangle[4], 1.5 * LEFT)
        angle_theta.shift(0.1 * UP)

        self.play(
            Write(angle_theta)
        )
        self.wait()

        cos = BraceLabel(triangle[1], "\\mathrm{cos}(\\theta)", DOWN)
        sin = BraceLabel(triangle[2], "\\mathrm{sin}(\\theta)", LEFT)
        self.play(
            Write(cos),
            Write(sin)
        )
        self.wait()

        projection = diameter.get_projection(points[3])
        projection_line = Line(points[15], projection, color = BLUE_D)
        perpendicular_line = DashedLine(points[3], projection)
        #projection_point = Point(projection, radius = 0.05)

        self.play(
            #Create(projection_point),
            GrowFromPoint(projection_line, projection),
            GrowFromPoint(perpendicular_line, points[3])
        )
        self.wait()

        length_L = BraceLabel(projection_line, "L", DOWN)

        self.play(
            Transform(unit_circle, length_L)
        )
        self.wait()
