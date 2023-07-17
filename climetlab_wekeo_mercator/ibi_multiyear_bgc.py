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
    "cmems_mod_ibi_bgc_my_0.083deg-3D_P1Y-m_202211",  # Cmems ibi reanalysis: yearly biogeochemical products
    "cmems_mod_ibi_bgc_my_0.083deg-3D_P1M-m_202012",  # Cmems ibi reanalysis: monthly biogeochemical products
    "cmems_mod_ibi_bgc_my_0.083deg-3D-climatology_P1M-m_202211",  # cmems_mod_ibi_bgc_my_0.083deg-3D-climatology_P1M-m_202211
    "cmems_mod_ibi_bgc_my_0.083deg-3D_P1D-m_202012",  # Cmems ibi reanalysis: daily biogeochemical products
]


class ibi_multiyear_bgc(Main):
    name = "EO:MO:DAT:IBI_MULTIYEAR_BGC_005_003"
    dataset = "EO:MO:DAT:IBI_MULTIYEAR_BGC_005_003"

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "chl",
            "depth",
            "dissic",
            "fe",
            "latitude",
            "longitude",
            "nh4",
            "no3",
            "nppv",
            "o2",
            "ph",
            "phyc",
            "po4",
            "si",
            "spco2",
            "time",
            "zeu",
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
        if layer == "cmems_mod_ibi_bgc_my_0.083deg-3D_P1Y-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-01-01T00:00:00Z"

        if layer == "cmems_mod_ibi_bgc_my_0.083deg-3D_P1M-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2023-01-01T00:00:00Z"

        if layer == "cmems_mod_ibi_bgc_my_0.083deg-3D-climatology_P1M-m_202211":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2022-11-28T00:00:00Z"

        if layer == "cmems_mod_ibi_bgc_my_0.083deg-3D_P1D-m_202012":
            if start is None:
                start = "2020-12-01T00:00:00Z"

            if end is None:
                end = "2023-01-01T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
