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
    "cmems_obs-ins_glo_phy-temp-sal_my_cora-oa_P1M_202211",  # Global ocean - coriolis observation re-analysis cora
]


class insitu_glo_phy_ts_oa_my(Main):
    name = "EO:MO:DAT:INSITU_GLO_PHY_TS_OA_MY_013_052"
    dataset = "EO:MO:DAT:INSITU_GLO_PHY_TS_OA_MY_013_052"

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
            "TEMP",
            "TEMP_ERR",
            "TEMP_PCTVAR",
            "depth",
            "latitude",
            "longitude",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer="cmems_obs-ins_glo_phy-temp-sal_my_cora-oa_P1M_202211",
        area=None,
        start=None,
        end=None,
        variables=None,
    ):
        if layer == "cmems_obs-ins_glo_phy-temp-sal_my_cora-oa_P1M_202211":
            if start is None:
                start = "1960-01-15T00:00:00Z"

            if end is None:
                end = "2022-06-15T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
