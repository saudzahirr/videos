from manimce import *
from custom.functions import fourier_series, square_wave
from custom.drawings import Speaker
from 2021.sampling import get_sampling




def get_impulse_train(a, x_min, x_max, n):
    impulse_train = VGroup()
    for i in arange(x_min, x_max, n):
        impulse_train.add(Arrow(Point([i, -0.25, 0]), Point([i, a, 0])))
    return impulse_train

  
  
def get_frequency_domain(frequency):
    f = frequency
    axes = Axes(
        y_range = [-2, 2],
        x_range = [-5, 5],
        axis_config = {"include_tip" : False},
    )
    axes.stretch_to_fit_height(2)
    audio_signal = MathTex("F(j\\omega)")
    freq = MathTex("\\omega")
    for label in audio_signal, freq:
        label.scale(0.8)
    audio_signal.next_to(axes.y_axis, UP)
    audio_signal.shift(LEFT)
    freq.next_to(axes.x_axis.get_right(), DOWN + LEFT)
    labels = VGroup(audio_signal, freq)
    for i, j in zip([-3, 3], [-f, f]):
        axes.add(Arrow(Point(array([i, - 0.25, 0])), Point(array([i, 1.5, 0])), color = YELLOW))
        axes.add(MathTex(str(j)).scale(0.75).next_to(Point(array([i, - 0.25, 0])), 0.5 * DOWN))
    return axes, labels  
  
  
  
def get_axis(x_min, x_max):
    axis = NumberLine(
        (x_min, x_max, 1),
        tick_size = 0.025,
        longer_tick_multiple = 4,
        numbers_with_elongated_ticks = range(x_min, x_max, 5),
    )
    # axis.add_numbers(
    #     range(x_min, x_max, 1),
    #     group_with_commas = False,
    # )
    # axis = Line(LEFT, RIGHT, color = GREY_B).scale(15)
    return axis



def function(x):
    return  sin(x)



def get_square_wave(square_wave, x_min, x_max, n):
    wave = FunctionGraph(
        lambda x : square_wave(x, n),
        x_range = [x_min, x_max]
    )
    return wave
  
  
  
def get_graph(function, x_min, x_max):
    graph = FunctionGraph( 
        lambda x : function(x),
        x_range = [x_min, x_max],
        color = BLUE
    )
    return graph
  
  
  
class NyquistShannonTheorem(Scene):
  pass
