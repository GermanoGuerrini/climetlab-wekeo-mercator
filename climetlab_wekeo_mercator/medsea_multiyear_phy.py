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
    "med-cmcc-cur-rean-m_202012",  # Horizontal velocity (3d) - monthly mean
    "med-cmcc-ssh-rean-h_202012",  # Sea surface height (2d) - hourly mean
    "med-cmcc-cur-rean-d_202012",  # Horizontal velocity (3d) - daily mean
    "cmems_mod_med_phy-tem_my_4.2km_P1Y-m_202211",  # Potential temperature (3d) - yearly mean
    "cmems_mod_med_phy-cur_my_4.2km_P1Y-m_202211",  # Horizontal velocity (3d) - yearly mean
    "med-cmcc-tem-int-m_202112",  # Potential temperature (3d) - monthly mean
    "cmems_mod_med_phy-ssh_my_4.2km_P1Y-m_202211",  # Sea surface height (2d) - yearly mean
    "med-cmcc-sal-rean-m_202012",  # Salinity (3d) - monthly mean
    "med-cmcc-mld-rean-d_202012",  # Mixed layer depth (2d) - daily mean
    "med-cmcc-mld-rean-m_202012",  # Mixed layer depth (2d) - monthly mean
    "med-cmcc-cur-rean-h_202012",  # Horizontal surface velocity (2d) - hourly mean
    "med-cmcc-ssh-rean-m_202012",  # Sea surface height (2d) - monthly mean
    "med-cmcc-cur-int-m_202112",  # Horizontal velocity (3d) - monthly mean
    "med-cmcc-mld-int-m_202112",  # Mixed layer depth (2d) - monthly mean
    "med-cmcc-sal-int-m_202112",  # Salinity (3d) - monthly mean
    "cmems_mod_med_phy-mld_my_4.2km_P1Y-m_202211",  # Mixed layer depth (2d) - yearly mean
    "cmems_mod_med_phy-sal_my_4.2km_P1Y-m_202211",  # Salinity (3d) - yearly
    "med-cmcc-ssh-rean-d_202012",  # Sea surface height (2d) - daily mean
    "med-cmcc-sal-rean-d_202012",  # Salinity (3d) - daily mean
    "med-cmcc-tem-rean-d_202012",  # Potential temperature (3d) - daily mean
    "cmems_mod_med_phy_my_4.2km-climatology_P1M-m_202211",  # cmems_mod_med_phy_my_4.2km-climatology_P1M-m_202211
    "med-cmcc-ssh-int-m_202112",  # Sea surface height (2d) - monthly mean
    "med-cmcc-tem-rean-m_202012",  # Potential temperature (3d) - monthly mean
]


class medsea_multiyear_phy(Main):
    name = "EO:MO:DAT:MEDSEA_MULTIYEAR_PHY_006_004"
    dataset = "EO:MO:DAT:MEDSEA_MULTIYEAR_PHY_006_004"

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "bottomT",
            "depth",
            "lat",
            "lon",
            "thetao",
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
        if layer == "med-cmcc-cur-rean-m_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-ssh-rean-h_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-cur-rean-d_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "cmems_mod_med_phy-tem_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "cmems_mod_med_phy-cur_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-tem-int-m_202112":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "cmems_mod_med_phy-ssh_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-sal-rean-m_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-mld-rean-d_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-mld-rean-m_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-cur-rean-h_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-ssh-rean-m_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-cur-int-m_202112":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-mld-int-m_202112":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-sal-int-m_202112":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "cmems_mod_med_phy-mld_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "cmems_mod_med_phy-sal_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-ssh-rean-d_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-sal-rean-d_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-tem-rean-d_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "cmems_mod_med_phy_my_4.2km-climatology_P1M-m_202211":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-ssh-int-m_202112":
            if start is None:
                start = "2022-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        if layer == "med-cmcc-tem-rean-m_202012":
            if start is None:
                start = "2020-09-01T00:00:00Z"

            if end is None:
                end = "2022-09-01T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
