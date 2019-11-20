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

# Open binary diagnostic
df_trac = xbpch.open_bpchdataset(
    ARGS["trac_avg"],
    tracerinfo_file=ARGS["tracerinfo"],
    diaginfo_file=ARGS["diaginfo"],
)
df_trac


# %%

# df_ts = xbpch.open_bpchdataset(
#     "temp/geos45s/ts20150102.bpch",
#     tracerinfo_file=ARGS["tracerinfo"],
#     diaginfo_file=ARGS["diaginfo"],
# )
# df_ts


# %%

