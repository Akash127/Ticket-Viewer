import unittest
from unittest.mock import patch
from Tickets import DateParser


class TestTickets(unittest.TestCase):

	def test_parse(self):
		date = "2018-03-03T00:15:44Z"
		self.assertEqual(DateParser().parse(date), "Date: 3/3/2018 Time: 0:15:44")



if __name__ == '__main__':
	unittest.main()()