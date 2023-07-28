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
    "cmems_obs-oc_glo_bgc-optics_my_l4-multi-4km_P1M_202211",  # Cmems obs-oc glo bgc-optics my l4-multi-4km p1m
    "cmems_obs-oc_glo_bgc-plankton_my_l4-gapfree-multi-4km_P1D_202207",  # Cmems obs-oc glo bgc-plankton my l4-gapfree-multi-4km p1d
    "cmems_obs-oc_glo_bgc-plankton_my_l4-multi-4km_P1M_202207",  # Cmems obs-oc glo bgc-plankton my l4-multi-4km p1m
    "cmems_obs-oc_glo_bgc-plankton_my_l4-multi-climatology-4km_P1D_202207",  # cmems_obs-oc_glo_bgc-plankton_my_l4-multi-climatology-4km_P1D_202207
    "cmems_obs-oc_glo_bgc-plankton_my_l4-olci-300m_P1M_202211",  # Cmems obs-oc glo bgc-plankton my l4-olci-300m p1m
    "cmems_obs-oc_glo_bgc-plankton_my_l4-olci-4km_P1M_202207",  # Cmems obs-oc glo bgc-plankton my l4-olci-4km p1m
    "cmems_obs-oc_glo_bgc-pp_my_l4-multi-4km_P1M_202207",  # Cmems obs-oc glo bgc-pp my l4-multi-4km p1m
    "cmems_obs-oc_glo_bgc-reflectance_my_l4-multi-4km_P1M_202207",  # Cmems obs-oc glo bgc-reflectance my l4-multi-4km p1m
    "cmems_obs-oc_glo_bgc-reflectance_my_l4-olci-300m_P1M_202211",  # Cmems obs-oc glo bgc-reflectance my l4-olci-300m p1m
    "cmems_obs-oc_glo_bgc-reflectance_my_l4-olci-4km_P1M_202207",  # Cmems obs-oc glo bgc-reflectance my l4-olci-4km p1m
    "cmems_obs-oc_glo_bgc-transp_my_l4-gapfree-multi-4km_P1D_202207",  # Cmems obs-oc glo bgc-transp my l4-gapfree-multi-4km p1d
    "cmems_obs-oc_glo_bgc-transp_my_l4-multi-4km_P1M_202207",  # Cmems obs-oc glo bgc-transp my l4-multi-4km p1m
    "cmems_obs-oc_glo_bgc-transp_my_l4-olci-4km_P1M_202207",  # Cmems obs-oc glo bgc-transp my l4-olci-4km p1m
]


