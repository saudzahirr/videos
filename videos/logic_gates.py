from manim import *

class Logic_Gate(Scene):
    def construct(self):
        #LOGO
        circle = Circle(radius=0.25,fill_color=BLUE_A,stroke_color=WHITE,stroke_width=1.3,fill_opacity=0.2)
        title = MathTex("\\alpha")
        thumbnail = VGroup(circle, title)
        thumbnail.scale(1.1)
        thumbnail.to_edge(0.5*DOWN+0.5*RIGHT)
        self.add(thumbnail)

        buffer = SVGMobject("buffer")
        buffer.set_color(WHITE)

        not_gate = SVGMobject("not")
        not_gate.set_color(WHITE)

        or_gate = SVGMobject("or")
        or_gate.set_color(WHITE)

        and_gate = SVGMobject("and")
        and_gate.set_color(WHITE)

        nor_gate = SVGMobject("nor")
        nor_gate.set_color(WHITE)

        nand_gate = SVGMobject("nand")
        nand_gate.set_color(WHITE)

        xor_gate = SVGMobject("xor")
        xor_gate.set_color(WHITE)

        xnor_gate = SVGMobject("xnor")
        xnor_gate.set_color(WHITE)

        buffer_table = MobjectTable(
            [
                [Tex(r"\large{Buffer}").scale(1.2), buffer],
                [Tex(r"A"), Tex(r"Q $=$ A")],
                [Tex(r"0"), Tex(r"0")],
                [Tex(r"1"), Tex(r"1")],
            ],
            include_outer_lines=True)
        buffer_table.scale(0.5)

        not_table = MobjectTable(
            [
                [Tex(r"\large{Not}").scale(1.2), not_gate],
                [Tex(r"A"), Tex(r"Q $=\overline{\text{A}}$")],
                [Tex(r"0"), Tex(r"1")],
                [Tex(r"1"), Tex(r"0")],
            ],
            include_outer_lines=True)
        not_table.scale(0.5)
        not_table.next_to(buffer_table, 5 * RIGHT)

        or_table = MobjectTable(
            [
                [Tex(r"\large{Or}").scale(1.2), Tex(r"Q $=$ A$+$B"), or_gate],
                [Tex(r"A"), Tex(r"B"), Tex(r"Q")],
                [Tex(r"0"), Tex(r"0"), Tex(r"0")],
                [Tex(r"0"), Tex(r"1"), Tex(r"1")],
                [Tex(r"1"), Tex(r"0"), Tex(r"1")],
                [Tex(r"1"), Tex(r"1"), Tex(r"1")]
            ],
            include_outer_lines=True)
        or_table.scale(0.5)
        or_table.next_to(not_table, 5 * RIGHT)

        and_table = MobjectTable(
            [
                [Tex(r"\large{And}").scale(1.2), Tex(r"Q $=$ A$\cdot$B"), and_gate],
                [Tex(r"A"), Tex(r"B"), Tex(r"Q")],
                [Tex(r"0"), Tex(r"0"), Tex(r"0")],
                [Tex(r"0"), Tex(r"1"), Tex(r"0")],
                [Tex(r"1"), Tex(r"0"), Tex(r"0")],
                [Tex(r"1"), Tex(r"1"), Tex(r"1")]
            ],
            include_outer_lines=True)
        and_table.scale(0.5)
        and_table.next_to(or_table, 5 * RIGHT)

        nor_table = MobjectTable(
            [
                [Tex(r"\large{Nor}").scale(1.2), Tex(r"Q $=\overline{\text{A}+\text{B}}$"), nor_gate],
                [Tex(r"A"), Tex(r"B"), Tex(r"Q")],
                [Tex(r"0"), Tex(r"0"), Tex(r"1")],
                [Tex(r"0"), Tex(r"1"), Tex(r"0")],
                [Tex(r"1"), Tex(r"0"), Tex(r"0")],
                [Tex(r"1"), Tex(r"1"), Tex(r"0")]
            ],
            include_outer_lines=True)
        nor_table.scale(0.5)
        nor_table.next_to(and_table, 5 * RIGHT)

        nand_table = MobjectTable(
            [
                [Tex(r"\large{Nand}").scale(1.2), Tex(r"Q $=\overline{\text{A}\cdot\text{B}}$"), nand_gate],
                [Tex(r"A"), Tex(r"B"), Tex(r"Q")],
                [Tex(r"0"), Tex(r"0"), Tex(r"1")],
                [Tex(r"0"), Tex(r"1"), Tex(r"1")],
                [Tex(r"1"), Tex(r"0"), Tex(r"1")],
                [Tex(r"1"), Tex(r"1"), Tex(r"0")]
            ],
            include_outer_lines=True)
        nand_table.scale(0.5)
        nand_table.next_to(nor_table, 5 * RIGHT)

        xor_table = MobjectTable(
            [
                [Tex(r"\large{Xor}").scale(1.2), Tex(r"Q $=$ A$\oplus$B"), xor_gate],
                [Tex(r"A"), Tex(r"B"), Tex(r"Q")],
                [Tex(r"0"), Tex(r"0"), Tex(r"0")],
                [Tex(r"0"), Tex(r"1"), Tex(r"1")],
                [Tex(r"1"), Tex(r"0"), Tex(r"1")],
                [Tex(r"1"), Tex(r"1"), Tex(r"0")]
            ],
            include_outer_lines=True)
        xor_table.scale(0.5)
        xor_table.next_to(nand_table, 5 * RIGHT)

        xnor_table = MobjectTable(
            [
                [Tex(r"\large{Xnor}").scale(1.2), Tex(r"Q $=\overline{\text{A}\oplus\text{B}}$"), xnor_gate],
                [Tex(r"A"), Tex(r"B"), Tex(r"Q")],
                [Tex(r"0"), Tex(r"0"), Tex(r"1")],
                [Tex(r"0"), Tex(r"1"), Tex(r"0")],
                [Tex(r"1"), Tex(r"0"), Tex(r"0")],
                [Tex(r"1"), Tex(r"1"), Tex(r"1")]
            ],
            include_outer_lines=True)
        xnor_table.scale(0.5)
        xnor_table.next_to(xor_table, 5 * RIGHT)

        gates = VGroup(buffer_table, not_table, or_table, and_table, nor_table, nand_table, xor_table, xnor_table)
        gates.next_to(ORIGIN, 5 * RIGHT)
        self.add(gates)
        self.add(Tex(r"\large{Logic Gates}").set_color(BLUE).scale(1.5).to_edge(UP))

        for gate in gates:
            if gate == gates[0]:
                self.play(
                    gates.animate.shift(3.5 * LEFT),
                    run_time=2
                )
                self.play(
                    Indicate(gate, run_time=3.5)
                )
                self.wait(2)

            elif gate == gates[1]:
                self.play(
                    gates.animate.shift(5.5 * LEFT),
                    run_time=2
                )
                self.play(
                    Indicate(gate, run_time=3.5)
                )
                self.wait(2)
            
            else:
                self.play(
                    gates.animate.shift(7 * LEFT),
                    run_time=2
                )
                self.play(
                    Indicate(gate, run_time=3.5)
                )
                self.wait(2)

        self.wait()
