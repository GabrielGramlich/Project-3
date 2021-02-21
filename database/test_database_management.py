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


	def test_user_can_input_artist(self):
		self.fail('Test not written')


	def test_user_can_input_artwork(self):
		self.fail('Test not written')


	def test_user_cannot_input_artwork_artist_doesnt_exist(self):
		self.fail('Test not written')


	def test_user_cannot_input_artist_duplicate_name(self):
		self.fail('Test not written')


	def test_user_cannot_input_artist_duplicate_email(self):
		self.fail('Test not written')


	def test_user_cannot_input_artwork_duplicate_name(self):
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
