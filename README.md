# aljabrak

"If you can't explain it simply, you don't understand it well enough."
<br/>
<br/>
[<img align="left" alt="codeSTACKr.com" width="22px" src="https://raw.githubusercontent.com/iconic/open-iconic/master/svg/globe.svg" />]()
[<img align="left" alt="codeSTACKr | YouTube" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/youtube.svg" />](https://www.youtube.com/channel/UCN0ssVJD0ANFjmggc1vkcww/featured)
[<img align="left" alt="codeSTACKr | Twitter" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/twitter.svg" />](https://twitter.com/aljabrak)
[<img align="left" alt="codeSTACKr | Instagram" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />](https://www.instagram.com/aljabrak/)
[<img align="left" alt="codeSTACKr | Reddit" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/reddit.svg" />](https://www.reddit.com/user/aljabrak)
[<img align="left" alt="codeSTACKr | Facebook" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/facebook.svg" />](https://web.facebook.com/aljabrak)
<br/>

This project contains code for animated mathematics, physics, engineering and computer science for better understanding.
All the work here is generated using community maintained version at [Manim Community](https://github.com/ManimCommunity).
Some of the animantions are based on [manim](https://github.com/3b1b/manim), an open source scrappy python library for mathematical animation
created by Grant Sanderson. Also see his work [3blue1brown](https://www.3blue1brown.com/).

```py
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
```

# Manim Installation
```sh
pip install manim
# Manim Community Version.
```
```sh
pip install manimgl
# Manim used by 3Blue1Brown.
```
Manim runs on Python 3.6 or higher (Python 3.8 is recommended).

System requirements are [FFmpeg](https://ffmpeg.org/), [OpenGL](https://www.opengl.org/) and [LaTeX](https://www.latex-project.org) ([MiKTeX](https://miktex.org/howto/install-miktex)).


# Copyright ©
The source code in this repository is only for reference, and not for usage without permission.
