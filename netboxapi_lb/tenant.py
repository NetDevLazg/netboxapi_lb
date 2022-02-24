import requests
import json
import urllib3
from .BaseConnection import BaseConnection

urllib3.disable_warnings()


class TENANT(BaseConnection):

    def __init__(self,ip,token):
        super().__init__(ip,token)
#----------------------------------------------------------------------------------------------
# GET METHODS
#----------------------------------------------------------------------------------------------
    def get_tenant(self,**filter):
        """
        Gets the list of tenants on Netbox
        Path: Organization > Tenant 
        """

        url_base =  "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}

        if len(filter) == 0:
            get_tenant = requests.get(url=url_base+"/tenancy/tenants/",
                                headers=headers,
                                verify=False)
        if len(filter) == 1:
            get_tenant = requests.get(url=url_base+"/tenancy/tenants/?{}".format(filter["filter"]),
                    headers=headers,
                    verify=False)
        if get_tenant.status_code == 200:

            return get_tenant.json()['results']
        else:
            print(get_tenant.status_code)
            return get_tenant.status_code
#----------------------------------------------------------------------------------------------
# POST METHODS
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# DELETE METHODS
#----------------------------------------------------------------------------------------------

