import requests
import json
import urllib3
from .BaseConnection import BaseConnection

urllib3.disable_warnings()


class ORGANIZATION(BaseConnection):

    def __init__(self,ip,token):
        super().__init__(ip,token)
#----------------------------------------------------------------------------------------------
# GET METHODS
#----------------------------------------------------------------------------------------------
    def get_site(self, **filter):
        """
        Gets a list of all sites on Netbox, Pass filter to filter results
        """
        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}
        
        if len(filter) == 0:
            get_site = requests.get(url=url_base+"/dcim/sites/",
                                headers=headers,
                                verify=False)

        if len(filter) == 1:
            get_site = requests.get(url=url_base+"/dcim/sites/?{}".format(filter["filter"]),
                    headers=headers,
                    verify=False)
        
        if get_site.status_code == 200:
            return get_site.json()['results']
        else:
            return get_site.status_code

    def get_tenants(self, **filter):
        """
        Gets a list of all Tenants on Netbox, Pass filter to filter results
        """
        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}
        
        if len(filter) == 0:
            get_tenants = requests.get(url=url_base+"/tenancy/tenants/",
                                headers=headers,
                                verify=False)

        if len(filter) == 1:
            get_tenants = requests.get(url=url_base+"/tenancy/tenants/?{}".format(filter["filter"]),
                    headers=headers,
                    verify=False)
        
        if get_tenants.status_code == 200:
            return get_tenants.json()['results']
        else:
            return get_tenants.status_code