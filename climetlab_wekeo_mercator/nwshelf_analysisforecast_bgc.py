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
    "cmems_mod_nws_bgc-no3_anfc_7km-3D_P1D-m_202105",  # Daily-mean nitrate (3d)
    "cmems_mod_nws_bgc-pp_anfc_7km-3D_P1D-m_202105",  # Daily-mean primary productivity (3d)
    "cmems_mod_nws_bgc-kd_anfc_7km-3D_P1D-m_202105",  # Daily-mean attenuation coefficient (3d)
    "cmems_mod_nws_bgc-spco2_anfc_7km-2D_P1D-m_202105",  # Daily-mean spco2 (2d)
    "cmems_mod_nws_bgc-phyc_anfc_7km-3D_P1D-m_202105",  # Daily-mean phytoplankton (3d)
    "cmems_mod_nws_bgc-o2_anfc_7km-3D_P1D-m_202105",  # Daily-mean dissolved oxygen (3d)
    "cmems_mod_nws_bgc-chl_anfc_7km-3D_P1D-m_202105",  # Daily-mean chlorophyll concentration (3d)
    "cmems_mod_nws_bgc-po4_anfc_7km-3D_P1D-m_202105",  # Daily-mean phosphate (3d)
    "cmems_mod_nws_bgc-ph_anfc_7km-3D_P1D-m_202105",  # Daily-mean ph (3d)
]


class nwshelf_analysisforecast_bgc(Main):
    name = "EO:MO:DAT:NWSHELF_ANALYSISFORECAST_BGC_004_002"
    dataset = "EO:MO:DAT:NWSHELF_ANALYSISFORECAST_BGC_004_002"

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
            "ph",
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
        if layer == "cmems_mod_nws_bgc-no3_anfc_7km-3D_P1D-m_202105":
            if start is None:
                start = "2019-05-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-pp_anfc_7km-3D_P1D-m_202105":
            if start is None:
                start = "2019-05-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-kd_anfc_7km-3D_P1D-m_202105":
            if start is None:
                start = "2019-05-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-spco2_anfc_7km-2D_P1D-m_202105":
            if start is None:
                start = "2019-05-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-phyc_anfc_7km-3D_P1D-m_202105":
            if start is None:
                start = "2019-05-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-o2_anfc_7km-3D_P1D-m_202105":
            if start is None:
                start = "2019-05-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-chl_anfc_7km-3D_P1D-m_202105":
            if start is None:
                start = "2019-05-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-po4_anfc_7km-3D_P1D-m_202105":
            if start is None:
                start = "2019-05-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "cmems_mod_nws_bgc-ph_anfc_7km-3D_P1D-m_202105":
            if start is None:
                start = "2019-05-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
