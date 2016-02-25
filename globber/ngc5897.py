from __future__ import division, print_function

__author__ = "adrn <adrn@astro.columbia.edu>"

# Third-party
import astropy.coordinates as coord
import astropy.units as u
import numpy as np

cluster_c = coord.SkyCoord(ra=229.352*u.degree,
                           dec=-21.01*u.degree)
cluster_pad = {
    'inner': 4*u.arcmin,
    'outer': 15*u.arcmin
}

# what photometry do we want to use? g,r,i,z,y
mixing_matrix = np.array([[0, 0, 1, 0, 0],    # i magnitude
                          [1, -1, 0, 0, 0],   # g-r color
                          [1, 0, -1, 0, 0],   # g-i
                          [1, 0, 0, -1, 0],   # g-z
                          [0, 1, 0, -1, 0]])  # r-z

magnitude_lims = {
    'i': (17,21)
}

color_lims = {
    ('g','r'): (-0.1,0.7),
    ('g','i'): (-0.1,1.),
    ('g','z'): (-0.1,1.1),
    ('r','z'): (-0.2,0.5),
}
