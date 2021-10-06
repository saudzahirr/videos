from manimce import *


class A440(Scene):
    def construct(self):
        watermark(self)

        speaker = Speaker()
        speaker.add(Tex('A440').set_color(YELLOW).next_to(speaker, UP))
        speaker.to_edge(UP + 4 * LEFT)
        title = Tex("Audio Frequency ", "440 Hz", tex_to_color_map={'440 Hz': BLUE})
        title.scale(1.5)
        title.next_to(speaker, 2*RIGHT)
        title.to_edge(UP + 2 * RIGHT)
        axes = Axes(
            y_range = [-2, 2],
            x_range = [0, 10],
            axis_config = {"include_tip" : False},
        )
        axes.stretch_to_fit_height(2)
        axes.shift(2*DOWN)

        self.add_sound('A440.wav', time_offset = 1)
        self.add(speaker)
        frequency = 2.1
        graph = self.get_wave_graph(frequency, axes)
        graph.shift(0.5*UP)
        graph.set_color(BLUE)
        self.play(Create(axes))
        waves = Circle(radius = 3, arc_center = speaker[4].get_center(), color = BLUE_B)

        self.play(
            Write(title, lag_ratio = 0.1 , run_time = 3.25, rate_func = smooth),
            Create(graph, run_time = 5, rate_func = smooth),
            Broadcast(waves, focal_point = speaker[4].get_center(), n_mobs = 10, run_time = 5, rate_func = smooth)
        )



    def get_wave_graph(self, frequency, axes):
        tail_len = 3.0
        x_min, x_max = 0, 10
        def func(x):
            value = 0.7*np.cos(2*np.pi*frequency*x)
            if x - x_min < tail_len:
                value *= smooth((x-x_min)/tail_len)
            if x_max - x < tail_len:
                value *= smooth((x_max - x )/tail_len)
            return value
        graph = axes.get_graph(func)
        return graph
        
        
        
