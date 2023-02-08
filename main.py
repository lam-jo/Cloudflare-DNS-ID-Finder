import json

import requests
raw_config_read = open("config.json", "r")
config = json.load(raw_config_read)
#CF_Token = input('Please input Cloudflare token: ')
#Zone_ID = input('Please input zone identifier: ')
#domain = input('Please input domain(SLD): ')
CF_Token = config["cf_token"]
Zone_ID = config["zone_id"]
domain = config["domain"]
cf_header = {"Authorization": "Bearer %s" % CF_Token}
cf_verify_url = 'https://api.cloudflare.com/client/v4/user/tokens/verify'
cf_token_verify_result = requests.get(cf_verify_url, headers=cf_header)
if cf_token_verify_result.status_code == 200:
    print('Cloudflare token valid')
else:
    print(cf_token_verify_result.content)
    quit()
cf_list_dns_url = 'https://api.cloudflare.com/client/v4/zones/%s/dns_records' % Zone_ID
cf_list_dns_param = {'name': domain}
dns_records_result = requests.get(cf_list_dns_url, headers=cf_header, params=cf_list_dns_param)
zone_list = json.loads(dns_records_result.text);
for i in zone_list['result']:
    print(i['name'], end=' ')
    print(i['id'])
#print(dns_records_result.text)
