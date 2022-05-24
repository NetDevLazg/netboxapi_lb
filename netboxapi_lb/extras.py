import requests
import json
import urllib3
from .BaseConnection import BaseConnection

urllib3.disable_warnings()


class EXTRAS(BaseConnection):

    def __init__(self,ip,token,protocol):
        super().__init__(ip,token,protocol)

#----------------------------------------------------------------------------------------------
# GET METHODS
#----------------------------------------------------------------------------------------------

    def get_image(self,**filter):
        """
        Gets a list of all images attached to network
        """
        url_base = "{protocol}://{ip}/api".format(protocol=self.protocol,ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}
        
        if len(filter) == 0:
            get_image = requests.get(url=url_base+"/extras/image-attachments/",
                                headers=headers,
                                verify=False)

        if len(filter) == 1:
            get_image = requests.get(url=url_base+"/extras/image-attachments/?{}".format(filter["filter"]),
                    headers=headers,
                    verify=False)
        
        if get_image.status_code == 200:
            return get_image.json()['results']
        else:
            return get_image.status_code

#----------------------------------------------------------------------------------------------
# POST METHODS
#----------------------------------------------------------------------------------------------

    def create_image(self, data):
        """
        Creates an image on Netbox, must pass data
        """
        data = json.dumps(data,indent=4)

        url_base = "{protocol}://{ip}/api".format(protocol=self.protocol,ip=self.ip)

        headers = {"Content-type": "application/json",
                    "Accept": "application/json",
                    "Authorization" : "Token  {token}".format(token=self.token)}


        create_image = requests.post(url=url_base+"/extras/image-attachments/",
                headers=headers,
                verify=False,
                data=data)
        
        return create_image