from zspython import Zerostack
import pprint
import json

print "*********Project Token**********"
input_dict = {'token_scope':'project','user_region':'uswe'}
auth = Zerostack(input_dict)

print "********Get The Token***********"
a = auth.authenticate()
print a

'''
print "*******Get the raw body*********"
print pprint.pprint(json.loads(auth.get_raw_zstoken_contents()))

print "*******Get the project*******"
print auth.get_zsproject()

print "*******Get the project ID*******"
print auth.get_zsproject_id()

print "*******Get the domain********"
print auth.get_zsdomain()

print "*******Get the BU ID********"
print auth.get_zsbu_id()

print "*******Get the Services********"
print auth.list_zs_services()

print "*******Get the Endpoints********"
for service in auth.list_zs_services():
    print pprint.pprint(auth.get_zs_endpoint(service['endpoint_id']))

print "*******Get the raw zscatalog****"
print pprint.pprint(auth.get_raw_zscatalog())

print "*******Get token owner**********"
print auth.get_zstoken_owner()

print "*******Create user - project token*********"
output = auth.create_user({'username':'blahblah101',
                           'useremail':'blass2@hotmail.com',
                           'password':'blahpass',
                           'role':'Admin',
                           'zs_bu_id':'c098588fb466427ebbc142036d3c25c3'})
print output

print "********Get the region ID*********"
print auth.get_zs_region_id()
'''

print "*********Domain Token**********"
input_dict = {'token_scope':'domain','user_region':'uswe'}
auth = Zerostack(input_dict)

print "********Get The Token***********"
a = auth.authenticate()
print a
'''
print "*******Get the raw body*********"
print pprint.pprint(json.loads(auth.get_raw_zstoken_contents()))

print "*******Get the project*******"
print auth.get_zsproject()

print "*******Get the project ID*******"
print auth.get_zsproject_id()

print "*******Get the domain********"
print auth.get_zs_bu()

print "*******Get the BU ID********"
print auth.get_zsbu_id()

print "*******Get the Services********"
print auth.list_zs_services()

print "*******Get the Endpoints********"
for service in auth.list_zs_services():
    print pprint.pprint(auth.get_zs_endpoint(service['zs_endpoint_id']))

print "*******Get the raw zscatalog****"
print pprint.pprint(auth.get_raw_zscatalog())

print "*******Get token owner**********"
print auth.get_zstoken_owner()

print "*******Create user - domain token*********"
output = auth.create_user({'username':'blahblah101',
                           'useremail':'blass2@hotmail.com',
                           'password':'blahpass',
                           'role':'Admin',
                           'zs_bu_id':'c098588fb466427ebbc142036d3c25c3'})
print output

print "********Get the region ID*********"
print auth.get_zs_region_id()

print "******Create a new Project - Domain tokan********"
print auth.create_zsproject({'description':"blah blah",
                             'zs_bu_id':'c098588fb466427ebbc142036d3c25c3',
                             'project_name':'automationmade',
                             'quota_level':'small'
                            })
'''
print "********List zs projects - domain token**********"
print auth.list_zsprojects()