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
    "cmems_mod_blk_bgc-car_anfc_3km_P1D-m_202211",  # Dissolved inorganic carbon, alkalinity, ph (3d) - daily mean
    "cmems_mod_blk_bgc-pft_anfc_3km_P1M-m_202211",  # Phytoplankton carbon biomass and chlorophyll (3d) - monthly mean
    "cmems_mod_blk_bgc-pft_anfc_3km_P1D-m_202211",  # Phytoplankton carbon biomass and chlorophyll (3d) - daily mean
    "cmems_mod_blk_bgc-nut_anfc_3km_P1M-m_202211",  # Nitrate and phosphate (3d) - monthly mean
    "cmems_mod_blk_bgc-bio_anfc_3km_P1D-m_202211",  # Net primary production, dissolved oxygen (3d), bottom dissolved oxygen (2d) - daily mean
    "cmems_mod_blk_bgc-opt_anfc_3km_P1M-m_202211",  # Photosynthetical-active radiation and attenuation coefficient (3d) - monthly mean
    "cmems_mod_blk_bgc-co2_anfc_3km_P1M-m_202211",  # Surface partial pressure of co2 and surface co2 flux (2d) - monthly mean
    "cmems_mod_blk_bgc-bio_anfc_3km_P1M-m_202211",  # Net primary production, dissolved oxygen (3d), bottom dissolved oxygen (2d) - monthly mean
    "cmems_mod_blk_bgc-co2_anfc_3km_PT1H-m_202211",  # Surface partial pressure of co2 and surface co2 flux (2d) - hourly mean
    "cmems_mod_blk_bgc-co2_anfc_3km_P1D-m_202211",  # Surface partial pressure of co2 and surface co2 flux (2d) - daily mean
    "cmems_mod_blk_bgc-car_anfc_3km_P1M-m_202211",  # Dissolved inorganic carbon, alkalinity, ph (3d) - monthly mean
    "cmems_mod_blk_bgc-nut_anfc_3km_P1D-m_202211",  # Nitrate and phosphate (3d) - daily mean
    "cmems_mod_blk_bgc-opt_anfc_3km_P1D-m_202211",  # Photosynthetical-active radiation and attenuation coefficient (3d) - daily mean
]


class blksea_analysisforecast_bgc(Main):
    name = "EO:MO:DAT:BLKSEA_ANALYSISFORECAST_BGC_007_010"
    dataset = "EO:MO:DAT:BLKSEA_ANALYSISFORECAST_BGC_007_010"

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "depth",
            "kd",
            "latitude",
            "lght",
            "longitude",
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
        if layer == "cmems_mod_blk_bgc-car_anfc_3km_P1D-m_202211":
            if start is None:
                start = "2022-11-10T00:00:00Z"

            if end is None:
                end = "2023-07-10T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-pft_anfc_3km_P1M-m_202211":
            if start is None:
                start = "2022-11-13T00:00:00Z"

            if end is None:
                end = "2023-06-13T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-pft_anfc_3km_P1D-m_202211":
            if start is None:
                start = "2022-11-10T00:00:00Z"

            if end is None:
                end = "2023-07-10T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-nut_anfc_3km_P1M-m_202211":
            if start is None:
                start = "2022-11-13T00:00:00Z"

            if end is None:
                end = "2023-06-13T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-bio_anfc_3km_P1D-m_202211":
            if start is None:
                start = "2022-11-10T00:00:00Z"

            if end is None:
                end = "2023-07-10T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-opt_anfc_3km_P1M-m_202211":
            if start is None:
                start = "2022-11-13T00:00:00Z"

            if end is None:
                end = "2023-06-13T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-co2_anfc_3km_P1M-m_202211":
            if start is None:
                start = "2022-11-13T00:00:00Z"

            if end is None:
                end = "2023-06-13T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-bio_anfc_3km_P1M-m_202211":
            if start is None:
                start = "2022-11-13T00:00:00Z"

            if end is None:
                end = "2023-06-13T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-co2_anfc_3km_PT1H-m_202211":
            if start is None:
                start = "2022-11-13T00:00:00Z"

            if end is None:
                end = "2023-07-10T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-co2_anfc_3km_P1D-m_202211":
            if start is None:
                start = "2022-11-10T00:00:00Z"

            if end is None:
                end = "2023-07-10T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-car_anfc_3km_P1M-m_202211":
            if start is None:
                start = "2022-11-13T00:00:00Z"

            if end is None:
                end = "2023-06-13T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-nut_anfc_3km_P1D-m_202211":
            if start is None:
                start = "2022-11-10T00:00:00Z"

            if end is None:
                end = "2023-07-10T00:00:00Z"

        if layer == "cmems_mod_blk_bgc-opt_anfc_3km_P1D-m_202211":
            if start is None:
                start = "2022-11-10T00:00:00Z"

            if end is None:
                end = "2023-07-10T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
