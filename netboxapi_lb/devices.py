import requests
import json
import urllib3
from .BaseConnection import BaseConnection

urllib3.disable_warnings()


class DEVICES(BaseConnection):

    def __init__(self, ip, token):
        super().__init__(ip, token)

# ----------------------------------------------------------------------------------------------
# GET METHODS
# ----------------------------------------------------------------------------------------------

    def get_devices(self, **filter):
        """
        Gets a list of all Devices on Netbox, Pass filter to filter results
        """
        url_base = "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                   "Accept": "application/json",
                   "Authorization": "Token  {token}".format(token=self.token)}

        if len(filter) == 0:
            get_devices = requests.get(url=url_base+"/dcim/devices/",
                                       headers=headers,
                                       verify=False)

        if len(filter) == 1:
            get_devices = requests.get(url=url_base+"/dcim/devices/?{}".format(filter["filter"]),
                                       headers=headers,
                                       verify=False)

        if get_devices.status_code == 200:
            return get_devices.json()['results']
        else:
            return get_devices.status_code

    def get_device_role(self, **filter):
        """
        Gets a list of all Devices Role on Netbox, Pass filter to filter results
        """
        url_base = "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                   "Accept": "application/json",
                   "Authorization": "Token  {token}".format(token=self.token)}

        if len(filter) == 0:
            get_device_role = requests.get(url=url_base+"/dcim/device-roles/",
                                           headers=headers,
                                           verify=False)

        if len(filter) == 1:
            get_device_role = requests.get(url=url_base+"/dcim/device-roles/?{}".format(filter["filter"]),
                                           headers=headers,
                                           verify=False)

        if get_device_role.status_code == 200:
            return get_device_role.json()['results']
        else:
            return get_device_role.status_code

    def get_device_platform(self, **filter):
        """
        Gets a list of all Devices Platform on Netbox, Pass filter to filter results
        """
        url_base = "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                   "Accept": "application/json",
                   "Authorization": "Token  {token}".format(token=self.token)}

        if len(filter) == 0:
            get_device_platform = requests.get(url=url_base+"/dcim/platforms/",
                                               headers=headers,
                                               verify=False)

        if len(filter) == 1:
            get_device_platform = requests.get(url=url_base+"/dcim/platforms/?{}".format(filter["filter"]),
                                               headers=headers,
                                               verify=False)

        if get_device_platform.status_code == 200:
            return get_device_platform.json()['results']
        else:
            return get_device_platform.status_code

    def get_device_manufacturer(self, **filter):
        """
        Gets a list of all Devices Manufacturer on Netbox, Pass filter to filter results
        """
        url_base = "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                   "Accept": "application/json",
                   "Authorization": "Token  {token}".format(token=self.token)}

        if len(filter) == 0:
            get_device_manufacturer = requests.get(url=url_base+"/dcim/manufacturers/",
                                                   headers=headers,
                                                   verify=False)

        if len(filter) == 1:
            get_device_manufacturer = requests.get(url=url_base+"/dcim/manufacturers/?{}".format(filter["filter"]),
                                                   headers=headers,
                                                   verify=False)

        if get_device_manufacturer.status_code == 200:
            return get_device_manufacturer.json()['results']
        else:
            return get_device_manufacturer.status_code

    def get_device_inventory_item(self, **filter):
        """
        Gets a list of all Devices Inventory Items on Netbox, Pass filter to filter results
        """
        url_base = "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                   "Accept": "application/json",
                   "Authorization": "Token  {token}".format(token=self.token)}

        if len(filter) == 0:
            get_device_inventory_item = requests.get(url=url_base+"/dcim/inventory-items/",
                                                     headers=headers,
                                                     verify=False)

        if len(filter) == 1:
            get_device_inventory_item = requests.get(url=url_base+"/dcim/inventory-items/?{}".format(filter["filter"]),
                                                     headers=headers,
                                                     verify=False)

        if get_device_inventory_item.status_code == 200:
            return get_device_inventory_item.json()['results']
        else:
            return get_device_inventory_item.status_code

# ----------------------------------------------------------------------------------------------
# POST METHODS
# ----------------------------------------------------------------------------------------------

    def create_device_inventory_item(self, data):
        """
        Creates a Device Inventory Item on Netbox, Must pass data
        """
        data = json.dumps(data, indent=4)

        url_base = "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                   "Accept": "application/json",
                   "Authorization": "Token  {token}".format(token=self.token)}

        create_device_inventory_item = requests.post(url=url_base+"/dcim/inventory-items/",
                                                     headers=headers,
                                                     verify=False,
                                                     data=data)

        return create_device_inventory_item

# ----------------------------------------------------------------------------------------------
# PATCH METHODS
# ----------------------------------------------------------------------------------------------

    def patch_device(self, id, data):
        """
        Patches a device on Netbox, Must pass data
        """
        data = json.dumps(data, indent=4)

        url_base = "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                   "Accept": "application/json",
                   "Authorization": "Token  {token}".format(token=self.token)}

        patch_device = requests.patch(url=url_base+"/dcim/devices/{}/".format(id),
                                      headers=headers,
                                      verify=False,
                                      data=data)

        return patch_device

    def patch_device_inventory_item(self, id, data):
        """
        Patches a inventory-items on Netbox, Must pass data
        """
        data = json.dumps(data, indent=4)

        url_base = "http://{ip}/api".format(ip=self.ip)

        headers = {"Content-type": "application/json",
                   "Accept": "application/json",
                   "Authorization": "Token  {token}".format(token=self.token)}

        device_inventory_item = requests.patch(url=url_base+"/dcim/inventory-items/{}/".format(id),
                                               headers=headers,
                                               verify=False,
                                               data=data)

        return device_inventory_item
