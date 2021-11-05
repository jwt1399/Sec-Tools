#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from .Base import Base


class Scan(Base):
    def __init__(self, api_base_url, api_key):
        super().__init__(api_base_url, api_key)

        self.profile_dict = {
            'full_scan': '11111111-1111-1111-1111-111111111111',
            'high_risk_vuln': '11111111-1111-1111-1111-111111111112',
            'xss_vuln': '11111111-1111-1111-1111-111111111116',
            'sqli_vuln': '11111111-1111-1111-1111-111111111113',
            'weak_passwords': '11111111-1111-1111-1111-111111111115',
            'crawl_only': '11111111-1111-1111-1111-111111111117'
        }

        self.logger = self.get_logger

    def add(self, target_id, profile_key, report_template_id='', schedule=None, ui_session_id=''):
        """添加扫描任务

        Args:
            target_id (string): 目标ID
            profile_key (string): 扫秒类型
            schedule (None, optional): 扫秒时间，默认为即时扫描
            report_template_id (string, optional): 扫描报告模板ID
            ui_session_id (str, optional): Description

            schedule格式对照：
            1. 定时扫描，time senstive为False
            schedule = {disable: False, start_date: "20180816T000000+0700", time_sensitive: False}
            2. 定时扫描，time senstive为True
            schedule = {disable: False, start_date: "20180816T000000+0700", time_sensitive: True}
            3.周期扫描，每天
            schedule = {disable: false, recurrence: "DTSTART:20180815T170000Z FREQ=DAILY;INTERVAL=1", time_sensitive: false}
            4.周期扫描，每周
            schedule = {disable: false, recurrence: "DTSTART:20180815T170000Z FREQ=WEEKLY;INTERVAL=1", time_sensitive: false}
            5.周期扫描，每月
            schedule = {disable: false, recurrence: "DTSTART:20180815T170000Z FREQ=MONTHLY;INTERVAL=1", time_sensitive: false}
            6.周期扫描，每年
            schedule = {disable: false, recurrence: "DTSTART:20180815T170000Z FREQ=YEARLY;INTERVAL=1", time_sensitive: false}
            7.自定义
            修改FREQ和INTERVAL即可
            (1)无截止时间格式
            schedule = {disable: false, recurrence: "DTSTART:20180815T170000Z FREQ=YEARLY;INTERVAL=1", time_sensitive: false}
            (2)有截止时间
            schedule = {disable: false, recurrence: "DTSTART:20180815T170000Z FREQ=YEARLY;INTERVAL=1;UNTIL=20180830T170000Z", time_sensitive: false}
        """
        data = {
            'target_id': target_id,
            'profile_id': self.profile_dict.get(profile_key),
        }

        if report_template_id:
            data['report_template_id'] = self.report_template_dict.get(report_template_id)

        if not schedule:
            schedule = {
                'disable': False,
                'start_date': None,
                'time_sensitive': False
            }
        data['schedule'] = schedule
        try:
            response = requests.post(self.scan_api, json=data, headers=self.auth_headers, verify=False)
            # self.logger.error(data)
            status_code = 200
        except Exception:
            self.logger.error('Add Scan Failed......', exc_info=True)
            status_code = 404
        return status_code

    def delete(self, scan_id):
        scan_delete_api = f'{self.scan_api}/{scan_id}'
        try:
            response = requests.delete(scan_delete_api, headers=self.auth_headers, verify=False)
        except Exception:
            self.logger.error('Delete Scan Failed......', exc_info=True)

    def get_all(self):
        try:
            response = requests.get(self.scan_api, headers=self.auth_headers, verify=False)
            request_url = response.url
            scan_response = response.json().get('scans')
            scan_list = []
            for scan in scan_response:
                scan['request_url'] = request_url
                scan_list.append(scan)
        except Exception:
            scan_list = []
            self.logger.error('Get All Scan Failed......\n【ERROR】Please start your AWVS server，Otherwise vulnerability scanning will be disabled!!!\n', exc_info=False)  # awvs未启动时，报错信息关闭exc_info=False

        return scan_list

    def get(self, scan_id):
        scan_get_api = f'{self.scan_api}/{scan_id}'
        try:
            response = requests.get(scan_get_api, headers=self.auth_headers, verify=False)
            return response.json()
        except Exception:
            self.logger.error('Get Scan Failed......', exc_info=True)
            return None

    def get_vulns(self, scan_id, scan_session_id):
        scan_result_api = f'{self.scan_api}/{scan_id}/results/{scan_session_id}/vulnerabilities'
        try:
            response = requests.get(scan_result_api, headers=self.auth_headers, verify=False)
            vuln_list = response.json().get('vulnerabilities')
            return vuln_list
        except Exception:
            self.logger.error('Get Scan Result Failed......', exc_info=True)
            vuln_list = []
            return None

    def get_vuln_detail(self, scan_id, scan_session_id, vuln_id):
        scan_vuln_detail_api = f'{self.scan_api}/{scan_id}/results/{scan_session_id}/vulnerabilities/{vuln_id}'
        try:
            response = requests.get(scan_vuln_detail_api, headers=self.auth_headers, verify=False)
            vuln_detail = response.json()
            return vuln_detail
        except Exception:
            self.logger.error('Get Scan Result Failed......', exc_info=True)
            return None
