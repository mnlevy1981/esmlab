#!/usr/bin/env python

import os
import sys

import numpy as np
import pytest
import xarray as xr

from esmlab.datasets import open_dataset
from esmlab.regrid import regridder


@pytest.mark.skipif(sys.version_info[0] < 3, reason="requires python3")
def test_regrid_init():

    R = regridder(
        name_grid_src="T62",
        name_grid_dst="CAM_f09",
        method="bilinear",
        overwrite_existing=True,
    )

    assert isinstance(R, regridder)


@pytest.mark.skipif(sys.version_info[0] < 3, reason="requires python3")
def test_regrid_regrid():

    R = regridder(
        name_grid_src="T62",
        name_grid_dst="CAM_f09",
        method="bilinear",
        overwrite_existing=False,
    )
    ds = open_dataset(name="ncep_t_10_T62_2009_time0")
    dao = R(ds.t_10)
    print(dao)
    assert isinstance(dao, xr.DataArray)
