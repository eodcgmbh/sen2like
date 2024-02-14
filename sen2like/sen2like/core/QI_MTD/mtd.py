#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2023 ESA.
#
# This file is part of sen2like.
# See https://github.com/senbox-org/sen2like for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import datetime


class Metadata:
    def __init__(self):
        self.mtd = {}
        self.qi = {}
        self.hardcoded_values = {}
        self.clear()

    def clear(self):
        self.mtd = {
            "bands_path_H": [],
            "bands_path_F": [],
            "product_H_name": "NONE",
            "product_F_name": "NONE",
            "granule_H_name": "NONE",
            "granule_F_name": "NONE",
            "band_rootName_H": "NONE",
            "band_rootName_F": "NONE",
            "generation_time": datetime.datetime(1, 1, 1, 1, 1, 1),
            "masks_H": [],
            "masks_F": [],
            "quicklooks_H": [],
            "quicklooks_F": [],
            "ang_filename": "NONE",
            "qi_path": "NONE",
            "pvi_filename": "NONE",
            "S2_AC": 'ZZZ'
        }

        # self.qi is a dict with the 'Value' nodes from the QI report. key=node_name, item=node_text
        self.qi = {
            "COREGISTRATION_BEFORE_CORRECTION": "NONE",
            "INPUT_RMSE_X": "NONE",
            "INPUT_RMSE_Y": "NONE",
            "SKEW": "NONE",
            "KURTOSIS": "NONE",
            "REF_IMAGE": "NONE",
            "MEAN": "NONE",
            'MEAN_X': "NONE",
            'MEAN_Y': "NONE",
            "STD": "NONE",
            'STD_X': "NONE",
            'STD_Y': "NONE",
            "RMSE": "NONE",
            "NB_OF_POINTS": "NONE",
            "MEAN_DELTA_AZIMUTH": "NONE",
            "CONSTANT_SOLAR_ZENITH_ANGLE": "NONE",
            "BRDF_METHOD": "NONE",
        }

        self.hardcoded_values = {
            "s2_struct_xml": "xml_backbones/S2_folder_backbone.xml",
            "bb_QIH_path": "xml_backbones/L2H_QUALITY_backbone.xml",
            "bb_QIF_path": "xml_backbones/L2F_QUALITY_backbone.xml",
            "product_mtd_xsd": "xsd_files/S2-PDGS-TAS-DI-PSD-V14.5_Schema/S2_User_Product_Level-2A_Metadata.xsd",
            "product_tl_xsd": "xsd_files/S2-PDGS-TAS-DI-PSD-V14.5_Schema/S2_PDI_Level-2A_Tile_Metadata.xsd",
            "product_QIH_xsd": "xsd_files/L2H_QUALITY.xsd",
            "product_QIF_xsd": "xsd_files/L2F_QUALITY.xsd",
            "PDGS": "9999",
            "L8_archiving_center": "ZZZ_",
            "L8_archiving_time": "0000-00-00T00:00:00.000Z"
        }

    def update(self, new_medatada):
        """Merge a metadata content with current metadata

        :param new_medatada: Metadata to merge
        """
        self.qi.update(new_medatada.qi)

        for key, val in new_medatada.mtd.items():
            if isinstance(val, list):
                self.mtd[key].extend(val)
            elif isinstance(val, dict):
                self.mtd[key].update(val)
            else:
                self.mtd[key] = val
