from manimce import *



class OrbitalMotion(Scene):
    def construct(self):
      
        logo(self)
        self.origin_point = np.array([0,0,0])
        self.show_orbit()
        self.move_mass()
    
    def show_orbit(self):
        ellipse = Ellipse(width=5.5,height=4.5, color=WHITE)
        ellipse.move_to(self.origin_point)
        focus = Dot(np.array([sqrt(5), 0, 0]),radius=0.02)
        R = Tex(r"$\textbf{R}$").next_to(focus, 0.25*DOWN)
        focus.add(R.scale(0.7))
        centre = Dot(np.array([0,0,0]),radius=0.02)
        C = Tex(r"$\textbf{C}$").next_to(centre, 0.25*DOWN)
        centre.add(C.scale(0.7))
        ellipse.add(focus)
        ellipse.add(centre)
        self.add(ellipse)
        self.ellipse = ellipse

    def move_mass(self):
        orbit = self.ellipse
        origin_point = self.origin_point

        dot = Dot(radius=0.0008, color=YELLOW)
        P = Tex(r"$\textbf{P}$").next_to(dot, UP)
        dot.add(P.scale(0.7))
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.09

        def go_around_orbit(mob, dt):
            self.t_offset += (dt * rate)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_orbit():
            return Line(np.array([sqrt(5), 0, 0]), dot.get_center(), color=YELLOW)
        
        def get_line_from_origin_to_orbit():
            return DashedLine(origin_point, dot.get_center())
        
        dot.add_updater(go_around_orbit)
        
        focus_to_orbit =  always_redraw(get_line_to_orbit)
        origin_to_orbit_line = always_redraw(get_line_from_origin_to_orbit)

        self.add(dot)
        self.add(orbit, focus_to_orbit, origin_to_orbit_line)
        

        force_equation = MathTex(
            "F = {GMm \\over (0.000)^2}",
            tex_to_color_map={
                "F": BLUE,
                "0.000": BLACK,
            }
        ).next_to(orbit, DOWN)
        radius_in_denominator_ref = force_equation.get_part_by_tex("0.000")
        radius_in_denominator = DecimalNumber(number = 0, num_decimal_places = 3, color = YELLOW)
        update_radius_in_denominator = ChangingDecimal(radius_in_denominator, lambda a: focus_to_orbit.get_length(), rate_func = slow_into 
        )
        radius_in_denominator.move_to(radius_in_denominator_ref)
        self.add(force_equation)
        self.play(update_radius_in_denominator, run_time = 10, rate_func = slow_into)
        self.wait()
        dot.remove_updater(go_around_orbit)
        self.clear()
        
        
        
        
        
        
        
        
        
        
