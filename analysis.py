#!/usr/bin/env python
# -*- coding: utf-8 -*-

# %%

from temp.gamap_colormap import WhGrYlRd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
import xarray as xr
import xbpch

import warnings

warnings.filterwarnings("ignore")  # hide some xbpch warnings

# %%

ARGS = {
    "trac45s": "temp/geos45s/trac_avg.geosfp_4x5_standard.201501010000",
    "tracerinfo": "temp/geos45s/tracerinfo.dat",
    "diaginfo": "temp/geos45s/diaginfo.dat",
}

# %%

ds_bp = xbpch.open_bpchdataset(
    ARGS["trac45s"],
    tracerinfo_file=ARGS["tracerinfo"],
    diaginfo_file=ARGS["diaginfo"],
)
ds_bp


# %%
