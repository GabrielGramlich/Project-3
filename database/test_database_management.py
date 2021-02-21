import unittest
from unittest import TestCase
from database_management import *

import quiz

class TestCreatingRows(TestCase):

	test_db = 'test_artwork.db'

	@classmethod
	def setUpClass(cls):
		database_management.DATABASE = os.path.join('database', test_db)


	def setUp(self):
		self.Manager = ArtDatabaseManager
		self.clear_database()


	def test_something(self):
		self.fail('Test not written')


class TestReadingRows(TestCase):

	test_db = 'test_artwork.db'

	@classmethod
	def setUpClass(cls):
		database_management.DATABASE = os.path.join('database', test_db)


	def setUp(self):
		self.Manager = ArtDatabaseManager
		self.clear_database()


	def test_something(self):
		self.fail('Test not written')


class TestUpdatingRows(TestCase):

	test_db = 'test_artwork.db'

	@classmethod
	def setUpClass(cls):
		database_management.DATABASE = os.path.join('database', test_db)


	def setUp(self):
		self.Manager = ArtDatabaseManager
		self.clear_database()


	def test_something(self):
		self.fail('Test not written')


class TestDeletingRows(TestCase):

	test_db = 'test_artwork.db'

	@classmethod
	def setUpClass(cls):
		database_management.DATABASE = os.path.join('database', test_db)


	def setUp(self):
		self.Manager = ArtDatabaseManager
		self.clear_database()


	def test_something(self):
		self.fail('Test not written')
