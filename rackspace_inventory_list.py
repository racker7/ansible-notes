#!/usr/bin/env python2
#import the pyrax module
import pyrax
#set the identity type to Rackspace
pyrax.set_setting("identity_type", "rackspace")
#Show Pyrax where to find your credentials
pyrax.set_credential_file("/root/.rackspace_cloud_credentials")
#Quick example to list servers.
cs_dfw = pyrax.connect_to_cloudservers(region="DFW")
cs_ord = pyrax.connect_to_cloudservers(region="ORD")
cs_iad = pyrax.connect_to_cloudservers(region="IAD")
dfw_servers = cs_dfw.list()
ord_servers = cs_ord.list()
iad_servers = cs_iad.list()
all_servers = dfw_servers + ord_servers + iad_servers
print "DFW Servers"
print dfw_servers
print "ORD Servers"
print ord_servers
print "IAD Servers"
print iad_servers
print "All Servers"
print all_servers
