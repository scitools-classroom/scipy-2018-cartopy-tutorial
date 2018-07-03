
// Don't use the standard CSS import mechanism so that we can easily support directories of notebooks.
$('head').append('<link rel="stylesheet" href="/files/static/theme/rise.css" type="text/css" />');

header = `
<a href="https://scitools.org.uk">
    <img src="https://scitools.org.uk/static/images/logo.200x200-trans-white-122x122.png" style="height: 4.5rem;" />
    SciTools
</a>
<div style="float: right;">
    <img src="/files/static/theme/favicon.png" style="height: 3.8rem;">
    Cartopy tutorial | SciPy 2018
</div>
`;

footer = `
<a href="https://github.com/scitools/cartopy-tutorial">github.com/scitools/cartopy-tutorial</a>

<div style="float: right;">Phil Elson & Bill Little</div>
`;


$('#rise-header').html(header);
$('#rise-footer').html(footer);


index = Reveal.getIndices();
if (index.h == 0 & index.v == 0) {
    onFirstSlide();
}

Reveal.addEventListener('slidechanged', function(evt) {
  if (evt.indexh == 0 & evt.indexv == 0) {
    onFirstSlide();
  }
});


function onFirstSlide() {
  // Do the thing when first slide is being shown.
}
