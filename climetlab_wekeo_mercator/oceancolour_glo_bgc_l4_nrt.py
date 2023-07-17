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
    "cmems_obs-oc_glo_bgc-plankton_nrt_l4-olci-300m_P1M_202211",  # Cmems obs-oc glo bgc-plankton NRT l4-olci-300m p1m
    "cmems_obs-oc_glo_bgc-reflectance_nrt_l4-olci-300m_P1M_202211",  # Cmems obs-oc glo bgc-reflectance NRT l4-olci-300m p1m
    "cmems_obs-oc_glo_bgc-transp_nrt_l4-multi-4km_P1M_202207",  # Cmems obs-oc glo bgc-transp NRT l4-multi-4km p1m
    "cmems_obs-oc_glo_bgc-reflectance_nrt_l4-multi-4km_P1M_202207",  # Cmems obs-oc glo bgc-reflectance NRT l4-multi-4km p1m
    "cmems_obs-oc_glo_bgc-plankton_nrt_l4-olci-4km_P1M_202207",  # Cmems obs-oc glo bgc-plankton NRT l4-olci-4km p1m
    "cmems_obs-oc_glo_bgc-transp_nrt_l4-gapfree-multi-4km_P1D_202207",  # Cmems obs-oc glo bgc-transp NRT l4-gapfree-multi-4km p1d
    "cmems_obs-oc_glo_bgc-plankton_nrt_l4-multi-4km_P1M_202207",  # Cmems obs-oc glo bgc-plankton NRT l4-multi-4km p1m
    "cmems_obs-oc_glo_bgc-plankton_nrt_l4-gapfree-multi-4km_P1D_202207",  # Cmems obs-oc glo bgc-plankton NRT l4-gapfree-multi-4km p1d
    "cmems_obs-oc_glo_bgc-pp_nrt_l4-multi-4km_P1M_202207",  # Cmems obs-oc glo bgc-pp NRT l4-multi-4km p1m
    "cmems_obs-oc_glo_bgc-reflectance_nrt_l4-olci-4km_P1M_202207",  # Cmems obs-oc glo bgc-reflectance NRT l4-olci-4km p1m
    "cmems_obs-oc_glo_bgc-transp_nrt_l4-olci-4km_P1M_202207",  # Cmems obs-oc glo bgc-transp NRT l4-olci-4km p1m
    "cmems_obs-oc_glo_bgc-optics_nrt_l4-multi-4km_P1M_202207",  # Cmems obs-oc glo bgc-optics NRT l4-multi-4km p1m
]


class oceancolour_glo_bgc_l4_nrt(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_GLO_BGC_L4_NRT_009_102"
    dataset = "EO:MO:DAT:OCEANCOLOUR_GLO_BGC_L4_NRT_009_102"

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "BBP",
            "BBP_uncertainty",
            "CDM",
            "CDM_uncertainty",
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
        if layer == "cmems_obs-oc_glo_bgc-plankton_nrt_l4-olci-300m_P1M_202211":
            if start is None:
                start = "2023-05-31T21:28:11Z"

            if end is None:
                end = "2023-06-29T12:23:34Z"

        if layer == "cmems_obs-oc_glo_bgc-reflectance_nrt_l4-olci-300m_P1M_202211":
            if start is None:
                start = "2023-05-31T21:28:11Z"

            if end is None:
                end = "2023-06-29T12:23:34Z"

        if layer == "cmems_obs-oc_glo_bgc-transp_nrt_l4-multi-4km_P1M_202207":
            if start is None:
                start = "2023-05-31T18:54:14Z"

            if end is None:
                end = "2023-07-01T02:56:18Z"

        if layer == "cmems_obs-oc_glo_bgc-reflectance_nrt_l4-multi-4km_P1M_202207":
            if start is None:
                start = "2023-05-31T22:50:02Z"

            if end is None:
                end = "2023-07-01T02:35:59Z"

        if layer == "cmems_obs-oc_glo_bgc-plankton_nrt_l4-olci-4km_P1M_202207":
            if start is None:
                start = "2023-05-31T20:58:04Z"

            if end is None:
                end = "2023-06-29T09:41:43Z"

        if layer == "cmems_obs-oc_glo_bgc-transp_nrt_l4-gapfree-multi-4km_P1D_202207":
            if start is None:
                start = "2023-06-28T13:47:27Z"

            if end is None:
                end = "2023-07-10T02:44:17Z"

        if layer == "cmems_obs-oc_glo_bgc-plankton_nrt_l4-multi-4km_P1M_202207":
            if start is None:
                start = "2023-04-30T20:02:03Z"

            if end is None:
                end = "2023-06-01T03:10:24Z"

        if layer == "cmems_obs-oc_glo_bgc-plankton_nrt_l4-gapfree-multi-4km_P1D_202207":
            if start is None:
                start = "2023-06-28T13:47:27Z"

            if end is None:
                end = "2023-07-10T02:44:17Z"

        if layer == "cmems_obs-oc_glo_bgc-pp_nrt_l4-multi-4km_P1M_202207":
            if start is None:
                start = "2023-05-31T18:54:14Z"

            if end is None:
                end = "2023-07-01T02:56:18Z"

        if layer == "cmems_obs-oc_glo_bgc-reflectance_nrt_l4-olci-4km_P1M_202207":
            if start is None:
                start = "2023-05-31T20:58:04Z"

            if end is None:
                end = "2023-06-29T09:41:43Z"

        if layer == "cmems_obs-oc_glo_bgc-transp_nrt_l4-olci-4km_P1M_202207":
            if start is None:
                start = "2023-05-31T20:58:04Z"

            if end is None:
                end = "2023-06-29T09:41:43Z"

        if layer == "cmems_obs-oc_glo_bgc-optics_nrt_l4-multi-4km_P1M_202207":
            if start is None:
                start = "2023-05-31T22:50:02Z"

            if end is None:
                end = "2023-07-01T02:35:59Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
