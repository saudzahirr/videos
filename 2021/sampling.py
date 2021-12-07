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
