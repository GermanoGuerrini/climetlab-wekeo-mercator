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
    "SST_MED_SST_L4_NRT_OBSERVATIONS_010_004_a_V2",  # Mediterranean sst analysis, l4, 1/16deg daily (sst med sst l4 NRT observations 010 004 a v2)
    "SST_MED_SSTA_L4_NRT_OBSERVATIONS_010_004_d",  # Mediterranean sst anomaly, l4, 1km daily (sst med ssta l4 NRT observations 010 004 d)
    "SST_MED_SST_L4_NRT_OBSERVATIONS_010_004_c_V2",  # Mediterranean sst analysis, l4, 1km daily (sst med sst l4 NRT observations 010 004 c v2)
    "SST_MED_SSTA_L4_NRT_OBSERVATIONS_010_004_b",  # Mediterranean sst anomaly, l4, 1/16deg daily (sst med ssta l4 NRT observations 010 004 b)
]


class sst_med_sst_l4_nrt_observations(Main):
    name = "EO:MO:DAT:SST_MED_SST_L4_NRT_OBSERVATIONS_010_004"
    dataset = "EO:MO:DAT:SST_MED_SST_L4_NRT_OBSERVATIONS_010_004"

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "lat",
            "lon",
            "sst_anomaly",
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
        if layer == "SST_MED_SST_L4_NRT_OBSERVATIONS_010_004_a_V2":
            if start is None:
                start = "2007-12-31T19:00:00Z"

            if end is None:
                end = "2023-07-10T07:00:00Z"

        if layer == "SST_MED_SSTA_L4_NRT_OBSERVATIONS_010_004_d":
            if start is None:
                start = "2007-12-31T00:00:00Z"

            if end is None:
                end = "2023-07-10T00:00:00Z"

        if layer == "SST_MED_SST_L4_NRT_OBSERVATIONS_010_004_c_V2":
            if start is None:
                start = "2007-12-31T19:00:00Z"

            if end is None:
                end = "2023-07-10T06:00:00Z"

        if layer == "SST_MED_SSTA_L4_NRT_OBSERVATIONS_010_004_b":
            if start is None:
                start = "2007-12-31T00:00:00Z"

            if end is None:
                end = "2023-07-10T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
