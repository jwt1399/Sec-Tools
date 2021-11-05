# -*- coding:utf-8 -*-

import re
import requests
import chardet
from ..randheader.randheader import get_ua


# 用于匹配waf的规则
# 格式： waf名|匹配对象|匹配属性|匹配规则
# 360|headers|Server|XXX
WAF_RULE = (
    'WAF|headers|Server|WAF',
    '360|headers|X-Powered-By-360wzb|wangzhan\.360\.cn',
    '360|headers|X-Powered-By|360',
    '360wzws|headers|Server|360wzws',
    'Anquanbao|headers|X-Powered-By-Anquanbao|MISS',
    'Armor|headers|Server|armor',
    'BaiduYunjiasu|headers|Server|yunjiasu-nginx',
    'BinarySEC|headers|x-binarysec-cache|miss',
    'BinarySEC|headers|x-binarysec-via|binarysec\.com',
    'BinarySEC|headers|Server|BinarySec',
    'BlockDoS|headers|Server|BlockDos\.net',
    'CloudFlare CDN|headers|Server|cloudflare-nginx',
    'CloudFlare CDN|headers|Server|cloudflare',
    'cloudflare CDN|headers|CF-RAY|.+',
    'Cloudfront CDN|headers|Server|cloudfront',
    'Cloudfront CDN|headers|X-Cache|cloudfront',
    'Cloudfront CDN|headers|X-Cache|Error\sfrom\scloudfront',
    'mod_security|headers|Server|mod_security',
    'Barracuda NG|headers|Server|Barracuda',
    'mod_security|headers|Server|Mod_Security',
    'F5 BIG-IP APM|headers|Server|BigIP',
    'F5 BIG-IP APM|headers|Server|BIG-IP',
    'F5 BIG-IP ASM|headers|X-WA-Info|.+',
    'F5 BIG-IP ASM|headers|X-Cnection|close',
    'F5-TrafficShield|headers|Server|F5-TrafficShield',
    'GoDaddy|headers|X-Powered-By|GoDaddy',
    'Bluedon IST|headers|Server|BDWAF',
    'Comodo|headers|Server|Protected by COMODO',
    'Airee CDN|headers|Server|Airee',
    'Beluga CDN|headers|Server|Beluga',
    'Fastly CDN|headers|X-Fastly-Request-ID|\w+',
    'limelight CDN|headers|Set-Cookie|limelight',
    'CacheFly CDN|headers|BestCDN|CacheFly',
    'maxcdn CDN|headers|X-CDN|maxcdn',
    'DenyAll|headers|Set-Cookie|\Asessioncookie=',
    'AdNovum|headers|Set-Cookie|^Navajo.*?$',
    'dotDefender|headers|X-dotDefender-denied|1',
    'Incapsula CDN|headers|X-CDN|Incapsula',
    'Jiasule|headers|Set-Cookie|jsluid=',
    'KONA|headers|Server|AkamaiGHost',
    'ModSecurity|headers|Server|NYOB',
    'ModSecurity|headers|Server|NOYB',
    'ModSecurity|headers|Server|.*mod_security',
    'NetContinuum|headers|Cneonction|\Aclose',
    'NetContinuum|headers|nnCoection|\Aclose',
    'NetContinuum|headers|Set-Cookie|citrix_ns_id',
    'Newdefend|headers|Server|newdefend',
    'NSFOCUS|headers|Server|NSFocus',
    'Safe3|headers|X-Powered-By|Safe3WAF',
    'Safe3|headers|Server|Safe3 Web Firewall',
    'Safedog|headers|X-Powered-By|WAF/2\.0',
    'Safedog|headers|Server|Safedog',
    'Safedog|headers|Set-Cookie|Safedog',
    'SonicWALL|headers|Server|SonicWALL',
    'ZenEdge Firewall|headers|Server|ZENEDGE',
    'WatchGuard|headers|Server|WatchGuard',
    'Stingray|headers|Set-Cookie|\AX-Mapping-',
    'Art of Defence HyperGuard|headers|Set-Cookie|WODSESSION=',
    'Sucuri|headers|Server|Sucuri/Cloudproxy',
    'Usp-Sec|headers|Server|Secure Entry Server',
    'Varnish|headers|X-Varnish|.+',
    'Varnish|headers|Server|varnish',
    'Wallarm|headers|Server|nginx-wallarm',
    'WebKnight|headers|Server|WebKnight',
    'Yundun|headers|Server|YUNDUN',
    'Teros WAF|headers|Set-Cookie|st8id=',
    'Imperva SecureSphere|headers|X-Iinfo|.+',
    'NetContinuum WAF|headers|Set-Cookie|NCI__SessionId=',
    'Yundun|headers|X-Cache|YUNDUN',
    'Yunsuo|headers|Set-Cookie|yunsuo',
    'Immunify360|headers|Server|imunify360',
    'ISAServer|headers|Via|.+ISASERVER',
    'Qiniu CDN|headers|X-Qiniu-Zone|0',
    'azion CDN|headers|Server|azion',
    'HyperGuard Firewall|headers|Set-cookie|ODSESSION=',
    'ArvanCloud|headers|Server|ArvanCloud',
    'GreyWizard Firewall|headers|Server|greywizard.*',
    'FortiWeb Firewall|headers|Set-Cookie|cookiesession1',
    'Beluga CDN|headers|Server|Beluga',
    'DoSArrest Internet Security|headers|X-DIS-Request-ID|.+',
    'ChinaCache CDN|headers|Powered-By-ChinaCache|\w+',
    'ChinaCache CDN|headers|Server|ChinaCache',
    'HuaweiCloudWAF|headers|Server|HuaweiCloudWAF',
    'HuaweiCloudWAF|headers|Set-Cookie|HWWAFSESID',
    'KeyCDN|headers|Server|KeyCDN',
    'Reblaze Firewall|headers|Set-cookie|rbzid=\w+',
    'Distil Firewall|headers|X-Distil-CS|.+',
    'SDWAF|headers|X-Powered-By|SDWAF',
    'NGENIX CDN|headers|X-NGENIX-Cache|HIT',
    'FortiWeb|headers|Server|FortiWeb.*',
    'Naxsi|headers|X-Data-Origin|naxsi-waf',
    'IBM DataPower|headers|X-Backside-Transport|\w+',
    'Cisco ACE XML Gateway|headers|Server|ACE\sXML\sGateway',
    'AWS WAF|headers|Server|awselb.*',
    'PowerCDN|headers|Server|PowerCDN',
    'Profense|headers|Server|profense',
    'CompState|headers|X-SL-CompState|.+',
    'West263CDN|headers|X-Cache|.+WT263CDN-.+',
    'DenyALL WAF|content|content|Condition Intercepted',
    'yunsuo|content|content|<img class="yunsuologo"',
    'aesecure|content|content|aesecure_denied.png',
    'aliyun|content|content|errors.aliyun.com',
    'aliyun|headers|Set-Cookie|aliyungf_tc=',
    'Palo Alto Firewall|content|content|has been blocked in accordance with company policy',
    'PerimeterX Firewall|content|content|https://www.perimeterx.com/whywasiblocked',
    'Neusoft SEnginx|content|content|SENGINX-ROBOT-MITIGATION',
    'SiteLock TrueShield|content|content|sitelock-site-verification',
    'SonicWall|content|content|nsa_banner',
    'SonicWall|content|content|Web Site Blocked',
    'Sophos UTM Firewall|content|content|Powered by UTM Web Protection',
    'Unknown FireWall|content|content|firewall',
    '知道创宇云安全WAF|content|content|知道创宇云安全'
)


