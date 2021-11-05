#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .Base import Base
import requests

class Report(Base):
    def __init__(self, api_base_url, api_key):
        super().__init__(api_base_url, api_key)
        self.logger = self.get_logger

    def get_all(self):
        try:
            response = requests.get(self.report_api, headers=self.auth_headers, verify=False)
            return response.json()
        except Exception:
            self.logger.error('Get All Reports Failed......', exc_info=True)
            return None

    def generate(self, template_id, list_type, id_list):
        data = {
            'template_id': self.report_template_dict.get(template_id),
            'source': {
                'list_type': list_type,
                'id_list': id_list
            }
        }
        try:
            response = requests.post(self.report_api, json=data, headers=self.auth_headers, verify=False)
            return True
        except Exception:
            self.logger.error('Generate Report Failed......', exc_info=True)
            return False
