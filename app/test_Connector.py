import unittest
from unittest.mock import patch
from Connector import *

class TestConnector(unittest.TestCase):


	def test_getListTicketsOperation(self):
		self.assertEqual(ApiOperation().getListTicketsOperation(), "/api/v2/tickets.json")

	def test_getDisplayTicketOperation(self):
		self.assertEqual(ApiOperation().getDisplayTicketOperation(1), "/api/v2/tickets/1.json")

	def test_ApiRequest(self):
		
		str = ApiOperation().getListTicketsOperation()
		query = ApiRequest(str).query
		str = Configuration().getAPI_SERVER() + str
		
		self.assertEqual(query, str)



if __name__ == '__main__':
	unittest.main()
