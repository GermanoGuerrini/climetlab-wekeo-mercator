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
    "osisaf_obs-si_glo_phy-siedge_nrt_sh-P1D_202107",  # Daily sea ice edge analysis from osi saf eumetsat
    "osisaf_obs-si_glo_phy-sitype_nrt_sh-P1D_202107",  # Daily sea ice type analysis from osi saf eumetsat
    "METNO-GLO-SEAICE_DRIFT-NORTH-L4-NRT-OBS",  # Arctic ice drift, l4 osisaf, 62km daily (metno-glo-seaice drift-north-l4-nrt-obs)
    "METNO-GLO-SEAICE_DRIFT-SOUTH-L4-NRT-OBS",  # Antarctic ice drift, l4 osisaf, 62km daily (metno-glo-seaice drift-south-l4-nrt-obs)
    "osisaf_obs-si_glo_phy-sitype_nrt_nh-P1D_202107",  # Daily sea ice type analysis from osi saf eumetsat
    "osisaf_obs-si_glo_phy-siedge_nrt_nh-P1D_202107",  # Daily sea ice edge analysis from osi saf eumetsat
]


class seaice_glo_seaice_l4_nrt_observations(Main):
    name = "EO:MO:DAT:SEAICE_GLO_SEAICE_L4_NRT_OBSERVATIONS_011_001"
    dataset = "EO:MO:DAT:SEAICE_GLO_SEAICE_L4_NRT_OBSERVATIONS_011_001"

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "Polar_Stereographic_Grid",
            "ice_edge",
            "lat",
            "lon",
            "orbit_num_amsr",
            "orbit_num_ascat",
            "orbit_num_ssmis",
            "param_used",
            "status_flag",
            "time",
            "time_bnds",
            "uncertainty",
            "xc",
            "yc",
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
        if layer == "osisaf_obs-si_glo_phy-siedge_nrt_sh-P1D_202107":
            if start is None:
                start = "2021-06-01T00:00:00Z"

            if end is None:
                end = "2023-07-10T00:00:00Z"

        if layer == "osisaf_obs-si_glo_phy-sitype_nrt_sh-P1D_202107":
            if start is None:
                start = "2021-06-01T00:00:00Z"

            if end is None:
                end = "2023-07-10T00:00:00Z"

        if layer == "METNO-GLO-SEAICE_DRIFT-NORTH-L4-NRT-OBS":
            if start is None:
                start = "2017-12-30T12:00:00Z"

            if end is None:
                end = "2023-07-09T12:00:00Z"

        if layer == "METNO-GLO-SEAICE_DRIFT-SOUTH-L4-NRT-OBS":
            if start is None:
                start = "2017-12-30T12:00:00Z"

            if end is None:
                end = "2023-07-09T12:00:00Z"

        if layer == "osisaf_obs-si_glo_phy-sitype_nrt_nh-P1D_202107":
            if start is None:
                start = "2021-06-01T00:00:00Z"

            if end is None:
                end = "2023-07-10T00:00:00Z"

        if layer == "osisaf_obs-si_glo_phy-siedge_nrt_nh-P1D_202107":
            if start is None:
                start = "2021-06-01T00:00:00Z"

            if end is None:
                end = "2023-07-10T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
