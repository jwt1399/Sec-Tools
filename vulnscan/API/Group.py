#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .Base import Base
import requests

class Group(Base):
    def __init__(self, api_base_url, api_key):
        super().__init__(api_base_url, api_key)
        self.logger = self.get_logger

    def create_new_group(self, group_name, description = None):
        if not description:
            description = f'{group_name} group'
        
        data = {'name': group_name, 'description':description}
        response = requests.post(self.create_group_api, json=data, headers=self.auth_headers, verify=False)
        if response.status_code != 201:
            self.logger.error("创建分组失败~！", exc_info=True)
            return False
        else: 
            group_id = response.headers['Location'].split('/')[-1]
            # group_id格式如下图所示
            #8b78443f-8bcd-4408-a8fd-0692868e265b
            group_id = '{0}-{1}-{2}-{3}-{4}'.format(group_id[0:8], group_id[8:12], group_id[12:16], group_id[16:20], group_id[20:len(group_id)])
            return group_id
    
    def get_existed_groups(self):
        groups = {}
        response = requests.get(self.create_group_api, headers=self.auth_headers, verify=False)
        print(response.status_code)
        if response.status_code != 200:
            self.logger.error("查询已存在组失败~", exc_info=True)
        else:
            response_j = response.json()
            groups_list = response_j.get('groups')
            for group in groups_list:
                groups[group.get('name')] = group.get('group_id')
        return groups


    def add_to_group(self, target_id, group_id):
        add_to_group_api = self.create_group_api + '/{0}/targets'.format(group_id)
        # print(add_to_group_api)
        data = {'add':[target_id],'remove':[]}
        # print(data)
        response = requests.patch(add_to_group_api, json=data, headers=self.auth_headers, verify=False)
        if response.status_code != 206:
            self.logger.error("添加失败~！", exc_info=True)
            return False
        else:
            print(response.headers)
            return True
    
    def remove_from_group(self, target_id, group_id):
        add_to_group_api = self.create_group_api + '/{0}/targets'.format(group_id)
        print(add_to_group_api)
        data = {'add':[],'remove':[target_id]}
        print(data)
        response = requests.patch(add_to_group_api, json=data, headers=self.auth_headers, verify=False)
        if response.status_code != 206:
            self.logger.error("删除失败~！", exc_info=True)
            return False
        else:
            print(response.headers)
            return True
