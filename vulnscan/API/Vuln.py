#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .Base import Base
import requests


class Vuln(Base):
    def __init__(self, api_base_url, api_key):
        super().__init__(api_base_url, api_key)

        self.logger = self.get_logger

    def get_all(self, status):
        vuln_get_all_api = f'{self.vuln_api}?q=status:{status}'
        try:
            response = requests.get(vuln_get_all_api, headers=self.auth_headers, verify=False)
            return response.json()
        except Exception:
            self.logger.error('Get All Vuln Failed......', exc_info=True)
            return None

    def get(self, vuln_id):
        vuln_get_api = f'{self.vuln_api}/{vuln_id}'
        try:
            response = requests.get(vuln_get_api, headers=self.auth_headers, verify=False)
            return response.json()
        except Exception:
            self.logger.error('Get Vuln Failed......', exc_info=True)
            return None

    def search(self, severity, criticality, status, cvss_score=0.0, target_id=None, group_id=None):
        """
        搜索漏洞
        :param severity: int
        :param criticality: int
        :param status: string
        :param cvss_score: logic expression
        :param target_id:
        :param group_id:
        :return:
        """

        # vuln_search_api = f'{self.vuln_api}?q=severity:{severity};criticality:{criticality};status:{status};cvss_score:{cvss_score};target_id:{target_id};group_id:{group_id}'
        vuln_search_api = f'{self.vuln_api}?q=status:{status};target_id:{target_id}'
        print(vuln_search_api)
        try:
            response = requests.get(vuln_search_api, headers=self.auth_headers, verify=False)
            # print(response.text)
            return response.text
        except Exception:
            self.logger.error('Search Vuln Failed......', exc_info=True)
            return None
