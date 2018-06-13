<!-- markdownlint-disable -->
<h1 align="center" style="margin:1em">
  <a href="https://github.com/scitools/">
    <img src="https://github.com/DenisCarriere/geocoder/raw/master/docs/_static/geocoder.png"
         alt="Markdownify"
         width="200"></a>
  <br />
  Around the world in 80 ways: An introduction to working with geodata and cartopy
</h1>

<h4 align="center">
  Presented at <a href="https://scipy2018.scipy.org">SciPy 2018</a>
</h4>


<!-- TOC -->

+ [Abstract](#abstract)

<!-- /TOC -->


# Abstract


On the 1st of October 1872, Jules Verne’s character Phileas Fogg embarks on an adventure to circumnavigate the world in just 80 days. Travelling exclusively by sea and rail, Fogg voyages from the misty alleys of Victorian London to the exotic subcontinent and the Wild West in a race against the clock. Despite fastidiously counting each sunrise, he famously neglects the effect of crossing the dateline and thus arrives on a different day to the one he calculated.
 
The mistreatment of the dateline is far from unique to Phileas Fogg; it is not just the 24hr time discontinuity that we struggle with - the antimeridian is also a longitudinal discontinuity of 360 degrees for coordinate systems centered at the Greenwich Prime meridian. Whilst Cartesian treatment of geospatial data is a reasonable assumption with an appropriately transformed coordinate system and at large scale (small area), the discontinuities of the antimeridian and the poles frequently wreak havoc on our Cartesian tools when we treat larger area (global / small scale) data.
  
In this tutorial, join Phileas Elson on our own epic adventure by tracking Fogg’s travel log with careful non-Cartesian treatment as we go. Along the way, we will discover how many of the python libraries we may already know and love can be used in conjunction with cartopy to provide a powerful suite of open source geospatial tools.
   
We will cover many of the core concepts in cartopy, including topics such as: coordinate reference systems and projections; the matplotlib interface; geospatial image, data (NetCDF) and raster treatment; as well as geometry predicates and transformations. The knowledge developed from this tutorial will be applicable to a broad range of geospatial analyses (both raster and vector), and will provide hands-on experience of tools such as numpy, proj.4, matplotlib and shapely to name a few.
    
The tutorial will be applicable to a broad range of experiences, but familiarity with numpy and matplotlib will be essential to enable progress through the exercises. A prior awareness of tools such as shapely, proj.4, geopandas, and xarray/Iris will help, though are by no means essential. The tutorial will be made up of a number of exercises with each being designed to accommodate a broad range of expertise. 
