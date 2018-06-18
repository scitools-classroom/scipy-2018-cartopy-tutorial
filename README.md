<!-- markdownlint-disable -->
<h1 align="center" style="margin:1em">
  <a href="https://github.com/scitools/cartopy-tutorial">
    <img src="static/around_the_world.jpg" width="200"></a>
  <br />
  Around the world in 80 ways: An introduction to working with geodata and cartopy
</h1>

## Note

This repository is still under development. Please check back closer to the time for the complete
tutorial material.
In the meantime, please feel free to install the dependencies documented in
[``requirement.txt``](requirements.txt) to speed up installation on the day.

<!-- TOC -->

+ [SciPy 2018](#scipy-2018)
+ [Installation / set-up](#installation)

<!-- /TOC -->


# [SciPy 2018](https://scipy2018.scipy.org/ehome/index.php?eventid=299527&tabid=711308&cid=2229599&sessionid=21549174&sessionchoice=1&)

Date: 8am on Monday 9th July, 2018

Download: scipy-2018 git tag (available from around 6th July), see also
[releases](https://github.com/SciTools/cartopy-tutorial/releases/)

## Abstract

On the 1st of October 1872, Jules Verne’s character Phileas Fogg embarks on an adventure to circumnavigate the world in just 80 days. Travelling exclusively by sea and rail, Fogg voyages from the misty alleys of Victorian London to the exotic subcontinent and the Wild West in a race against the clock. Despite fastidiously counting each sunrise, he famously neglects the effect of crossing the dateline and thus arrives on a different day to the one he calculated.
 
The mistreatment of the dateline is far from unique to Phileas Fogg; it is not just the 24hr time discontinuity that we struggle with - the antimeridian is also a longitudinal discontinuity of 360 degrees for coordinate systems centered at the Greenwich Prime meridian. Whilst Cartesian treatment of geospatial data is a reasonable assumption with an appropriately transformed coordinate system and at large scale (small area), the discontinuities of the antimeridian and the poles frequently wreak havoc on our Cartesian tools when we treat larger area (global / small scale) data.
  
In this tutorial, join Phileas Elson on our own epic adventure by tracking Fogg’s travel log with careful non-Cartesian treatment as we go. Along the way, we will discover how many of the python libraries we may already know and love can be used in conjunction with cartopy to provide a powerful suite of open source geospatial tools.
   
We will cover many of the core concepts in cartopy, including topics such as: coordinate reference systems and projections; the matplotlib interface; geospatial image, data (NetCDF) and raster treatment; as well as geometry predicates and transformations. The knowledge developed from this tutorial will be applicable to a broad range of geospatial analyses (both raster and vector), and will provide hands-on experience of tools such as numpy, proj.4, matplotlib and shapely to name a few.
    
The tutorial will be applicable to a broad range of experiences, but familiarity with numpy and matplotlib will be essential to enable progress through the exercises. A prior awareness of tools such as shapely, proj.4, geopandas, and xarray/Iris will help, though are by no means essential. The tutorial will be made up of a number of exercises with each being designed to accommodate a broad range of expertise.


# Installation

Please see the [dependency requirements](requirements.txt) for a list of packages needed
to participate in this tutorial.

Of significant note is that this tutorial is only designed for Python 3.6 or greater.
Whilst most of the tools are available for earlier versions of Python, the tutorial
itself isn't (and will never be).

## Conda

Conda is the recommended tool for installing the dependencies of this tutorial.
Users of conda or Anaconda can install the dependencies into a clean environment with:

```
conda create --file=requirements.txt --channel=conda-forge --name=scipy-cartopy-tutorial
```

There are a number of large packages in the ``requirements.txt``, and this could take a
few minutes to download.

Once installed, the environment can be activated as usual with:

```
conda activate scipy-cartopy-tutorial
```

Or for users of older versions of conda ``source activate scipy-cartopy-tutorial``.


## Pip

``pip`` is not recommended for installing this tutorial's dependencies.
This is mostly because there are a number of non-trivial (non-python) packages
that need to be installed. These are the kinds of packages that a tool like conda
was designed for.

## conda environment file

The conda environment under which the tutorial was originally written is available
in ``env-exports/${platform}.txt``. This may be useful in ascertaining specific
dependency versions were used when developing.

These were produced with ``conda list --explicit > env-exports/${platform}.txt``.
