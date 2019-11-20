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

# Files path
ARGS = {
    "trac_avg": "temp/geos45s/trac_avg.geosfp_4x5_standard.201501010000",
    "tracerinfo": "temp/geos45s/tracerinfo.dat",
    "diaginfo": "temp/geos45s/diaginfo.dat",
}

# %%

# Open binary diagnostic with .dat (contain tracer names and other metadata)
df_trac = xbpch.open_bpchdataset(
    ARGS["trac_avg"],
    tracerinfo_file=ARGS["tracerinfo"],
    diaginfo_file=ARGS["diaginfo"],
)
df_trac

# %%

# Select variable
df_trac["IJ_AVG_S_CO"]

# %%

# Select time boundaries
df_trac["time_bnds"]

# %%

# Drop time boundaries and redudant dimension
df_trac = df_trac.drop("time_bnds")
df_trac = df_trac.drop("nv")

# %%

# Changes order (time, lon, lat, lev) to common order (time, lev, lat, lon)
# df_trac = df_trac.transpose("time", "lev", "lat", "lon")
# df_trac

# %%
