import requests
import json
import urllib3
from .BaseConnection import BaseConnection

urllib3.disable_warnings()


class VIRTUALIZATION(BaseConnection):

    def __init__(self,ip,token):
        super().__init__(ip,token)
#----------------------------------------------------------------------------------------------
# GET METHODS
#----------------------------------------------------------------------------------------------
    def get_vm(self, **filter):
        """
        Gets a list of all virtual machines on Netbox, Pass filter to filter results
        """
        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}
        
        if len(filter) == 0:
            get_vm = requests.get(url=url_base+"/virtualization/virtual-machines/",
                                headers=headers,
                                verify=False)

        if len(filter) == 1:
            get_vm = requests.get(url=url_base+"/virtualization/virtual-machines/?{}".format(filter["filter"]),
                    headers=headers,
                    verify=False)
        
        if get_vm.status_code == 200:
            return get_vm.json()['results']
        else:
            return get_vm.status_code

    def get_cluster(self, **filter):
        """
        Gets a list of all virtualization clusters on Netbox, Pass filter to filter results
        """
        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}
        
        if len(filter) == 0:
            get_cluster = requests.get(url=url_base+"/virtualization/clusters/",
                                headers=headers,
                                verify=False)

        if len(filter) == 1:
            get_cluster = requests.get(url=url_base+"/virtualization/clusters/?{}".format(filter["filter"]),
                    headers=headers,
                    verify=False)
        
        if get_cluster.status_code == 200:
            return get_cluster.json()['results']
        else:
            return get_cluster.status_code

    def get_cluster_type(self, **filter):
        """
        Gets a list of all virtualization clusters types on Netbox, Pass filter to filter results
        """
        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}
        
        if len(filter) == 0:
            get_cluster_type = requests.get(url=url_base+"/virtualization/cluster-types/",
                                headers=headers,
                                verify=False)

        if len(filter) == 1:
            get_cluster_type = requests.get(url=url_base+"/virtualization/cluster-types/?{}".format(filter["filter"]),
                    headers=headers,
                    verify=False)
        
        if get_cluster_type.status_code == 200:
            return get_cluster_type.json()['results']
        else:
            return get_cluster_type.status_code


    def get_cluster_group(self, **filter):
        """
        Gets a list of all virtualization clusters groups on Netbox, Pass filter to filter results
        """
        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}
        
        if len(filter) == 0:
            get_cluster_group = requests.get(url=url_base+"/virtualization/cluster-groups/",
                                headers=headers,
                                verify=False)

        if len(filter) == 1:
            get_cluster_group = requests.get(url=url_base+"/virtualization/cluster-groups/?{}".format(filter["filter"]),
                    headers=headers,
                    verify=False)
        
        if get_cluster_group.status_code == 200:
            return get_cluster_group.json()['results']
        else:
            return get_cluster_group.status_code

    def get_vm_interface(self, **filter):
        """
        Gets a list of all virtual machine interfaces on Netbox, Pass filter to filter results
        """
        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}
        
        if len(filter) == 0:
            get_vm_interface = requests.get(url=url_base+"/virtualization/interfaces/",
                                headers=headers,
                                verify=False)

        if len(filter) == 1:
            get_vm_interface = requests.get(url=url_base+"/virtualization/interfaces/?{}".format(filter["filter"]),
                    headers=headers,
                    verify=False)
        
        if get_vm_interface.status_code == 200:
            return get_vm_interface.json()['results']
        else:
            return get_vm_interface.status_code


#----------------------------------------------------------------------------------------------
# POST METHODS
#----------------------------------------------------------------------------------------------

    def create_cluster(self, data):
        """
        Creates a virtualization clusters on Netbox, Must pass data
        """
        data = json.dumps(data,indent=4)

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        create_cluster = requests.post(url=url_base+"/virtualization/clusters/",
                headers=headers,
                verify=False,
                data=data)
        
        return create_cluster


    def create_vm(self, data):
        """
        Creates a virtual machine on Netbox, Must pass data
        """
        data = json.dumps(data,indent=4)

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        create_vm = requests.post(url=url_base+"/virtualization/virtual-machines/",
                headers=headers,
                verify=False,
                data=data)
        
        return create_vm

    def create_vm_interface(self, data):
        """
        Creates a virtual machine interfaces on Netbox, Must pass data
        """
        data = json.dumps(data,indent=4)

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        create_vm_interface = requests.post(url=url_base+"/virtualization/interfaces/",
                headers=headers,
                verify=False,
                data=data)
        
        return create_vm_interface


#----------------------------------------------------------------------------------------------
# PATCH METHODS
#----------------------------------------------------------------------------------------------

    def patch_vm(self, data, vm_id):
        """
        Patch a virtual machine on Netbox, Must pass data
        """
        data = json.dumps(data,indent=4)

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        patch_vm = requests.patch(url=url_base+"/virtualization/virtual-machines/{}/".format(vm_id),
                headers=headers,
                verify=False,
                data=data)
        
        return patch_vm