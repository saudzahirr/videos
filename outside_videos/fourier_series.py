from manimce import *
from custom.functions import fourier_series



def square_wave(x, n):
    y = 0
    for i in range(1, n):
        y += sin((2*i - 1)*x)/(2*i - 1)
    return y


def discrete_function(x, y):
    f = []
    for m, n in zip(x, y):
        q = [m, n, 0]
        f.append(q)
    
    print(f)
    return f


def function(x):
    return  sin(x) + sin(2*x) + sin(3*x)


        
class Sampling(MovingCameraScene):
    def construct(self):
        #watermark(self)
        frame = self.camera.frame
        title = Tex("Sampling")
        title.scale(1.5)
        title.to_edge(UP + LEFT)
        sampling_equation = MathTex(
            "x[n] = x_{c}(nT)",
            color = YELLOW,
        )
        sampling_equation.scale(1.7)
        sampling_equation.to_edge(LEFT + 3*UP)
        sampling_equation.add_background_rectangle()
        up_sample = Tex("Up Sampling")
        up_sample.to_edge(DOWN + 3*RIGHT)
        down_sample = Tex("Down Sampling")
        down_sample.move_to(up_sample)

        x = [i for i in range(-25, 25)]
        y = [function(i) for i in range(-25, 25)]
        f = discrete_function(x, y)
        graph = FunctionGraph( 
            lambda x : function(x),
            x_range = [-25, 25],
            color = BLUE
        )

        axis = Line(LEFT, RIGHT, color = GREY_B).scale(15)

        points = VGroup()

        for coord in f:
            points.add(Dot(coord))

        stem = VGroup()
        stem.add(points)

        x_coords = []
        for i in x:
            x = [i, 0, 0]
            print(x)
            x_coords.append(x)

        for x_coord, y_coord in zip(x_coords, f):
            line = Line(x_coord, y_coord)
            stem.add(line)

        self.play(
            GrowFromCenter(axis),
            rate_func = smooth,
            run_time = 0.5
        )
        #self.wait()
        self.play(
            Create(graph),
            rate_func = slow_into,
            run_time = 6
        )
        #self.wait()
        self.play(
            Write(title, run_time = 3),
            Write(stem),
            rate_func = smooth,
            run_time = 5
        )
        self.wait(2)


        x = [i for i in arange(-25, 25, 0.2)]
        y = [function(i) for i in arange(-25, 25, 0.2)]
        f = discrete_function(x, y)

        points = VGroup()

        for coord in f:
            points.add(Dot(coord))

        stem_graph = VGroup()
        stem_graph.add(points)

        x_coords = []
        for i in x:
            x = [i, 0, 0]
            print(x)
            x_coords.append(x)

        for x_coord, y_coord in zip(x_coords, f):
            line = Line(x_coord, y_coord)
            stem_graph.add(line)


        frame.save_state()
        self.play(FadeOut(title))
        self.play(
            frame.animate.scale(1.75),
            rate_func = smooth,
            run_time = 5
        )
        self.wait(2)

        self.play(
            Restore(frame),
            rate_func = smooth,
            run_time = 5
        )
        self.play(
            FadeIn(sampling_equation, shift = RIGHT),
            rate_func = smooth,
            run_time = 1.5
        )
        self.add_foreground_mobject(sampling_equation)
        self.wait(2)

        self.play(
            Write(up_sample),
            ReplacementTransform(stem, stem_graph),
            rate_func = smooth,
            run_time = 1.5
        )
        self.wait(2)

        x = [i for i in arange(-25, 25, 0.5)]
        y = [function(i) for i in arange(-25, 25, 0.5)]
        f = discrete_function(x, y)

        points = VGroup()

        for coord in f:
            points.add(Dot(coord))

        stem_plot = VGroup()
        stem_plot.add(points)

        x_coords = []
        for i in x:
            x = [i, 0, 0]
            print(x)
            x_coords.append(x)

        for x_coord, y_coord in zip(x_coords, f):
            line = Line(x_coord, y_coord)
            stem_plot.add(line)
        
        self.play(
            TransformMatchingTex(up_sample, down_sample),
            ReplacementTransform(stem_graph, stem_plot),
            rate_func = smooth,
            run_time = 1.5
        )
        self.wait(4)

        

class SawToothWave(Scene):
    def construct(self):
        waves = FunctionGraph( 
            lambda x : fourier_series(x, 100, 0, [0 for k in range(0, 100)], [(2/pi * (-1)**(i+2)/(i+1)) for i in range(0, 100)]),
            x_range = [-100, 100]
        )
        waves.scale(0.25)

        self.play(
            Create(waves)
        )
        self.wait()
        
        
        
class FourierSeries(Scene):
    def construct(self):
        waves = VGroup()
        for m in range(10):
            waves.add(
                FunctionGraph( 
                    lambda x : square_wave(x, m),
                    x_range = [-10, 10]
                )
            )
        # waves[3:].arrange(DOWN, buff = SMALL_BUFF)
        # waves[3:].to_edge(UP)

        # for color, wave in zip(waves, cycle([BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E])):
        #     wave.set_color(color)

        for i, wave in zip(range(2, len(waves)-1), waves):
            if i < len(waves):
                self.play(
                    Create(waves[i])
                )
                self.wait()
                self.play(
                    ReplacementTransform(waves[i], waves[i+1])
                )
            else:
                break
            self.wait()
        self.wait()

        
        
        
