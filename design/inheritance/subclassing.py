"""
        Subclassing should be used to specialize objects by
            creating detailed abstractions starting from based ones.
"""

from urllib.request import Request, urlopen
import json
import logging


class GetPublicIpRequest(Request):
    PUBLIC_IP_API_URL = "https://api.ipify.org?format=json"
    PUBLIC_IP_API_HEADERS = {"contentType": "json"}

    def __init__(self):
        # Create Request object
        super().__init__(self.PUBLIC_IP_API_URL, headers=self.PUBLIC_IP_API_HEADERS)


def get_public_ip(request: GetPublicIpRequest) -> dict:
    response = urlopen(request)
    response_content = response.read()

    try:
        return json.loads(response_content)

    except json.decoder.JSONDecodeError as e:
        logging.error((e, response_content))


my_public_ip = get_public_ip(GetPublicIpRequest())

print(my_public_ip)
