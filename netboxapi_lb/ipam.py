import requests
import json
import urllib3
from .BaseConnection import BaseConnection

urllib3.disable_warnings()

class IPAM(BaseConnection):


    def __init__(self,ip,token):
        super().__init__(ip,token)

#----------------------------------------------------------------------------------------------
# GET METHODS
#----------------------------------------------------------------------------------------------

    def get_vlan(self,**filter):
        """
        Gets a list of VLAN Roles created on Netbox IPAM.
        Path: IPAM>VLAN.
        If using filters please fill fuctions as folow.
        filter="name=test"
        """
        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}

        if len(filter) == 0:
            get_vlan = requests.get(url=url_base+"/ipam/vlans/",
                                headers=headers,
                                verify=False)
        if len(filter) == 1:
            get_vlan = requests.get(url=url_base+"/ipam/vlans/?{}".format(filter["filter"]),
                    headers=headers,
                    verify=False)
        if get_vlan.status_code == 200:

            return get_vlan.json()['results']
        else:
            return get_vlan.status_code

    def get_ip(self,**filter):
        """
        Gets a list of IP on Netbox IPAM.
        Path: IPAM>VLAN.
        If using filters please fill fuctions as folow.
        filter="name=test"
        """
        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}

        if len(filter) == 0:
            get_ip = requests.get(url=url_base+"/ipam/ip-addresses/",
                                headers=headers,
                                verify=False)
        if len(filter) == 1:
            get_ip = requests.get(url=url_base+"/ipam/ip-addresses/?{}".format(filter["filter"]),
                    headers=headers,
                    verify=False)
        if get_ip.status_code == 200:
            return get_ip.json()['results']
        else:
            return get_ip.status_code


    def get_rirs(self,**filter):
        """
        Gets a list of IPAM Rirs on Netbox.
        Path: IPAM>RIRS.
        If using filters please fill fuctions as folow.
        filter="name=test"
        """
        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}

        if len(filter) == 0:
            get_rirs = requests.get(url=url_base+"/ipam/rirs/",
                                headers=headers,
                                verify=False)
        if len(filter) == 1:
            get_rirs = requests.get(url=url_base+"/ipam/rirs/?{}".format(filter["filter"]),
                    headers=headers,
                    verify=False)
        if get_rirs.status_code == 200:
            return get_rirs.json()['results']
        else:
            return get_rirs.status_code

    def get_aggregates(self,**filter):
        """
        Gets a list of IPAM Aggregates on Netbox.
        Path: IPAM>Aggregates.
        If using filters please fill fuctions as folow.
        filter="name=test"
        """
        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}

        if len(filter) == 0:
            get_aggregates = requests.get(url=url_base+"/ipam/aggregates/",
                                headers=headers,
                                verify=False)
        if len(filter) == 1:
            get_aggregates = requests.get(url=url_base+"/ipam/aggregates/?{}".format(filter["filter"]),
                    headers=headers,
                    verify=False)
        if get_aggregates.status_code == 200:
            return get_aggregates.json()['results']
        else:
            return get_aggregates.status_code


    def get_roles(self,**filter):
        """
        Gets a list of IPAM Prefix Roles on Netbox.
        Path: IPAM>Roles.
        If using filters please fill fuctions as folow.
        filter="name=test"
        """
        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}

        if len(filter) == 0:
            get_roles = requests.get(url=url_base+"/ipam/roles/",
                                headers=headers,
                                verify=False)
        if len(filter) == 1:
            get_roles = requests.get(url=url_base+"/ipam/roles/?{}".format(filter["filter"]),
                    headers=headers,
                    verify=False)
        if get_roles.status_code == 200:
            return get_roles.json()['results']
        else:
            return get_roles.status_code

    def get_prefixes(self,**filter):
        """
        Gets a list of IPAM Prefixes on Netbox.
        Path: IPAM>Prefixes.
        If using filters please fill fuctions as folow.
        filter="name=test"
        """
        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}

        if len(filter) == 0:
            get_prefixes = requests.get(url=url_base+"/ipam/prefixes/",
                                headers=headers,
                                verify=False)
        if len(filter) == 1:
            get_prefixes = requests.get(url=url_base+"/ipam/prefixes/?{}".format(filter["filter"]),
                    headers=headers,
                    verify=False)
        if get_prefixes.status_code == 200:
            return get_prefixes.json()['results']
        else:
            return get_prefixes.status_code


