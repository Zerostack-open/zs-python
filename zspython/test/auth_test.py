from zspython import Zerostack
import pprint
import json
import time
import random

'''
print "*********Project Token**********"
input_dict = {'token_scope':'project','user_region':'uswe'}
auth = Zerostack(input_dict)

print "********Get The Token***********"
a = auth.authenticate()
print a

print "*******Get the raw body*********"
print pprint.pprint(json.loads(auth.get_raw_zstoken_contents()))

print "*******Get the project*******"
print auth.get_zsproject()

print "*******Get the project ID*******"
print auth.get_zsproject_id()

print "*******Get the domain********"
print auth.get_zs_bu()

print "*******Get the BU ID********"
bu = auth.get_zsbu_id()
print bu

print "*******Get the Services********"
print auth.list_zs_services()

print "*******Get the Endpoints********"
for service in auth.list_zs_services():
    print pprint.pprint(auth.get_zs_endpoint(service['zs_endpoint_id']))

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

print "\n********Get the region ID*********"
print auth.get_zs_region_id()


print "\n******Create a new Project - Project token********"
create_proj = auth.create_zsproject({'description':"blah blah",
                             'zs_bu_id':bu,
                             'project_name':'automationmade',
                             'quota_level':'small'
                            })

print create_proj

print "\n*****Get project Details - Project Token**********"
get_proj_detail = auth.get_zsproject_details()
print get_proj_detail

time.sleep(10)

print "\n********List zs projects - Project token**********"
print auth.list_zsprojects()

print "\n*****Delete the new project - Project Token*******"
delete_proj_detail = auth.delete_zsproject(create_proj['zs_project_id'])
print delete_proj_detail

print "\n\n"
'''
print "*********Domain Token**********"
input_dict = {'token_scope':'domain','user_region':'uswe'}
auth2 = Zerostack(input_dict)

print "\n********Get The Token***********"
a = auth2.authenticate()
print a

print "\n*******Get the raw body*********"
print pprint.pprint(json.loads(auth2.get_raw_zstoken_contents()))

print "\n*******Get the project*******"
print auth2.get_zsproject()

print "\n*******Get the project ID*******"
print auth2.get_zsproject_id()

print "\n*******Get the domain********"
print auth2.get_zs_bu()

print "\n*******Get the BU ID********"
print auth2.get_zsbu_id()

print "\n*******Get the Services********"
print auth2.list_zs_services()

print "\n*******Get the Endpoints********"
for service in auth2.list_zs_services():
    print pprint.pprint(auth2.get_zs_endpoint(service['zs_endpoint_id']))

print "\n*******Get the raw zscatalog****"
print pprint.pprint(auth2.get_raw_zscatalog())

print "\n*******Get token owner**********"
print auth2.get_zstoken_owner()

print "\n*******List the ZS Bu IDs*******"
listbu = auth2.list_zsbusiness_units()
print listbu

new_bu_name = "automation_%s"%(random.randint(0,1002))

print "\n*******Create a new ZSBU - automation*********"
zsbu = auth2.create_zsbusiness_unit({'bu_name':new_bu_name,'bu_description':'Created by zs python'})
print zsbu

print "\n*******Create user - domain token*********"
output = auth2.create_user({'username':'blahblah101',
                           'useremail':'blass2@hotmail.com',
                           'password':'blahpass',
                           'role':'Admin',
                           'zs_bu_id':zsbu['zs_bu_id']})
print output

print "\n********Get the region ID*********"
print auth2.get_zs_region_id()

print "\n******Create a new Project - Domain tokan********"
create_proj = auth2.create_zsproject({'description':"blah blah",
                             'zs_bu_id':zsbu['zs_bu_id'],
                             'project_name':'automationmade',
                             'quota_level':'small'
                            })

print create_proj

print "\n*****Get project Details - Domain Token**********"
get_proj_detail = auth2.get_zsproject_details(create_proj['zs_project_id'])
print get_proj_detail

print "\n*****Delete the new project - Domain Token*******"
delete_proj_detail = auth2.delete_zsproject(create_proj['zs_project_id'])
print delete_proj_detail