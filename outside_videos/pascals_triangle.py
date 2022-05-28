from manimce import *
from custom.drawings import PascalsTriangle



class FibonacciNumbersInPascalsTriangle(Scene):
    def construct(self):
        line = Line([0, -FRAME_HEIGHT, 0], [0, FRAME_HEIGHT, 0], stroke_width = 4)

        title = Tex("Pascal's Triangle", "Fibonacci Numbers")
        title.scale(1.5)
        title[0].to_edge(UL)
        title[1].to_edge(UR)

        pascal_triangle = PascalsTriangle(n = 8)
        pascal_triangle.scale(0.85)
        pascal_triangle.next_to(line, LEFT)
        pascal_triangle.next_to(title[0], DOWN)
        pascal_triangle.shift(0.2 * RIGHT)

        for number, color in zip(pascal_triangle.get_part_by_tex(r"\\"), cycle([BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E])):
            number.set_color(color)
        
        kw = {"tex_to_color_map": {
            "{0}": GREY_B,
            "{1}": LIGHT_GREY,
            "{2}": GREY_BROWN,
            "{3}": GREY_B,
            "{4}": GREY_A,
            "{5}": GREY_C,
            "{6}": GREY_A,
            "{7}": GREY_BROWN,
            "{8}": GREY_C,
            "{9}": LIGHT_GREY,
            }
        }

        fibonacci_numbers = MathTex(
            "{0}, \\ {1}, \\ {1}, \\ {2}, \\ {3}, \\ {5}, \\ {8}, \\\\ {1}{3}, \\ {2}{1}, \\ {3}{4}, \\ {5}{5}, \\ {8}{9}, \\\\ {1}{4}{4}, \\ {2}{3}{3}, \\ {3}{7}{7}, \\ {6}{1}{0}, \\\\  {9}{8}{7}, \\ {1}{5}{9}{7}, \\ {2}{5}{8}{4}, \\\\  {4}{1}{8}{1}, \\ {6}{7}{6}{5}, \\ {1}{0}{9}{4}{6}, \\\\ {1}{7}{7}{1}{1}, \\ {2}{8}{6}{5}{7}, \\ {4}{6}{3}{6}{8}, \\\\ {7}{5}{0}{2}{5}, \\ {1}{2}{1}{3}{9}{3} \\cdots",
            **kw
        )

        fibonacci_numbers.scale(1.5 * 0.85)
        fibonacci_numbers.next_to(line, RIGHT)
        fibonacci_numbers.next_to(title[1], DOWN)
        fibonacci_numbers.shift(0.2 * RIGHT)


        self.add_foreground_mobjects(line, title, pascal_triangle, fibonacci_numbers)
