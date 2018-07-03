"""
==================
Image geo-location
==================

Based on the matplotlib/examples/widgets/rectangle_selector.py.

"""
import cartopy.crs as ccrs
from matplotlib.widgets import RectangleSelector
import matplotlib.pyplot as plt
import matplotlib.transforms as mtrans
import numpy as np


rob = ccrs.Robinson(central_longitude=11.25)
ax = plt.axes(projection=rob)
ax.set_global()
ax.coastlines()


extent = list(rob.x_limits) + list(rob.y_limits)
# A slightly better approximation...
# extent = [-13699119.4302052, 17123551.559067532,
#           -6356356.797292399, 8605867.777293697]

img_array = plt.imread(
    '../resources/640px-Around_the_World_in_Eighty_Days_map.png')
img = ax.imshow(img_array, extent=extent, transform=rob, origin='upper')

# Create a separate axes for the Rectangle selector (as it needs
# to extend beyond the axes clip area).
ax_selector = plt.axes([0, 0, 1, 1])
ax_selector.patch.set_visible(False)


def transform_extent(extent, transform):
    # A quick and dirty matplotlib transformation of an extent,
    # rather than a bbox.
    x0, y0 = transform.transform_point([extent[0], extent[2]])
    x1, y1 = transform.transform_point([extent[1], extent[3]])
    return x0, x1, y0, y1


def line_select_callback(eclick, erelease):
    # Update the image extent when the rectangle selector is moved.
    selector_to_rob = ax_selector.transData + ax.transData.inverted()
    ext = transform_extent(selector.extents, selector_to_rob)
    print('New extents: [{}, {}, {}, {}]'.format(*ext))
    img.set_extent(ext)


selector = RectangleSelector(
    ax_selector, line_select_callback,
    drawtype='box', minspanx=5, minspany=5,
    spancoords='pixels', interactive=True)


def align_box_to_img(event):
    # Because cartopy preserves aspect ratio, we need to trigger this
    # event each time the window is resized.
    rob_to_selector = ax.transData + ax_selector.transData.inverted()
    selector.extents = transform_extent(extent, rob_to_selector)
    plt.draw()
cid = ax.figure.canvas.mpl_connect('resize_event', align_box_to_img)
align_box_to_img(None)

plt.show()
