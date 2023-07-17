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
    "cmems_obs-oc_glo_bgc-reflectance_nrt_l3-olci-300m_P1D_202211",  # Cmems obs-oc glo bgc-reflectance NRT l3-olci-300m p1d
    "cmems_obs-oc_glo_bgc-plankton_nrt_l3-olci-300m_P1D_202207",  # Cmems obs-oc glo bgc-plankton NRT l3-olci-300m p1d
    "cmems_obs-oc_glo_bgc-optics_nrt_l3-multi-4km_P1D_202207",  # Cmems obs-oc glo bgc-optics NRT l3-multi-4km p1d
    "cmems_obs-oc_glo_bgc-transp_nrt_l3-multi-4km_P1D_202207",  # Cmems obs-oc glo bgc-transp NRT l3-multi-4km p1d
    "cmems_obs-oc_glo_bgc-plankton_nrt_l3-multi-4km_P1D_202207",  # Cmems obs-oc glo bgc-plankton NRT l3-multi-4km p1d
    "cmems_obs-oc_glo_bgc-plankton_nrt_l3-olci-4km_P1D_202207",  # Cmems obs-oc glo bgc-plankton NRT l3-olci-4km p1d
    "cmems_obs-oc_glo_bgc-reflectance_nrt_l3-multi-4km_P1D_202207",  # Cmems obs-oc glo bgc-reflectance NRT l3-multi-4km p1d
    "cmems_obs-oc_glo_bgc-reflectance_nrt_l3-olci-4km_P1D_202207",  # Cmems obs-oc glo bgc-reflectance NRT l3-olci-4km p1d
    "cmems_obs-oc_glo_bgc-transp_nrt_l3-olci-4km_P1D_202207",  # Cmems obs-oc glo bgc-transp NRT l3-olci-4km p1d
]


class oceancolour_glo_bgc_l3_nrt(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_GLO_BGC_L3_NRT_009_101"
    dataset = "EO:MO:DAT:OCEANCOLOUR_GLO_BGC_L3_NRT_009_101"

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "KD490",
            "KD490_uncertainty",
            "flags",
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
        if layer == "cmems_obs-oc_glo_bgc-reflectance_nrt_l3-olci-300m_P1D_202211":
            if start is None:
                start = "2023-07-08T21:40:52Z"

            if end is None:
                end = "2023-07-09T23:19:37Z"

        if layer == "cmems_obs-oc_glo_bgc-plankton_nrt_l3-olci-300m_P1D_202207":
            if start is None:
                start = "2023-06-28T21:09:06Z"

            if end is None:
                end = "2023-07-09T23:19:37Z"

        if layer == "cmems_obs-oc_glo_bgc-optics_nrt_l3-multi-4km_P1D_202207":
            if start is None:
                start = "2023-06-28T19:20:06Z"

            if end is None:
                end = "2023-07-10T02:44:17Z"

        if layer == "cmems_obs-oc_glo_bgc-transp_nrt_l3-multi-4km_P1D_202207":
            if start is None:
                start = "2023-06-28T13:47:27Z"

            if end is None:
                end = "2023-07-10T02:44:17Z"

        if layer == "cmems_obs-oc_glo_bgc-plankton_nrt_l3-multi-4km_P1D_202207":
            if start is None:
                start = "2023-06-28T13:47:27Z"

            if end is None:
                end = "2023-07-10T02:44:17Z"

        if layer == "cmems_obs-oc_glo_bgc-plankton_nrt_l3-olci-4km_P1D_202207":
            if start is None:
                start = "2023-06-28T20:31:25Z"

            if end is None:
                end = "2023-07-10T02:35:03Z"

        if layer == "cmems_obs-oc_glo_bgc-reflectance_nrt_l3-multi-4km_P1D_202207":
            if start is None:
                start = "2023-06-28T19:20:06Z"

            if end is None:
                end = "2023-07-10T02:44:17Z"

        if layer == "cmems_obs-oc_glo_bgc-reflectance_nrt_l3-olci-4km_P1D_202207":
            if start is None:
                start = "2023-07-05T20:50:16Z"

            if end is None:
                end = "2023-07-10T02:35:03Z"

        if layer == "cmems_obs-oc_glo_bgc-transp_nrt_l3-olci-4km_P1D_202207":
            if start is None:
                start = "2023-07-05T20:50:16Z"

            if end is None:
                end = "2023-07-10T02:35:03Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
