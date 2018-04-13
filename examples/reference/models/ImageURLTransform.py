from bokeh.models import ColumnDataSource
from bokeh.io import curdoc, show
from bokeh.plotting import figure
import pandas as pd
import numpy as np


url = "https://bokeh.pydata.org/en/latest/_static/images/logo.png"

# vary horizonal / veritcal flip / angle
hflips = pd.DataFrame(dict(key=[1] * 2, url=[url] * 2, scalex=[1, -1], x1=[0, 1]))
vflips = pd.DataFrame(dict(key=[1] * 2, scaley=[1, -1], x2=[0, 2]))
angles = pd.DataFrame(dict(key=[1] * 6, angle=np.arange(6) * 2 * np.pi / 6, y=np.arange(6)))

data = pd.merge(pd.merge(vflips, hflips, on='key'), angles, on='key')
data['yname'] = pd.Series(['a=%d' % np.round(x * 180 / np.pi) for x in data.angle], dtype='category')
scale_tuple = data.apply(lambda z: '(%d, %d)' % (z.scalex, z.scaley), axis=1)
data['xname'] = pd.Series(scale_tuple, dtype='category')

source = ColumnDataSource(data)

xdr = list(data.xname.unique().astype(str))
ydr = list(data.yname.unique().astype(str))

plot = figure(
    title=None, x_range=xdr, y_range=ydr, plot_width=300, plot_height=300,
    h_symmetry=False, v_symmetry=False, min_border=0)

plot.image_url(source=source, url="url", x="xname", y="yname",
               w=0.9, h=0.9, anchor="center",
               scale_x="scalex", scale_y="scaley", angle="angle")

curdoc().add_root(plot)

show(plot)
