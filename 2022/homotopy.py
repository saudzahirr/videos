from manimce import *



def homotopy(x, y, z, t):
  norm = linalg.norm([x, y])
  tau = interpolate(-5, 5, t) + norm/FRAME_WIDTH
  alpha = sigmoid(tau)
  return [x, y + 0.5 * sin(2 * pi * alpha), z]
        
  
class HomotopyAnimation(Scene):
    def construct(self):
        x = 2 * FRAME_WIDTH
        y = 2 * FRAME_HEIGHT
        plane = plane = NumberPlane(
        x_range = [-x, x],
        y_range = [-y, y],
        x_length = 2*x,
        y_length = 2*y,
        background_line_style = {
            "stroke_width": 2,
        },
        faded_line_ratio = 2
        )
        a = 1.5
        circle = Circle(radius = a, color = BLUE, fill_color = BLUE, fill_opacity = 0.5)
        for vector in compass_directions(16):
            circle.add(Arrow(0*vector, a*vector, color = YELLOW, buff = 0))
        self.add_foreground_mobjects(circle)
        
        self.play(
            Homotopy(homotopy, plane, run_time = 3)
        )
        self.wait()
        self.play(
            ApplyMatrix([[2, 0], [2, 1]], circle),
            run_time = 2
        )
        self.wait()
