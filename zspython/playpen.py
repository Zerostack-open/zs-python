import __future__
import os
import requests
import json
import re
import pprint

auth_username = os.getenv('OS_USERNAME',None)
auth_password = os.getenv('OS_PASSWORD',None)
auth_url = os.getenv('OS_AUTH_URL',None)
project_name = os.getenv('OS_PROJECT_NAME',None)
user_domain_name = os.getenv('OS_USER_DOMAIN_NAME',None)
project_domain_name=os.getenv('OS_PROJECT_DOMAIN_NAME',None)
cacert=os.getenv('OS_CACERT',None)

user_region = 'uswe'

if(auth_username == None or auth_password == None or auth_url == None or \
   project_name == None or user_region == None or user_domain_name == None or \
   project_domain_name == None or cacert == None):
    print "Export the Zerostack RC file, or explicitly define authentication variables"

token_scope = 'domain'

body = None

if(token_scope == 'project'):
    body = '{"auth":{"identity":{"methods":["password"],"password":{"user":{"name":"%s","domain":{"name":"%s"},"password":"%s"}}},"scope":{"project":{"name":"%s","domain":{"name":"%s"}}}}}' \
            %(auth_username,project_domain_name,auth_password,project_name,project_domain_name)
else:
    body = '{"auth":{"identity":{"methods":["password"],"password":{"user":{"domain":{"name":"%s"},"name":"%s","password":"%s"}}},"scope":{"domain":{"name":"%s"}}}}' \
           %(project_domain_name,auth_username,auth_password,project_domain_name)

headers={"content-type":"application/json"}

#raw_token_body = self.rest.run_rest({'body':body,'headers':headers,'verify':True,'url':self.auth_url+'/auth/tokens','verb':'POST'})
token_url = auth_url+'/auth/tokens'
trequest = requests.post(token_url,verify = False,data = body,headers={"content-type":"application/json"})
jtoken = json.loads(trequest.text)
pprint.pprint(jtoken)
token = trequest.headers.get('X-Subject-Token')
#print jtoken

#operation to test
#account_dict = '{"domain":{"name":"yoyo20","description":"yoyo20","ldapSet":false}}'
#print type(account_dict)
#aj = json.dumps(account_dict)
#print type(aj)

#send_url = 'https://console.zerostack.com/os/6366ac07-6c56-4899-991d-b75607d02f32/regions/e333d4a5-4a74-4afc-9f1f-1bd66da3f9e7/keystone/v3/domains'
#r = requests.post(send_url,verify = False,data = account_dict,headers={"content-type":"application/json","X-Auth-Token":token})
#j = json.loads(r.text)
#print j

#send_url = 'https://console.zerostack.com/os/6366ac07-6c56-4899-991d-b75607d02f32/regions/e333d4a5-4a74-4afc-9f1f-1bd66da3f9e7/keystone/v3/domains/c098588fb466427ebbc142036d3c25c3'
#r = requests.get(send_url,verify = False,headers={"content-type":"application/json","X-Auth-Token":token})
#j = json.loads(r.text)
#print j

#send_url = 'https://console.zerostack.com/os/6366ac07-6c56-4899-991d-b75607d02f32/regions/e333d4a5-4a74-4afc-9f1f-1bd66da3f9e7/keystone/v3/domains/4f55420fcbce45059d210fbd0da9ee77'
#r = requests.patch(send_url,verify = False,data = '{"enabled":false}',headers={"content-type":"application/json","X-Auth-Token":token})
#j = json.loads(r.text)
#print j

#send_url = 'https://console.zerostack.com/os/6366ac07-6c56-4899-991d-b75607d02f32/regions/e333d4a5-4a74-4afc-9f1f-1bd66da3f9e7/keystone/v3/domains/1c86ad0c28dc4ee798eeaa1d9db17056'
#r = requests.patch(send_url,data='{"domain":{"enabled":false}}',verify = True,headers={"content-type":"application/json","X-Auth-Token":token})
#j = json.loads(r.text)
#print j

#send_url = 'https://console.zerostack.com/os/6366ac07-6c56-4899-991d-b75607d02f32/regions/e333d4a5-4a74-4afc-9f1f-1bd66da3f9e7/keystone/v3/projects?domain_id=c098588fb466427ebbc142036d3c25c3'
#r = requests.get(send_url,verify = True,headers={"content-type":"application/json","X-Auth-Token":token})
#j = json.loads(r.text)
#pprint.pprint(j)

#send_url = 'https://console.zerostack.com/os/6366ac07-6c56-4899-991d-b75607d02f32/regions/e333d4a5-4a74-4afc-9f1f-1bd66da3f9e7/nova/v2/9f470e754aa94281aa79bcad27928269'
#r = requests.get(send_url,verify = True,headers={"content-type":"application/json","X-Auth-Token":token})
#print r
#j = json.loads(r.text)
#pprint.pprint(j)

#send_url = 'https://console.zerostack.com/os/6366ac07-6c56-4899-991d-b75607d02f32/regions/e333d4a5-4a74-4afc-9f1f-1bd66da3f9e7/keystone/v3/users'
#data = '{"user":{"email":"gabba7@mail.com","enabled":true,"name":"gabba7","domain_id":"c098588fb466427ebbc142036d3c25c3","password":"password"}}'
#r = requests.post(send_url,data = data,verify = True,headers={"content-type":"application/json","X-Auth-Token":token})
#j = json.loads(r.text)
#pprint.pprint(j)

#send_url = 'https://console.zerostack.com/os/6366ac07-6c56-4899-991d-b75607d02f32/regions/e333d4a5-4a74-4afc-9f1f-1bd66da3f9e7/keystone/v3/domains/c098588fb466427ebbc142036d3c25c3/users/%s/roles/508cb17d503642d7b55a206093abe420'%(j['user']['id'])
#r = requests.put(send_url,verify = True,headers={"content-type":"application/json","X-Auth-Token":token})
#print r
#j = json.loads(r.text)
#pprint.pprint(j)