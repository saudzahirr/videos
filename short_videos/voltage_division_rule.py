from manimce import *
from circuits import LongResistor

class Circuits(Scene):
    def construct(self):
        self.add(Title('Voltage Division Rule').scale(1.5))
        R1 = LongResistor()
        R1.add(Dot(R1.get_left()))
        R1.add(Tex("${R}_{1}$").next_to(R1, UP))
        R1.shift(1.5*UP + 1.5*RIGHT)
        R2 = LongResistor()
        R2.rotate_in_place(PI/2)
        R2.move_to(R1.get_right())
        R2.shift(1.8*DOWN)
        R2.add(EarthGround().move_to(R2.get_bottom()))
        R2.add(Tex("${R}_{2}$").next_to(R2, RIGHT))
        R2.add(BraceLabel(R2, 'V', RIGHT))
        source = Source()
        source.set_color(WHITE)
        source.add(EarthGround().move_to(source.get_bottom()))
        source.add(Tex("$E$").next_to(source, LEFT).shift(0.25*UP))
        circuit = VGroup(source, R1, R2)
        circuit.scale(0.85)
        circuit.to_edge(LEFT)
        voltage_division_formula = MathTex("V", "=", "\\left(", "{ R_{2} ", "\\over", " { R_{1}", "+", " R_{2} } }", "\\right)", "\\cdot", " E")
        voltage_division_formula.set_color_by_tex_to_color_map(
            {
                'V' : BLUE,
                'E' : DARK_PINK,
                'R_{1}' : MAROON_C,
                'R_{2}' : YELLOW,
                '\\left(' : GREY_BROWN,
                '\\right)' : GREY_BROWN
            }
        )
        voltage_division_formula.scale(1.5)
        voltage_division_formula.to_edge(2*RIGHT)

        self.play(
            circuit.animate,
            rate_func = smooth
        )
        self.wait(2)

        self.play(
            Write(voltage_division_formula),
            run_time = 4,
            lag_ratio = 0.1,
            rate_func = smooth
        )
        self.wait()
        
        
