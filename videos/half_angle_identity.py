from manimce import *

class HalfAngleIdentity(MovingCameraScene):
    colors = [
        PINK, RED, YELLOW, GREEN, GREEN_A, BLUE,
        MAROON_E, MAROON_B, YELLOW, BLUE,
    ]
    text = "Geometry WonderLand"

    def construct(self):
        frame = self.camera.frame
        logo_transformation(self)
        word = self.get_geometry_wonder_land_word()
        word_outlines = word.copy()
        word_outlines.set_fill(opacity=0)
        word_outlines.set_stroke(WHITE, 1)
        colors = list(self.colors)
        random.shuffle(colors)
        word_outlines.set_color_by_gradient(*colors)
        word_outlines.set_stroke(width=5)

        circles = VGroup()
        for letter in word:
            circle = Circle()
            # circle = letter.copy()
            circle.replace(letter, dim_to_match=1)
            circle.scale(3)
            circle.set_stroke(WHITE, 0)
            circle.set_fill(letter.get_color(), 0)
            circles.add(circle)
            circle.target = letter

        self.play(
            LaggedStartMap(MoveToTarget, circles),
            run_time=2
        )
        self.add(word_outlines, circles)
        self.play(LaggedStartMap(
            FadeIn, word_outlines,
            run_time=3,
            rate_func=there_and_back,
        ), Animation(circles))
        self.wait()
        self.clear()

        theorem = Tex(r"Inscribed Angle Theorem")
        theorem.scale(1.5)
        theorem.to_edge(UP)

        circle = Circle(radius = 2, color = GREY_B)
        points = circle.get_all_points()
        point = circle.get_top()
        center = circle.get_center()
        diameter = Line(circle.get_left(), circle.get_right(), color = YELLOW)
        dot = Dot(center, radius = 0.05)
        circle_radius = Line(circle.get_center(), circle.get_right(), color = CHARCOAL)
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
        projection_line = Line(points[15], projection, color = DARK_PINK)
        perpendicular_line = DashedLine(points[3], projection)
        projection_point = Dot(projection, radius = 0.05)

        self.play(
            Create(projection_point),
            GrowFromPoint(projection_line, projection),
            GrowFromPoint(perpendicular_line, points[3])
        )
        self.wait()

        length_L = BraceLabel(projection_line, "\\mathrm{cos}^{2}(\\theta)", DOWN)
        hypotenuse = BraceBetweenPoints(points[3], points[15])
        hyp = MathTex("\\mathrm{cos}(\\theta)")
        #hyp.add_background_rectangle()
        hyp.next_to(hypotenuse, 0.25 * UP)
        hyp.shift(0.38 * DOWN)
        circle.add(dot, theta, projection_line, perpendicular_line, projection_point, length_L, hypotenuse, hyp)
        theorem = circle.copy()
        circle.remove(diameter, chord, line, right_angle, half_angle, half_angle, dot, theta, projection_line, perpendicular_line, projection_point, length_L, hypotenuse, hyp)

        self.play(
            Write(hypotenuse, run_time = 2, rate_func = smooth),
            Write(hyp)
        )
        self.wait()

        self.play(
            ReplacementTransform(unit_circle, length_L)
        )
        self.wait()


        self.play(
            frame.animate.shift(9 * RIGHT),
            run_time = 2,
            rate_func = smooth
        )
        self.play(
            inscribed_angle_theorem.animate.shift(5 * RIGHT)
        )
        self.play(
            #theorem.animate,
            theorem.animate.shift(5 * RIGHT)
        )
        
        self.play(
            FadeOut(
                perpendicular_line,
                projection_line, hyp,
                hypotenuse, length_L
            )
        )
        self.remove(length_L)
        self.wait(0.5)

        perpendicular = Line(projection, points[3])
        angled_line = Line(circle.get_center(), points[3], color = MELON)
        radius = Line(circle.get_center(), circle.get_left(), color = CHARCOAL)
        circle_radius = Line(circle.get_center(), circle.get_right(), color = YELLOW)
        unit_circle = BraceLabel(diameter, "1", DOWN)

        self.play(
            Write(unit_circle),
            #ReplacementTransform(length_L, unit_circle),
            GrowFromPoint(perpendicular, points[3]),
            Create(angled_line)
        )
        #self.add(circle_radius)
        self.wait()


        double_angle = Angle(circle_radius, angled_line, radius = 0.5, color = WHITE)
        double_theta = MathTex("2\\theta").next_to(double_angle, 0.5 * RIGHT)
        double_theta.shift(0.1 * UP)

        radius_length = BraceLabel(radius, "\\small{1 \\over 2}", DOWN, label_scale = 0.85)
        angled_line_length = BraceBetweenPoints(points[3], center)
        half = MathTex("\\small{1 \\over 2}")
        half.scale(0.85)
        #half.add_background_rectangle()
        half.move_to(angled_line_length)
        half.shift(0.5 * UP)
        half.shift(0.5 * LEFT)
        angled_line_length.add(half)

        self.play(
            Create(double_angle),
            Write(double_theta)
        )
        self.wait()
        
        self.play(
            ReplacementTransform(unit_circle, radius_length),
            GrowFromPoint(radius, circle.get_center()),
            Write(angled_line_length)
        )
        self.wait()

        base = Line(center, projection, color = BLUE_B)
        label_base = BraceLabel(base, "{1 \\over 2}{\\mathrm{cos}(2\\theta)}", DOWN, label_scale = 0.85)

        self.play(
            GrowFromPoint(base, center),
            Write(label_base)
        )
        self.wait()

        self.play(
            frame.animate.shift(1.8 * DOWN)
        )
        self.wait()

        equation = MathTex(
            "\\mathrm{cos}^{2}(\\theta)", "=", "{1 \\over 2}", "+", "{1 \\over 2}{\\mathrm{cos}(2\\theta)}"
        )
        equation.scale(1.5)
        equation.next_to(theorem, 3 * DOWN)
        equation.shift(LEFT)

        self.play(
            Write(equation)
        )
        self.wait()
    

    def get_geometry_wonder_land_word(self):
        word = Tex(self.text)
        word.rotate(-90 * DEGREES)
        word.scale(0.25)
        word.shift(3 * RIGHT)
        word.apply_complex_function(np.exp)
        word.rotate(90 * DEGREES)
        word.set_width(9)
        word.center()
        word.to_edge(UP)
        word.set_color_by_gradient(*self.colors)
        word.set_background_stroke(width=0)
        return word
