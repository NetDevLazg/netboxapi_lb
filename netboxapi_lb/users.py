import requests
import json
import urllib3
from .BaseConnection import BaseConnection

urllib3.disable_warnings()


class USER(BaseConnection):

    def __init__(self, ip, token):
        super().__init__(ip, token)

# ----------------------------------------------------------------------------------------------
# GET METHODS
# ----------------------------------------------------------------------------------------------

    def get_user_groups(self, **filter):
        """
        Gets the list of user groups on Netbox
        Path: Admin  > Users > Groups 
        """

        url_base = "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                   "Accept": "application/json",
                   "Authorization": "Token  {token}".format(token=self.token)}

        if len(filter) == 0:
            get_user_groups = requests.get(url=url_base+"/users/groups/",
                                           headers=headers,
                                           verify=False)
        if len(filter) == 1:
            get_user_groups = requests.get(url=url_base+"/users/groups/?{}".format(filter["filter"]),
                                           headers=headers,
                                           verify=False)
        if get_user_groups.status_code == 200:

            return get_user_groups.json()['results']
        else:
            print(get_user_groups.status_code)
            return get_user_groups.status_code

    def get_user_permissions(self, **filter):
        """
        Gets the list of user groups on Netbox
        Path: Admin  > Users > Permissions 
        """

        url_base = "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                   "Accept": "application/json",
                   "Authorization": "Token  {token}".format(token=self.token)}

        if len(filter) == 0:
            get_user_permissions = requests.get(url=url_base+"/users/permissions/",
                                                headers=headers,
                                                verify=False)
        if len(filter) == 1:
            get_user_permissions = requests.get(url=url_base+"/users/permissions/?{}".format(filter["filter"]),
                                                headers=headers,
                                                verify=False)
        if get_user_permissions.status_code == 200:

            return get_user_permissions.json()['results']
        else:
            print(get_user_permissions.status_code)
            return get_user_permissions.status_code

# ----------------------------------------------------------------------------------------------
# POST METHODS
# ----------------------------------------------------------------------------------------------

    def create_user_groups(self, data):
        """
        Creates a user group in Netbox, Must pass data
        """
        data = json.dumps(data, indent=4)

        url_base = "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                   "Accept": "application/json",
                   "Authorization": "Token  {token}".format(token=self.token)}

        create_user_group = requests.post(url=url_base+"/users/groups/",
                                          headers=headers,
                                          verify=False,
                                          data=data)

        return create_user_group

    def create_user_permissions(self, data):
        """
        Creates a user permission in Netbox, Must pass data
        """
        data = json.dumps(data, indent=4)

        url_base = "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                   "Accept": "application/json",
                   "Authorization": "Token  {token}".format(token=self.token)}

        create_user_permissions = requests.post(url=url_base+"/users/permissions/",
                                                headers=headers,
                                                verify=False,
                                                data=data)

        return create_user_permissions


# ----------------------------------------------------------------------------------------------
# PUT METHODS
# ----------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------
# DELETE METHODS
# ----------------------------------------------------------------------------------------------
