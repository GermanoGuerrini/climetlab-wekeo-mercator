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
    "global-reanalysis-phy-001-026-grepv1-monthly_202003",  # Monthly mean from reanalyses
    "global-reanalysis-phy-001-026-grepv1-uv-monthly_202003",  # Monthly mean from reanalyses
    "global-reanalysis-phy-001-026-grepv1-ice-monthly_202003",  # Monthly mean from reanalyses
]


class global_reanalysis_phy(Main):
    name = "EO:MO:DAT:GLOBAL_REANALYSIS_PHY_001_026"
    dataset = "EO:MO:DAT:GLOBAL_REANALYSIS_PHY_001_026"

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "latitude",
            "longitude",
            "siconc_cglo",
            "siconc_foam",
            "siconc_glor",
            "siconc_mean",
            "siconc_oras",
            "siconc_std",
            "sithick_cglo",
            "sithick_foam",
            "sithick_glor",
            "sithick_mean",
            "sithick_oras",
            "sithick_std",
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
        if layer == "global-reanalysis-phy-001-026-grepv1-monthly_202003":
            if start is None:
                start = "1993-01-15T00:00:00Z"

            if end is None:
                end = "2020-12-15T00:00:00Z"

        if layer == "global-reanalysis-phy-001-026-grepv1-uv-monthly_202003":
            if start is None:
                start = "1993-01-15T00:00:00Z"

            if end is None:
                end = "2020-12-15T00:00:00Z"

        if layer == "global-reanalysis-phy-001-026-grepv1-ice-monthly_202003":
            if start is None:
                start = "1993-01-15T00:00:00Z"

            if end is None:
                end = "2020-12-15T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
