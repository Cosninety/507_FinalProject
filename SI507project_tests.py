import csv
import json

from artist_database import *
from SI507project_tools import *
import unittest
#Tests adapted from sample_tests_example.py
#
# class TestScrape(unittest.TestCase): #Testing that data has been retrieved from the website
#     def test_scraper():
#         webpage = access_page_data("https://www.moma.org/artists")
#         assert(type(self.webpage) == 'str')

class TestArtist(unittest.TestCase): #This class contains some general practice tests
	def setUp(self):
		self.art = Artist(Nationality= "French", Gender= "Male",Name= "Francois")

	def test_constructor(self):
		self.assertEqual(self.art.Name,'Francois')
		self.assertEqual(self.art.Gender,'Male')


class TestCsv(unittest.TestCase): #This test checks the CSV output
	def setUp(self):
		self.file = open('artists_spread.csv', encoding = 'utf-8', mode = 'r')
		self.rows = self.file.readlines()
		self.full_row = len(self.rows[1])
		self.row = self.rows[1][0:7]
		self.header = self.rows[0]

	def test_headers(self):
		# self.assertEqual(self.header,'Catalog Number|Nationality|Sex|Art_type|Name|Catalog Number2|Description|Image Source\n')
		self.assertEqual(self.header,'Catalog Number,Nationality,Sex,Art_type,Name,Catalog Number2,Description,Image Source\n')

	def test_row_len(self):
		self.assertEqual(self.full_row, 83)

	def test_row(self):
		self.assertEqual(self.row,'Q273511')

	def tearDown(self):
		self.file.close()


unittest.main(verbosity=2)
