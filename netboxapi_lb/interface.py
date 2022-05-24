import requests
import json
import urllib3
from .BaseConnection import BaseConnection

urllib3.disable_warnings()


class INTERFACE(BaseConnection):

    def __init__(self,ip,token,protocol):
        super().__init__(ip,token,protocol)
#----------------------------------------------------------------------------------------------
# GET METHODS
#----------------------------------------------------------------------------------------------
    def get_interface(self,**filter):
        """
        Gets the list of interfaces on Netbox
        Path: Devices > Interfaces
        """

        url_base = "{protocol}://{ip}/api".format(protocol=self.protocol,ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}

        if len(filter) == 0:
            get_interface = requests.get(url=url_base+"/dcim/interfaces/",
                                headers=headers,
                                verify=False)
        if len(filter) == 1:
            get_interface = requests.get(url=url_base+"/dcim/interfaces/?{}".format(filter["filter"]),
                    headers=headers,
                    verify=False)
        if get_interface.status_code == 200:

            return get_interface.json()['results']
        else:
            print(get_interface.status_code)
            return get_interface.status_code
#----------------------------------------------------------------------------------------------
# POST METHODS
#----------------------------------------------------------------------------------------------
    def create_interface(self, data):
        """
        Creates a interface for a device on Netbox, Must pass data
        """
        data = json.dumps(data,indent=4)

        url_base = "{protocol}://{ip}/api".format(protocol=self.protocol,ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        create_interface = requests.post(url=url_base+"/dcim/interfaces/",
                headers=headers,
                verify=False,
                data=data)
        
        return create_interface


#----------------------------------------------------------------------------------------------
# DELETE METHODS
#----------------------------------------------------------------------------------------------

    def delete_interface(self, id):
        """
        Deletes an interface on Netbox, Must pass ID
        """

        url_base = "{protocol}://{ip}/api".format(protocol=self.protocol,ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        delete_interface = requests.delete(url=url_base+"/dcim/interfaces/{}/".format(id),
                headers=headers,
                verify=False,)
        
        return delete_interface