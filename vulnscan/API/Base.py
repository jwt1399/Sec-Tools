#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logging.config import fileConfig
import requests
import logging
from os import path
# import requests.packages.urllib3
# from os.path import dirname, join
# from Sec_Tools.settings import API_KEY, API_URL
# API_URL = 'https://127.0.0.1:3443'
# API_KEY = '1986ad8c0a5b3df4d7028d5f3c06e936c61f48e0cd8c4462cb03d6a2f7c03deb4'

class Base(object):
    def __init__(self, api_base_url, api_key):
        self.api_base_url = api_base_url
        self._api_key = api_key

        api_base_url = api_base_url.strip('/')
        self.targets_api = f'{api_base_url}/api/v1/targets'
        self.scan_api = f'{api_base_url}/api/v1/scans'
        self.vuln_api = f'{api_base_url}/api/v1/vulnerabilities'
        self.report_api = f'{api_base_url}/api/v1/reports'
        self.create_group_api = f'{api_base_url}/api/v1/target_groups'

        self.report_template_dict = {
            'affected_items': '11111111-1111-1111-1111-111111111115',
            'cwe_2011': '11111111-1111-1111-1111-111111111116',
            'developer': '11111111-1111-1111-1111-111111111111',
            'executive_summary': '11111111-1111-1111-1111-111111111113',
            'hipaa': '11111111-1111-1111-1111-111111111114',
            'iso_27001': '11111111-1111-1111-1111-111111111117',
            'nist_SP800_53': '11111111-1111-1111-1111-111111111118',
            'owasp_top_10_2013': '11111111-1111-1111-1111-111111111119',
            'pci_dss_3.2': '11111111-1111-1111-1111-111111111120',
            'quick': '11111111-1111-1111-1111-111111111112',
            'sarbanes_oxley': '11111111-1111-1111-1111-111111111121',
            'scan_comparison': '11111111-1111-1111-1111-111111111124',
            'stig_disa': '11111111-1111-1111-1111-111111111122',
            'wasc_threat_classification': '11111111-1111-1111-1111-111111111123'
        }

        # 禁用https证书相关警告
        requests.packages.urllib3.disable_warnings()

    @property
    def auth_headers(self):
        auth_headers = {
            'X-Auth': self._api_key,
            'content-type': 'application/json'
        }
        return auth_headers

    @property
    def get_logger(self):
        logging_config = path.join(path.dirname(path.abspath(__file__)), '../config/logging.ini')
        logging.config.fileConfig(logging_config)
        return logging.getLogger('awvs')
