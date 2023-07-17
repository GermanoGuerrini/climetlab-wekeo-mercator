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
    "cmems_obs-oc_bal_bgc-reflectance_nrt_l3-olci-300m_P1D_202207",  # Cmems obs-oc bal bgc-reflectance NRT l3-olci-300m p1d
    "cmems_obs-oc_bal_bgc-transp_nrt_l3-olci-300m_P1D_202207",  # Cmems obs-oc bal bgc-transp NRT l3-olci-300m p1d
    "cmems_obs-oc_bal_bgc-plankton_nrt_l3-olci-300m_P1D_202211",  # Cmems obs-oc bal bgc-plankton NRT l3-olci-300m p1d
    "cmems_obs-oc_bal_bgc-optics_nrt_l3-olci-300m_P1D_202207",  # Cmems obs-oc bal bgc-optics NRT l3-olci-300m p1d
]


class oceancolour_bal_bgc_l3_nrt(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_BAL_BGC_L3_NRT_009_131"
    dataset = "EO:MO:DAT:OCEANCOLOUR_BAL_BGC_L3_NRT_009_131"

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "ADG443",
            "APH443",
            "BBP443",
            "SENSORMASK",
            "lat",
            "lon",
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
        if layer == "cmems_obs-oc_bal_bgc-reflectance_nrt_l3-olci-300m_P1D_202207":
            if start is None:
                start = "2023-06-04T00:00:00Z"

            if end is None:
                end = "2023-07-09T00:00:00Z"

        if layer == "cmems_obs-oc_bal_bgc-transp_nrt_l3-olci-300m_P1D_202207":
            if start is None:
                start = "2023-06-04T00:00:00Z"

            if end is None:
                end = "2023-07-09T00:00:00Z"

        if layer == "cmems_obs-oc_bal_bgc-plankton_nrt_l3-olci-300m_P1D_202211":
            if start is None:
                start = "2023-06-04T00:00:00Z"

            if end is None:
                end = "2023-07-09T00:00:00Z"

        if layer == "cmems_obs-oc_bal_bgc-optics_nrt_l3-olci-300m_P1D_202207":
            if start is None:
                start = "2023-06-04T00:00:00Z"

            if end is None:
                end = "2023-07-09T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
