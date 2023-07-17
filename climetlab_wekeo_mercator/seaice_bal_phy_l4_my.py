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
    "cmems_obs-si_bal_seaice-conc_my_1km_202112",  # Baltic ice concentration and classification, l4, 1km daily
    "cmems_obs-si_bal_phy-sit_my_l4-1km_P1D-m_202211",  # Baltic ice thickness, l4, 1km daily
]


class seaice_bal_phy_l4_my(Main):
    name = "EO:MO:DAT:SEAICE_BAL_PHY_L4_MY_011_019"
    dataset = "EO:MO:DAT:SEAICE_BAL_PHY_L4_MY_011_019"

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "crs",
            "ice_thickness",
            "lat",
            "lon",
            "product_quality",
            "thickness_range",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        area=None,
        start=None,
        end=None,
        variables=None,
    ):
        if layer == "cmems_obs-si_bal_seaice-conc_my_1km_202112":
            if start is None:
                start = "1980-11-03T14:00:00Z"

            if end is None:
                end = "2022-05-30T14:00:00Z"

        if layer == "cmems_obs-si_bal_phy-sit_my_l4-1km_P1D-m_202211":
            if start is None:
                start = "1980-11-03T14:00:00Z"

            if end is None:
                end = "2022-05-30T14:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
