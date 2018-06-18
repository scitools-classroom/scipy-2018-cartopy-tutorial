"""
Test import of packages for the tutorial

"""
from __future__ import print_function

import importlib
import sys


def version(pkg):
    try:
        mod = importlib.import_module(pkg)
        print(OK, '%s version %s' % (pkg, mod.__version__))
    except ImportError:
        print(FAIL, '%s not installed' % pkg)

try:
    import curses
    curses.setupterm()
    assert curses.tigetnum("colors") > 2
    OK = "\x1b[1;%dm[ OK ]\x1b[0m" % (30 + curses.COLOR_GREEN)
    FAIL = "\x1b[1;%dm[FAIL]\x1b[0m" % (30 + curses.COLOR_RED)
except:
    OK = '[ OK ]'
    FAIL = '[FAIL]'

print('Using python in', sys.prefix)
print(sys.version)

print()
print('Required packages:')

version('cartopy')
version('folium')
version('fiona')
version('geopandas')
version('iris')
version('matplotlib')
version('notebook')
version('numpy')
version('skimage')
version('shapely')
version('xarray')
print()
