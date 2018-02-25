from bokeh.models import ColumnDataSource, Range1d, Plot
from bokeh.models.glyphs import ImageURL
from bokeh.io import curdoc, show


url = "https://bokeh.pydata.org/en/latest/_static/images/logo.png"
N = 4

source = ColumnDataSource(dict(
    url=[url] * N,
    x1=[0, 1, 2, 3],
    y1=[0, 1, 2, 3],
    scalex1=[1, 1, -1, -1],
    scaley1=[1, -1, 1, -1],
    w1=[0.5] * N,
    h1=[0.5] * N,
))

xdr = Range1d(start=-1, end=4)
ydr = Range1d(start=-1, end=4)

plot = Plot(
    title=None, x_range=xdr, y_range=ydr, plot_width=300, plot_height=300,
    h_symmetry=False, v_symmetry=False, min_border=0)

image1 = ImageURL(url="url", x="x1", y="y1", w="w1", h="h1", anchor="center", scale_x="scalex1", scale_y="scaley1")
plot.add_glyph(source, image1)

curdoc().add_root(plot)

show(plot)
