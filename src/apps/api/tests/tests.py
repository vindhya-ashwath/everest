from django.test import TestCase, Client
from jsonschema import validate
import json
from django.conf import settings
import os


class DealTest(TestCase):
    """
    Test Case class to test the deal API.
    """

    def setup(self):
        self.deal_list_url = "/api/v1/deals/3"
        self.schema_file = os.path.join(settings.ROOT_DIR, "schema/deal.json")
        self.read_schema()
        self.client = Client()

    def read_schema(self):
        self.schema = None
        with open(self.schema_file) as fl:c
            data = fl.readlines()
            self.schema = json.loads(data)

    def test_deals_list(self):

        self.setup()
        response = self.client.get(self.deal_list_url)
        print(response.content)
