import unittest
from unittest import TestCase
from database_management import *

import quiz

class TestCreatingRows(TestCase):

	test_db = 'test_artwork.db'

	@classmethod
	def setUpClass(cls):
		database_management.DATABASE = os.path.join('database', test_db)

	def test_something(self):
		self.fail('Test not written')


class TestReadingRows(TestCase):

	def test_something(self):
		self.fail('Test not written')


class TestUpdatingRows(TestCase):

	def test_something(self):
		self.fail('Test not written')


class TestDeletingRows(TestCase):

	def test_something(self):
		self.fail('Test not written')


