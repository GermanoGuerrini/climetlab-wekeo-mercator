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
    "cmems_obs-ins_glo_phy-cur_nrt_argo_irr_202211",  # cmems_obs-ins_glo_phy-cur_nrt_argo_irr_202211
    "cmems_obs-ins_glo_phy-cur_nrt_drifter_irr_202211",  # cmems_obs-ins_glo_phy-cur_nrt_drifter_irr_202211
    "cmems_obs-ins_glo_phy-cur_nrt_radar-radial_irr_202211",  # cmems_obs-ins_glo_phy-cur_nrt_radar-radial_irr_202211
    "cmems_obs-ins_glo_phy-cur_nrt_radar-total_irr_202211",  # cmems_obs-ins_glo_phy-cur_nrt_radar-total_irr_202211
]


class insitu_glo_phy_uv_discrete_nrt(Main):
    name = "EO:MO:DAT:INSITU_GLO_PHY_UV_DISCRETE_NRT_013_048"
    dataset = "EO:MO:DAT:INSITU_GLO_PHY_UV_DISCRETE_NRT_013_048"

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "CCOV",
            "CSPD_QC",
            "DDNS_QC",
            "DEPH",
            "DEPH_QC",
            "EWCS",
            "EWCT",
            "GDOP",
            "GDOP_QC",
            "LATITUDE",
            "LONGITUDE",
            "NARX",
            "NATX",
            "NSCS",
            "NSCT",
            "POSITION_QC",
            "QCflag",
            "SCDR",
            "SCDT",
            "SDN_CRUISE",
            "SDN_EDMO_CODE",
            "SDN_LOCAL_CDI_ID",
            "SDN_REFERENCES",
            "SDN_STATION",
            "SDN_XLINK",
            "SLNR",
            "SLNT",
            "SLTR",
            "SLTT",
            "TIME",
            "TIME_QC",
            "VART_QC",
            "crs",
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
        if layer == "cmems_obs-ins_glo_phy-cur_nrt_argo_irr_202211":
            if start is None:
                start = "1997-07-20T07:27:03Z"

            if end is None:
                end = "2023-06-22T08:28:05Z"

        if layer == "cmems_obs-ins_glo_phy-cur_nrt_drifter_irr_202211":
            if start is None:
                start = "1986-06-02T09:00:00Z"

            if end is None:
                end = "2023-06-25T12:00:00Z"

        if layer == "cmems_obs-ins_glo_phy-cur_nrt_radar-radial_irr_202211":
            if start is None:
                start = "2016-06-22T10:30:00Z"

            if end is None:
                end = "2023-06-27T21:45:00Z"

        if layer == "cmems_obs-ins_glo_phy-cur_nrt_radar-total_irr_202211":
            if start is None:
                start = "2012-03-20T00:45:00Z"

            if end is None:
                end = "2023-06-27T20:35:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
