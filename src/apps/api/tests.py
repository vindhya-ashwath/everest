from django.test import TestCase, Client
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "price": {"type": "number"},
        "name": {"type": "string"},
    },
}


class DealTestCase(TestCase):
    """
    Test Case class to test the deal API.
    """

    def setup(self):
        self.deal_list_url = "/api/v1/deals/3"
        self.client = Client()

    def test_deals_list(self):

        # self.assertIs('1', '2')
        self.setup()
        print(validate({"name": "Eggs", "price": "34.99"}, schema))
        response = self.client.get(self.deal_list_url)
        print(response.content)
