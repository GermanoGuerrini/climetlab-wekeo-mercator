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
    "dataset-armor-3d-nrt-monthly_202012",  # Armor3d NRT - tshuvmld global ocean observation-based product monthly average
    "dataset-armor-3d-nrt-weekly_202012",  # Armor3d NRT - tshuvmld global ocean observation-based product
    "dataset-armor-3d-rep-monthly_202012",  # Armor3d rep - tshuvmld global ocean observation-based product monthly average
    "dataset-armor-3d-rep-weekly_202012",  # Armor3d rep - tshuvmld global ocean observation-based product
]


class multiobs_glo_phy_tsuv_3d_mynrt(Main):
    name = "EO:MO:DAT:MULTIOBS_GLO_PHY_TSUV_3D_MYNRT_015_012"
    dataset = "EO:MO:DAT:MULTIOBS_GLO_PHY_TSUV_3D_MYNRT_015_012"

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
            "depth",
            "latitude",
            "longitude",
            "mlotst",
            "so",
            "time",
            "to",
            "ugo",
            "vgo",
            "zo",
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
        if layer == "dataset-armor-3d-rep-weekly_202012":
            if start is None:
                start = "2020-10-23T00:00:00Z"

            if end is None:
                end = "2022-11-19T00:00:00Z"

        if layer == "dataset-armor-3d-nrt-weekly_202012":
            if start is None:
                start = "2020-11-16T00:00:00Z"

            if end is None:
                end = "2023-07-25T00:00:00Z"

        if layer == "dataset-armor-3d-nrt-monthly_202012":
            if start is None:
                start = "2020-11-17T00:00:00Z"

            if end is None:
                end = "2023-07-11T00:00:00Z"

        if layer == "dataset-armor-3d-rep-monthly_202012":
            if start is None:
                start = "2020-11-06T00:00:00Z"

            if end is None:
                end = "2023-07-20T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
