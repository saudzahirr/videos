from manimce import *
from custom.functions import fourier_series, square_wave
from custom.drawings import Speaker



def get_sampling(function, x_min, x_max, sample_step):
    """Samples a continuous function into discrete
    function and returns discrete plot."""
    x = [i for i in arange(x_min, x_max, sample_step)]
    y = [function(i) for i in arange(x_min, x_max, sample_step)]

    f = []
    for m, n in zip(x, y):
        q = [m, n, 0]
        f.append(q)

    points = VGroup()
    for coordinates in f:
        points.add(Dot(coordinates))

    stem_plot = VGroup()
    stem_plot.add(points)

    x_coords = []
    for i in x:
        x = [i, 0, 0]
        x_coords.append(x)

    for x_coord, y_coord in zip(x_coords, f):
        line = Line(x_coord, y_coord)
        stem_plot.add(line)

    return stem_plot



def get_graph(function, x_min, x_max):
    graph = FunctionGraph( 
        lambda x : function(x),
        x_range = [x_min, x_max],
        color = BLUE
    )
    return graph



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



def get_impulse_train(a, x_min, x_max, n):
    impulse_train = VGroup()
    for i in arange(x_min, x_max, n):
        impulse_train.add(Arrow(Point([i, -0.25, 0]), Point([i, a, 0])))
    return impulse_train
  
  
  
class Introduction(Scene):
  pass
 

class NyquistShannonTheorem(Scene):
  pass
