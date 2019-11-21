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
    "trac_bpch": "temp/geos45s/trac_avg.geosfp_4x5_standard.201501010000",
    "trac_nc": "temp/geos45s/trac_avg.geosfp_4x5_standard.201501010000.nc",
    "tracerinfo": "temp/geos45s/tracerinfo.dat",
    "diaginfo": "temp/geos45s/diaginfo.dat",
    "f_out": lambda x: f"out/img/{x}_emission.png",
}

# %%


# Get value size array
def rlen(variable):
    return range(len(variable))


# %%

# Open binary diagnostic with .dat (contain tracer names and other metadata)
df_trac = xbpch.open_bpchdataset(
    ARGS["trac_bpch"],
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

# Convert BPCH data to NC format
# df_trac = xbpch.common.fix_attr_encoding(df_trac)
# df_trac.to_netcdf(ARGS["trac_nc"])


# %%

# Terminal command
# !ncdump -h temp/geos45s/trac_avg.geosfp_4x5_standard.201501010000.nc

# %%

# Open NC
# ds_nc = xr.open_dataset("trac.nc")
# ds_nc

# %%

# PM, NOx, NMVOCs
# Get emissions and times
tracers = ["IJ_AVG_S_O3", "IJ_AVG_S_NO2", "IJ_AVG_S_SO2", "IJ_AVG_S_NH3"]
emissions = df_trac[tracers]
times = [t.values.astype("datetime64[M]") for t in emissions["time"]]

# %%

for tracer in emissions:
    fig, axes = plt.subplots(
        1, 2, figsize=(10, 4), subplot_kw={"projection": ccrs.PlateCarree()}
    )

    # Plot BPCH diagnotics for each time
    for ax, t in zip(axes, rlen(times)):
        emissions[tracer].isel(time=t, lev=0).plot(
            ax=ax, cmap=WhGrYlRd, cbar_kwargs={"shrink": 0.5, "label": "ppbv"}
        )
        ax.set_title(f"{tracer} emission - {times[t]}")
        ax.coastlines()
        ax.gridlines(linestyle="--")

    plt.savefig(ARGS["f_out"](tracer))


# %%
