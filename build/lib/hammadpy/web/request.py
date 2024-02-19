
#==============================================================================#
#== Hammad Saeed ==============================================================#
#==============================================================================#
#== www.hammad.fun ============================================================#
#== hammad@supportvectors.com =================================================#
#==============================================================================#

##== HamPy ==######################################== Hammad's Python Tools ==##
##== @/extensions/requests ==##############################################

#==============================================================================#

import requests

class Requests:
    """
    Extends the 'requests' library with convenience functions for sending 
    and receiving data.
    """

    def __init__(self):
        self.session = requests.Session()

    def send(self, method, url, data=None, json=None, headers=None, **kwargs):
        """
        Sends data to a URL using the specified HTTP method.

        Args:
            method (str):  The HTTP method (e.g., 'GET', 'POST').
            url (str): The target URL.
            data (dict, optional):  Data to send as form data.
            json (dict, optional):  Data to send as JSON.
            headers (dict, optional): HTTP headers. 
            **kwargs: Additional keyword arguments for the 'requests' call.

        Returns:
            requests.Response: The response object.
        """

        return self.session.request(method, url, data=data, json=json, headers=headers, **kwargs)

    def get_json(self, url, **kwargs):
        """
        Fetches data from a URL and parses the response as JSON.

        Args:
            url (str): The target URL.
            **kwargs: Additional keyword arguments for the 'requests' call.

        Returns:
            dict: The parsed JSON data.
        """

        response = self.session.get(url, **kwargs)
        response.raise_for_status()  # Raise an exception for error statuses
        return response.json()

#==============================================================================#
