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
    "MetO-NWS-PHY-hi-SSS_202012",  # Hourly-instantaneous surface salinity (2d)
    "MetO-NWS-PHY-qh-SSH_202012",  # 15minute-instantaneous ssh (2d)
    "MetO-NWS-PHY-hi-MLD_202012",  # Hourly-instantaneous mixed layer depth (2d)
    "MetO-NWS-PHY-dm-BED_202012",  # Daily-mean seabed temperature (2d)
    "MetO-NWS-PHY-hi-SST_202012",  # Hourly-instantaneous surface temperature (2d)
    "MetO-NWS-PHY-hi-CUR_202012",  # Hourly-instantaneous horizontal velocity (3d)
    "MetO-NWS-PHY-hi-SSC_202012",  # Hourly-instantaneous horizontal velocity (2d)
    "MetO-NWS-PHY-dm-MLD_202012",  # Daily-mean mixed layer depth (2d)
    "MetO-NWS-PHY-hi-TEM_202012",  # Hourly-instantaneous potential temperature (3d)
    "MetO-NWS-PHY-hi-SAL_202012",  # Hourly-instantaneous salinity (3d)
    "MetO-NWS-PHY-dm-TEM_202012",  # Daily-mean potential temperature (3d)
    "MetO-NWS-PHY-hi-BED_202012",  # Hourly-instantaneous seabed temperature (2d)
    "MetO-NWS-PHY-qh-SSC_202012",  # 15minute-instantaneous horizontal velocity (2d)
    "MetO-NWS-PHY-hi-SSH_202012",  # Hourly-instantaneous ssh (2d)
    "MetO-NWS-PHY-dm-SAL_202012",  # Daily-mean salinity (3d)
    "MetO-NWS-PHY-dm-CUR_202012",  # Daily-mean horizontal velocity (3d)
]


class northwestshelf_analysis_forecast_phy(Main):
    name = "EO:MO:DAT:NORTHWESTSHELF_ANALYSIS_FORECAST_PHY_004_013"
    dataset = "EO:MO:DAT:NORTHWESTSHELF_ANALYSIS_FORECAST_PHY_004_013"

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "depth",
            "lat",
            "lon",
            "time",
            "uo",
            "vo",
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
        if layer == "MetO-NWS-PHY-hi-SSS_202012":
            if start is None:
                start = "2019-01-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "MetO-NWS-PHY-qh-SSH_202012":
            if start is None:
                start = "2019-07-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "MetO-NWS-PHY-hi-MLD_202012":
            if start is None:
                start = "2019-07-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "MetO-NWS-PHY-dm-BED_202012":
            if start is None:
                start = "2019-01-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "MetO-NWS-PHY-hi-SST_202012":
            if start is None:
                start = "2019-01-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "MetO-NWS-PHY-hi-CUR_202012":
            if start is None:
                start = "2019-01-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "MetO-NWS-PHY-hi-SSC_202012":
            if start is None:
                start = "2019-01-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "MetO-NWS-PHY-dm-MLD_202012":
            if start is None:
                start = "2019-01-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "MetO-NWS-PHY-hi-TEM_202012":
            if start is None:
                start = "2019-01-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "MetO-NWS-PHY-hi-SAL_202012":
            if start is None:
                start = "2019-01-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "MetO-NWS-PHY-dm-TEM_202012":
            if start is None:
                start = "2019-01-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "MetO-NWS-PHY-hi-BED_202012":
            if start is None:
                start = "2019-01-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "MetO-NWS-PHY-qh-SSC_202012":
            if start is None:
                start = "2019-07-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "MetO-NWS-PHY-hi-SSH_202012":
            if start is None:
                start = "2019-01-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "MetO-NWS-PHY-dm-SAL_202012":
            if start is None:
                start = "2019-01-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        if layer == "MetO-NWS-PHY-dm-CUR_202012":
            if start is None:
                start = "2019-01-03T00:00:00Z"

            if end is None:
                end = "2023-07-15T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
