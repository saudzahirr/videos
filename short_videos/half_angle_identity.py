from manimce import *

class HalfAngleIdentity(MovingCameraScene):
    colors = [
        BLUE_B, BLUE_C, BLUE_D, BLUE_D
    ]
    text = "geometry_wonderland.svg"

    def construct(self):
        #self.add_sound("heartbeat.wav", time_offset = 6, gain = 1.5)
        logo_transformation(self)
        frame = self.camera.frame
        geometry = Circle(radius = 2, color = GREY_BROWN)
        points = geometry.get_all_points()
        point = geometry.get_top()
        diameter = Line(geometry.get_left(), geometry.get_right())
        diameter.set_color(WHITE)

        chords = VGroup()
        for i in range(5):
            chord = Line(start = point, end = points[- 4 * i])
            chords.add(chord)
        
        for i in range(5):
            chord = Line(start = geometry.get_bottom(), end = points[4 * i])
            chords.add(chord)
        
        chords.add(
            Line(start = points[3], end = points[15]),
            Line(start = points[12], end = points[0]),
            Line(start = points[15], end = points[-4]),
            Line(start = points[0], end = points[-12]),
            Line(start = points[0], end = points[3]),
            Line(start = points[0], end = points[-4]),
            Line(start = points[15], end = points[-12]),
            Line(start = points[15], end = points[12]),
            Line(start = points[3], end = points[12]),
            Line(start = points[-4], end = points[-12])
        )
        
        for chord, color in zip(chords, cycle([YELLOW_A, YELLOW_B, YELLOW_C, YELLOW, YELLOW_D, YELLOW_E])):
            chord.set_color(color)

        geometry.add(diameter, chords)
        word = self.get_geometry_wonderland_word()
        word.scale(1.3)
        word.to_edge(1 * UP)
        geometry.next_to(word, 4 * DOWN)
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
            #GrowFromPoint(geometry, geometry.get_center()),
            DrawBorderThenFill(geometry),
            run_time = 3
        )
        self.add(word_outlines, circles)
        self.play(LaggedStartMap(
            FadeIn, word_outlines,
            run_time = 3,
            rate_func = there_and_back,
        ), Animation(circles))
        self.wait(2)
        # self.play(
        #     FadeOut(word, word_outlines, shift = UP),
        #     FadeOut(geometry, circle),
        #     rate_func = smooth,
        # )
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
        self.wait()

        self.play(
            FadeIn(dot),
            GrowFromPoint(line_1, points[15]),
            GrowFromPoint(line_2, points[15]),
            GrowFromPoint(line_3, center),
            GrowFromPoint(line_4,center)
        )
        self.play(
            Write(theorem),
            run_time = 3,
            lag_ratio = 0.1
        )
        self.wait()

        half_angle = Angle(line_2, line_1, radius = 0.4, color = WHITE)
        angle = Angle(line_4, line_3, radius = 0.5, color = WHITE)

        self.play(
            Create(half_angle),
            Create(angle)
        )
        self.wait(2)

        theta = MathTex("\\theta").next_to(half_angle, 0.5 * RIGHT)
        double_theta = MathTex("2 \\cdot \\theta").next_to(angle, 0.5 * RIGHT)

        self.play(
            Write(theta),
            run_time = 1.25,
            rate_func = smooth
        )
        self.wait(1.25)
        self.play(
            Write(double_theta),
            run_time = 1.5,
            rate_func = smooth
            #GrowFromPoint(double_theta, geometry.get_left())
        )
        self.wait(3)

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
            # inscribed_angle_theorem.animate.to_edge(RIGHT),
            inscribed_angle_theorem.animate.next_to(circle, RIGHT),
            run_time = 2,
            rate_func = smooth
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
            ),
            run_time = 2,
            rate_func = smooth
        )
        self.wait(1.5)

        self.play(GrowFromPoint(diameter, point = circle.get_right()))
        self.play(GrowFromPoint(chord, point = points[15]))
        self.play(GrowFromPoint(line, point = points[3]))
        self.wait(2)

        self.play(
            Write(unit_circle),
            run_time = 1.25,
            rate_func = smooth
        )
        self.wait(2)

        right_angle = RightAngle(line, Line(start = points[3], end = points[15]), length = 0.2)
        self.play(
            Create(right_angle)
        )
        self.wait(2)

        half_angle = half_angle = Angle(diameter, chord, radius = 0.65)
        theta = MathTex("\\theta").next_to(half_angle, 1.5 * RIGHT)
        theta.shift(0.1 * UP)

        self.play(
            Create(half_angle)
        )
        self.wait(1)
        self.play(
            Write(theta)
        )
        self.wait(3)

        triangle = VGroup(
            diameter.copy(), chord.copy(),
            line.copy(), right_angle.copy(),
            half_angle.copy()
        )
        circle.add(
            diameter, chord, line,
            right_angle, half_angle,
            half_angle
        )

        self.play(
            triangle.animate.to_edge(LEFT),
            run_time = 2,
            rate_func = smooth
        )
        self.play(
            triangle.animate.rotate(- 203 * DEGREES),
            run_time = 2,
            rate_func = smooth
        )
        self.play(
            triangle.animate.shift(0.55 * DOWN)
        )
        self.wait(1.5)

        # self.play(
        #     # frame.animate.shift(4.25 * LEFT),
        #     frame.animate.shift(1.20 * LEFT),
        #     run_time = 2,
        #     rate_func = smooth
        # )

        angle_theta = theta.copy()
        angle_theta.next_to(triangle[4], 1.5 * LEFT)
        angle_theta.shift(0.1 * UP)

        self.play(
            Write(angle_theta),
            run_time = 1.25,
            rate_func = smooth
        )
        self.wait(1.5)

        cos = BraceLabel(triangle[1], "\\mathrm{cos}(\\theta)", DOWN)
        sin = BraceLabel(triangle[2], "\\mathrm{sin}(\\theta)", LEFT)
        self.play(
            Write(cos),
            Write(sin),
            frame.animate.shift(1.20 * LEFT),
            run_time = 2.5,
            rate_func = smooth
        )
        self.wait(2)

        projection = diameter.get_projection(points[3])
        projection_line = Line(points[15], projection, color = DARK_PINK)
        perpendicular_line = DashedLine(points[3], projection)
        projection_point = Dot(projection, radius = 0.05)

        self.play(
            Create(projection_point),
            GrowFromPoint(projection_line, projection),
            GrowFromPoint(perpendicular_line, points[3])
        )
        self.wait(3)

        length_L = BraceLabel(projection_line, "\\mathrm{cos}^{2}(\\theta)", DOWN)
        hypotenuse = BraceBetweenPoints(points[3], points[15])
        hyp = MathTex("\\mathrm{cos}(\\theta)")
        #hyp.add_background_rectangle()
        hyp.next_to(hypotenuse, 0.25 * UP)
        hyp.shift(0.38 * DOWN)
        circle.add(
            dot, theta, projection_line,perpendicular_line,
            projection_point, length_L, hypotenuse, hyp
        )
        theorem = circle.copy()
        circle.remove(
            diameter, chord, line,
            right_angle, half_angle,
            half_angle, dot, theta,
            projection_line, perpendicular_line,
            projection_point, length_L, hypotenuse, hyp
        )

        self.play(
            Write(hypotenuse, run_time = 2, rate_func = smooth),
            Write(hyp)
        )
        self.wait(2)

        self.play(
            ReplacementTransform(unit_circle, length_L)
        )
        self.wait(3.5)


        self.play(
            frame.animate.shift(5.85 * RIGHT),
            # frame.animate.shift(9 * RIGHT),
            run_time = 2,
            rate_func = smooth
        )
        self.play(
            inscribed_angle_theorem.animate.shift(5 * RIGHT),
            run_time = 2,
            rate_func = smooth
        )
        self.play(
            #theorem.animate,
            theorem.animate.shift(5 * RIGHT),
            run_time = 2,
            rate_func = smooth
        )
        
        self.play(
            FadeOut(
                perpendicular_line,
                projection_line, hyp,
                hypotenuse, length_L
            )
        )
        self.remove(length_L)
        self.wait(2)

        perpendicular = Line(projection, points[3])
        angled_line = Line(circle.get_center(), points[3], color = MELON)
        radius = Line(circle.get_center(), circle.get_left(), color = CHARCOAL)
        circle_radius = Line(circle.get_center(), circle.get_right(), color = YELLOW)
        unit_circle = BraceLabel(diameter, "1", DOWN)

        self.play(
            Write(unit_circle),
        )
        self.wait(2)
        self.play(
            #ReplacementTransform(length_L, unit_circle),
            GrowFromPoint(perpendicular, points[3]),
            Create(angled_line)
        )
        #self.add(circle_radius)
        self.wait(2.25)


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
            Write(double_theta),
            Indicate(inscribed_angle_theorem, color = BLUE_A, run_time = 2.75)
        )
        self.wait(2)
        
        self.play(
            ReplacementTransform(unit_circle, radius_length),
            GrowFromPoint(radius, circle.get_center()),
            Write(angled_line_length)
        )
        self.wait(3.25)

        base = Line(center, projection, color = BLUE_B)
        label_base = BraceLabel(base, "{1 \\over 2}{\\mathrm{cos}(2\\theta)}", DOWN, label_scale = 0.85)

        self.play(
            GrowFromPoint(base, center),
            Write(label_base, run_time = 3, lag_ratio = 0.1)
        )
        self.wait(3)

        self.play(
            frame.animate.shift(1.8 * DOWN),
            run_time = 2,
            rate_func = smooth
        )
        self.wait(1.5)

        equation = MathTex(
            "\\mathrm{cos}^{2}(\\theta)", "=", "{1 \\over 2}", "+", "{1 \\over 2}{\\mathrm{cos}(2\\theta)}"
        )
        equation.scale(1.5)
        equation.next_to(theorem, 3 * DOWN)
        equation.shift(LEFT)

        self.play(
            Write(equation),
            run_time = 3,
            rate_func = smooth,
            lag_ratio = 0.1
        )
        self.wait(2)

        # self.play(
        #     ApplyWave(equation, amplitude = 0.35, run_time = 2)
        #     #Wiggle(equation)
        # )
        rect = SurroundingRectangle(equation, color = BLUE_C)
        rect.scale(1.1)
        self.play(
            Create(rect),
            run_time = 2,
            rate_func = smooth
        )
        self.wait(0.1)
        self.play(
            FadeOut(rect)
        )
        self.wait(3)
        self.clear()
    

    def get_geometry_wonderland_word(self):
        word = SVGMobject(self.text)
        word.scale(2)
        word.shift(3 * RIGHT)
        word.set_width(9)
        word.center()
        word.to_edge(UP)
        word.set_color_by_gradient(*self.colors)
        word.set_background_stroke(width=0)
        return word