def checkwaf(headers, content):
    """
    判断是否使用的waf
    :param headers: request返回包res.headeres
    :param content: request返回包res.text[:10000]
    :return: WAF名字/不存在waf
    """
    for rule in WAF_RULE:
        name, method, position, regex = rule.split('|')
        if method == 'headers':
            if headers.get(position) is not None:
                if re.search(regex, str(headers.get(position)), re.I) is not None:
                    return '存在' + name
        else:
            if re.search(regex, str(content), re.I | re.M):
                return '存在' + name
    return '不存在WAF'


def getwaf(url=''):
    result_str = 'URL错误'
    if url.startswith('https://') or url.startswith('http://'):
        # 使用payload让目标站点爆出防火墙信息
        payload = r'/?id=1%27&d=2"&y=3%27or%27select%20*%20from%20users%20limit%200,1&b=<script>alert(1)</script>&o=eval&yy=%0a%0d'
        if url:
            try:
                res = requests.get(url+payload, headers=get_ua(), timeout=4)
                codetype = chardet.detect(res.content).get('encoding')
                res.encoding = codetype
                result_str = checkwaf(res.headers, res.text)
                if res.status_code == 403 and result_str == '不存在WAF':
                    return "存在WAF"
            except Exception as e:
                result_str = '目标站点不可访问'
    return result_str


if __name__ == '__main__':
    print("name:", getwaf('https://jwt1399.top'))
