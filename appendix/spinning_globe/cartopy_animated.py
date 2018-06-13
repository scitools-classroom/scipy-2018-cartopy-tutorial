import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import cartopy.crs as ccrs


fig = plt.figure()


# From http://scitools.org.uk/cartopy/docs/latest/examples/logo.html
def add_logo(ax):
    import matplotlib.textpath
    import matplotlib.patches
    from matplotlib.font_manager import FontProperties

    ax.gridlines()

    # generate a matplotlib path representing the word "cartopy"
    fp = FontProperties(family='Bitstream Vera Sans', weight='bold')
    logo_path = matplotlib.textpath.TextPath((-175, -35), 'cartopy',
                                             size=1, prop=fp)
    # scale the letters up to sensible longitude and latitude sizes
    logo_path._vertices *= np.array([80, 160])

    # add a background image
    im = ax.stock_img()
    # clip the image according to the logo_path. mpl v1.2.0 does not support
    # the transform API that cartopy makes use of, so we have to convert the
    # projection into a transform manually
    plate_carree_transform = ccrs.PlateCarree()._as_mpl_transform(ax)
    im.set_clip_path(logo_path, transform=plate_carree_transform)

    # add the path as a patch, drawing black outlines around the text
    patch = matplotlib.patches.PathPatch(logo_path,
                                         facecolor='none', edgecolor='black',
                                         transform=ccrs.PlateCarree())
    ax.add_patch(patch)


class Ortho(ccrs.Orthographic):
    @property
    def threshold(self):
        return self._threshold / 60.


def update(i):
    label = 'timestep {0}'.format(i)
    print(label)
    fig.clf()
    proj = Ortho(central_longitude=i, central_latitude=20)
    ax = fig.add_axes([0, 0, 1, 1], projection=proj)
    ax.coastlines()
    add_logo(ax)
    return [ax]
    
    # Update the line and the axes (with a new xlabel). Return a tuple of
    # "artists" that have to be redrawn for this frame.
#    line.set_ydata(x - 5 + i)
#    ax.set_xlabel(label)
#    return line, ax

if __name__ == '__main__':
    fps = 30
    animation_length = 12  # seconds
    anim = FuncAnimation(fig, update,
            frames=np.linspace(0., 360, fps * animation_length, endpoint=False),
            interval=1000 // fps)
    if len(sys.argv) > 1 and sys.argv[1] == 'save':
        anim.save('globe.gif', dpi=80, writer='imagemagick')
    else:
        # plt.show() will just loop the animation forever.
        plt.show()
