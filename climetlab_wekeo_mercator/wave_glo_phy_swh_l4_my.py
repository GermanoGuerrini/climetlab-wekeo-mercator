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
    "cmems_obs-wave_glo_phy-swh_my_multi-l4-2deg_P1D_202112",  # Multi-year merged all satellites global ocean gridded significant wave height l4 product and derived variables
]


class wave_glo_phy_swh_l4_my(Main):
    name = "EO:MO:DAT:WAVE_GLO_PHY_SWH_L4_MY_014_007"
    dataset = "EO:MO:DAT:WAVE_GLO_PHY_SWH_L4_MY_014_007"

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
            "VAVH_DAILY_MAX",
            "VAVH_DAILY_MEAN",
            "VAVH_DAILY_NBR",
            "VAVH_DAILY_STD",
            "VAVH_INST",
            "VAVH_INST_NBR",
            "VAVH_INST_SCORE",
            "lat_bnds",
            "latitude",
            "lon_bnds",
            "longitude",
            "nv",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer="cmems_obs-wave_glo_phy-swh_my_multi-l4-2deg_P1D_202112",
        area=None,
        start=None,
        end=None,
        variables=None,
    ):
        if layer == "cmems_obs-wave_glo_phy-swh_my_multi-l4-2deg_P1D_202112":
            if start is None:
                start = "2002-01-15T12:00:00Z"

            if end is None:
                end = "2020-12-31T12:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
