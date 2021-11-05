#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import requests.packages.urllib3
from .Base import Base


class Target(Base):
    def __init__(self, api_base_url, api_key):
        super().__init__(api_base_url, api_key)

        self.logger = self.get_logger


    def get_all(self):
        try:
            response = requests.get(self.targets_api, headers=self.auth_headers, verify=False)
            result = response.json()
            target_list = result.get('targets')
            return target_list
        except Exception:
            self.logger.error('Get Targets Failed......', exc_info=True)
            return None

    # https://10.0.0.22:3443/api/v1/targets?q=threat:2;text_search:*pc

    def search(self, threat=None, criticality=None, group_id=None, keyword=None):
        """
        搜索任务
        :param threat: 威胁等级;高->低:[3,2,1,0]
        :param criticality: 危险程度;高->低:[30,20,10,0]
        :param group_id: 分组id
        :param keyword: 筛选内容，支持通配符，*baidu.com
        :return:
        """
        search_targets_api = f'{self.targets_api}?q=threat:{threat};criticality:{criticality};group_id:{group_id};text_search:{keyword}'
        try:
            response = requests.get(search_targets_api, headers=self.auth_headers, verify=False)
            result = response.json()
            target_list = result.get('targets')
            return target_list
        except Exception:
            self.logger.error('Search Target Failed......', exc_info=True)
            return None

    def add(self, address, description=None):
        if not description:
            description = f'{address} 站点测试'
        data = {
            'address': address,
            'description': description,
        }
        try:
            response = requests.post(self.targets_api, headers=self.auth_headers, json=data, verify=False)
            result = response.json()
            target_id = result.get('target_id')
            return target_id

        except Exception:
            self.logger.error('Add Target Failed......', exc_info=True)
            return None

    def delete(self, target_id):
        delete_targets_api = f'{self.targets_api}/{target_id}'
        try:
            response = requests.delete(delete_targets_api, headers=self.auth_headers, verify=False)
            if response.status_code == 200:
                return True
            else:
                self.logger.error(f'Delete Target Failed......\n{response.text}')
                return False
        except Exception:
            self.logger.error('Delete Target Failed......', exc_info=True)
