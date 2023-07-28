#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations
from climetlab.decorators import normalize

from climetlab_wekeo_mercator.main import Main

LAYERS = [
    "cmems_obs-si_ant_phy_nrt_l3-1km_P1D_202303",  # Dmi-asip sea ice classification - antarctica
]


class seaice_ant_phy_auto_l3_nrt(Main):
    name = "EO:MO:DAT:SEAICE_ANT_PHY_AUTO_L3_NRT_011_012"
    dataset = "EO:MO:DAT:SEAICE_ANT_PHY_AUTO_L3_NRT_011_012"

    string_selects = [
        "variables",
    ]

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "acq_time",
            "confidence",
            "crs",
            "ice_concentration",
            "lat",
            "lon",
            "time",
            "x",
            "y",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer="cmems_obs-si_ant_phy_nrt_l3-1km_P1D_202303",
        area=None,
        start=None,
        end=None,
        variables=None,
    ):
        if layer == "cmems_obs-si_ant_phy_nrt_l3-1km_P1D_202303":
            if start is None:
                start = "2023-02-02T13:35:15Z"

            if end is None:
                end = "2023-07-26T19:20:55Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
