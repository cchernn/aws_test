import os
import boto3
from errors import error_handler

region_default = "us-east-2"

class AWS:
    def __init__(self, region=None, path=None):
        # region, session, path
        self.region = region_default
        self.CreateSession(self.region) # declare self.session
        self.path = os.getenv("HOME") if path is None else path

    @error_handler()
    def CreateSession(self, region=None):
        if region is None:
            region=self.region
        self.session = boto3.Session(region_name=region)
        self.region = self.session.region_name

    @error_handler()
    def CreateResource(self, resource):
        self.resource = self.session.resource(resource)

if __name__ == "__main__":
    pass