class oceancolour_glo_bgc_l4_my(Main):
    name = "EO:MO:DAT:OCEANCOLOUR_GLO_BGC_L4_MY_009_104"
    dataset = "EO:MO:DAT:OCEANCOLOUR_GLO_BGC_L4_MY_009_104"

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
            "BBP",
            "BBP_uncertainty",
            "CDM",
            "CDM_uncertainty",
            "CHL",
            "CHL_count",
            "CHL_maximum",
            "CHL_mean",
            "CHL_median",
            "CHL_minimum",
            "CHL_percentile_3",
            "CHL_percentile_97",
            "CHL_percentile_standard_deviation",
            "CHL_standard_deviation",
            "CHL_uncertainty",
            "DIATO",
            "DIATO_uncertainty",
            "DINO",
            "DINO_uncertainty",
            "GREEN",
            "GREEN_uncertainty",
            "HAPTO",
            "HAPTO_uncertainty",
            "KD490",
            "KD490_uncertainty",
            "MICRO",
            "MICRO_uncertainty",
            "NANO",
            "NANO_uncertainty",
            "PICO",
            "PICO_uncertainty",
            "PP",
            "PP_uncertainty",
            "PROCHLO",
            "PROCHLO_uncertainty",
            "PROKAR",
            "PROKAR_uncertainty",
            "RRS400",
            "RRS400_uncertainty",
            "RRS412",
            "RRS412_uncertainty",
            "RRS443",
            "RRS443_uncertainty",
            "RRS490",
            "RRS490_uncertainty",
            "RRS510",
            "RRS510_uncertainty",
            "RRS555",
            "RRS555_uncertainty",
            "RRS560",
            "RRS560_uncertainty",
            "RRS620",
            "RRS620_uncertainty",
            "RRS665",
            "RRS665_uncertainty",
            "RRS670",
            "RRS670_uncertainty",
            "RRS674",
            "RRS674_uncertainty",
            "RRS681",
            "RRS681_uncertainty",
            "RRS709",
            "RRS709_uncertainty",
            "SPM",
            "SPM_uncertainty",
            "ZSD",
            "ZSD_uncertainty",
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
        if layer == "cmems_obs-oc_glo_bgc-transp_my_l4-olci-4km_P1M_202207":
            if start is None:
                start = "2016-04-25T11:34:53Z"

            if end is None:
                end = "2023-07-01T06:29:17Z"

        if layer == "cmems_obs-oc_glo_bgc-optics_my_l4-multi-4km_P1M_202211":
            if start is None:
                start = "1997-09-04T16:26:34Z"

            if end is None:
                end = "2023-07-01T02:35:59Z"

        if layer == "cmems_obs-oc_glo_bgc-plankton_my_l4-olci-4km_P1M_202207":
            if start is None:
                start = "2016-04-25T11:34:53Z"

            if end is None:
                end = "2023-07-01T06:29:17Z"

        if layer == "cmems_obs-oc_glo_bgc-pp_my_l4-multi-4km_P1M_202207":
            if start is None:
                start = "1997-09-04T16:26:34Z"

            if end is None:
                end = "2023-07-01T08:10:11Z"

        if layer == "cmems_obs-oc_glo_bgc-plankton_my_l4-olci-300m_P1M_202211":
            if start is None:
                start = "2016-04-25T11:40:53Z"

            if end is None:
                end = "2023-07-01T08:06:14Z"

        if layer == "cmems_obs-oc_glo_bgc-plankton_my_l4-multi-4km_P1M_202207":
            if start is None:
                start = "1997-09-04T16:26:34Z"

            if end is None:
                end = "2023-07-01T08:10:11Z"

        if (
            layer
            == "cmems_obs-oc_glo_bgc-plankton_my_l4-multi-climatology-4km_P1D_202207"
        ):
            if start is None:
                start = "2016-01-01T00:08:13Z"

            if end is None:
                end = "2017-01-01T08:38:26Z"

        if layer == "cmems_obs-oc_glo_bgc-reflectance_my_l4-multi-4km_P1M_202207":
            if start is None:
                start = "1997-09-04T16:26:34Z"

            if end is None:
                end = "2023-07-01T02:35:59Z"

        if layer == "cmems_obs-oc_glo_bgc-transp_my_l4-multi-4km_P1M_202207":
            if start is None:
                start = "1997-09-04T16:26:34Z"

            if end is None:
                end = "2023-07-01T08:10:11Z"

        if layer == "cmems_obs-oc_glo_bgc-reflectance_my_l4-olci-300m_P1M_202211":
            if start is None:
                start = "2016-04-25T11:40:53Z"

            if end is None:
                end = "2023-07-01T08:06:14Z"

        if layer == "cmems_obs-oc_glo_bgc-reflectance_my_l4-olci-4km_P1M_202207":
            if start is None:
                start = "2016-04-25T11:34:53Z"

            if end is None:
                end = "2023-07-01T06:29:17Z"

        if layer == "cmems_obs-oc_glo_bgc-transp_my_l4-gapfree-multi-4km_P1D_202207":
            if start is None:
                start = "1997-09-04T16:26:34Z"

            if end is None:
                end = "2023-07-20T08:17:38Z"

        if layer == "cmems_obs-oc_glo_bgc-plankton_my_l4-gapfree-multi-4km_P1D_202207":
            if start is None:
                start = "1997-09-04T16:26:34Z"

            if end is None:
                end = "2023-07-20T08:17:38Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