#----------------------------------------------------------------------------------------------
# POST METHODS
#----------------------------------------------------------------------------------------------

    def create_ip(self, data):
        """
        Creates a ip address on Netbox, Must pass data
        """
        data = json.dumps(data,indent=4)

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        create_ip = requests.post(url=url_base+"/ipam/ip-addresses/",
                headers=headers,
                verify=False,
                data=data)
        
        return create_ip

    def create_rirs(self, data):
        """
        Creates a IPAM RIR on Netbox, Must pass data
        """
        data = json.dumps(data,indent=4)

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        create_rirs = requests.post(url=url_base+"/ipam/rirs/",
                headers=headers,
                verify=False,
                data=data)
        
        return create_rirs

    def create_aggregates(self, data):
        """
        Creates a IPAM Aggregates on Netbox, Must pass data
        """
        data = json.dumps(data,indent=4)

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        create_aggregates = requests.post(url=url_base+"/ipam/aggregates/",
                headers=headers,
                verify=False,
                data=data)
        
        return create_aggregates

    def create_roles(self, data):
        """
        Creates a IPAM Roles on Netbox, Must pass data
        """
        data = json.dumps(data,indent=4)

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        create_roles = requests.post(url=url_base+"/ipam/roles/",
                headers=headers,
                verify=False,
                data=data)
        
        return create_roles

    def create_prefixes(self, data):
        """
        Creates a IPAM Prefixes on Netbox, Must pass data
        """
        data = json.dumps(data,indent=4)

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        create_prefixes = requests.post(url=url_base+"/ipam/prefixes/",
                headers=headers,
                verify=False,
                data=data)
        
        return create_prefixes

#----------------------------------------------------------------------------------------------
# PATCH METHODS
#----------------------------------------------------------------------------------------------

    def patch_ip(self, id ,data):
        """
        Patches an ip address on Netbox, Must pass data
        """
        data = json.dumps(data,indent=4)

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        patch_ip = requests.patch(url=url_base+"/ipam/ip-addresses/{}/".format(id),
                headers=headers,
                verify=False,
                data=data)
        
        return patch_ip

    def patch_rirs(self, id ,data):
        """
        Patches an IPAM RIR on Netbox, Must pass data
        """
        data = json.dumps(data,indent=4)

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        patch_rirs = requests.patch(url=url_base+"/ipam/rirs/{}/".format(id),
                headers=headers,
                verify=False,
                data=data)
        
        return patch_rirs

    def patch_aggregates(self, id ,data):
        """
        Patches an IPAM Aggregates on Netbox, Must pass data
        """
        data = json.dumps(data,indent=4)

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        patch_aggregates = requests.patch(url=url_base+"/ipam/aggregates/{}/".format(id),
                headers=headers,
                verify=False,
                data=data)
        
        return patch_aggregates

    def patch_roles(self, id ,data):
        """
        Patches an IPAM Roles on Netbox, Must pass data
        """
        data = json.dumps(data,indent=4)

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        patch_roles = requests.patch(url=url_base+"/ipam/roles/{}/".format(id),
                headers=headers,
                verify=False,
                data=data)
        
        return patch_roles


    def patch_prefixes(self, id ,data):
        """
        Patches an IPAM Prefixes on Netbox, Must pass data
        """
        data = json.dumps(data,indent=4)

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        patch_prefixes = requests.patch(url=url_base+"/ipam/prefixes/{}/".format(id),
                headers=headers,
                verify=False,
                data=data)
        
        return patch_prefixes


#----------------------------------------------------------------------------------------------
# DELETE METHODS
#----------------------------------------------------------------------------------------------

    def delete_ip(self, id):
        """
        Deletes an ip address on Netbox, Must pass ID
        """

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        delete_ip = requests.delete(url=url_base+"/ipam/ip-addresses/{}/".format(id),
                headers=headers,
                verify=False,)
        
        return delete_ip

    def delete_rirs(self, id):
        """
        Deletes an IPAM RIR on Netbox, Must pass ID
        """

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        delete_rirs = requests.delete(url=url_base+"/ipam/rirs/{}/".format(id),
                headers=headers,
                verify=False,)
        
        return delete_rirs


    def delete_aggregates(self, id):
        """
        Deletes an IPAM Aggregates on Netbox, Must pass ID
        """

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        delete_aggregates = requests.delete(url=url_base+"/ipam/aggregates/{}/".format(id),
                headers=headers,
                verify=False,)
        
        return delete_aggregates


    def delete_roles(self, id):
        """
        Deletes an IPAM Roles on Netbox, Must pass ID
        """

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        delete_roles = requests.delete(url=url_base+"/ipam/roles/{}/".format(id),
                headers=headers,
                verify=False,)
        
        return delete_roles

    def delete_prefixes(self, id):
        """
        Deletes an IPAM Prefixes on Netbox, Must pass ID
        """

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        delete_prefixes = requests.delete(url=url_base+"/ipam/prefixes/{}/".format(id),
                headers=headers,
                verify=False,)
        
        return delete_prefixes