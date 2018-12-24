import requests
import json


url = 'http://192.168.1.11/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
###################################################
# data = {
#     "jsonrpc": "2.0",
#     "method": "apiinfo.version",
#     "params": [],
#     "id": 1
# }
###################################################
#
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "123456"
#     },
#     "id": 1
# }
# # result: 54f3bc14f30498e90dd9873b74d0f5d0  # 返回值,验证并返回有关用户的其他信息。
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         # "user": "Admin",
#         # "password": "zabbix"
#     },
#     "auth": "54f3bc14f30498e90dd9873b74d0f5d0",
#     "id": 1
# }

# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#                 "Template OS Windows"
#             ]
#         }
#     },
#     "auth": "54f3bc14f30498e90dd9873b74d0f5d0",
#     "id": 1
# }

data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "Web server",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.254",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "1"
            }
        ],
        "templates": [
            {
                "templateid": "20045"
            }
        ],
        "inventory_mode": 0,
        "inventory": {
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },
    "auth": "038e1d7b1735c6a5436ee9eae095879e",
    "id": 1
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
