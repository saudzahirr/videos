from manimce import *


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



def square_wave(x, n):
    y = 0
    for i in range(1, n):
        y += sin((2*i - 1)*x)/(2*i - 1)
    return y


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
