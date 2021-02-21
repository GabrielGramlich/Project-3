'''Using https://pypi.org/project/multipledispatch/ to overload the row creation'''

from multipledispatch import dispatch
import sqlite3
from database.artwork import Artwork
from database.artist import Artist
from user.ui import display_message

DATABASE = 'art.sqlite'


class ArtDatabaseError(Exception):
	pass


class ArtDatabaseManager():

	def __init__(self):
		self.initialize_artist_table()
		self.initialize_artwork_table()


	def initialize_artist_table(self):
		create_table = 'CREATE TABLE IF NOT EXISTS artists (artist_id INTEGER PRIMARY KEY, name TEXT UNIQUE, email_address TEXT UNIQUE)'
		with sqlite3.connect(DATABASE) as connection:
			connection.execute(create_table)
		connection.close()


	def initialize_artwork_table(self):
		create_table = 'CREATE TABLE IF NOT EXISTS artwork (artwork_id INTEGER PRIMARY KEY, artist TEXT, name TEXT UNIQUE, price NUMERIC, available BOOLEAN, FOREIGN KEY(artist) REFERENCES artists(name))'
		with sqlite3.connect(DATABASE) as connection:
			connection.execute(create_table)
		connection.close()


	def create_row(self, table, item):
		if table == 'artists':
			self.create_artist(table,item)
		elif table == 'artwork':
			self.create_artwork(table,item)


	def create_artist(self, table, artist):
		try:
			insert = f'INSERT INTO {table} (name, email_address) VALUES (?, ?)'
			with sqlite3.connect(DATABASE) as connection:
				connection.execute(insert, (artist.name,artist.email))
			connection.close()
		except sqlite3.IntegrityError:
			raise ArtDatabaseError('Artist already exists')


	def create_artwork(self, table, artwork):
		try:
			insert = f'INSERT INTO {table} (artist, name, price, available) VALUES (?, ?, ?, ?)'
			with sqlite3.connect(DATABASE) as connection:
				connection.execute(insert, (artwork.artist,artwork.name,artwork.price,artwork.available))
			connection.close()
		except sqlite3.IntegrityError:
			raise ArtDatabaseError('Artwork already exists')


	@dispatch(str, str, str)
	def read_rows(self, table, where_column, where_value):
		results = []

		connection = sqlite3.connect(DATABASE)
		select = f'SELECT {columns} FROM {table} WHERE UPPER({where_column}) = UPPER(?)'
		rows = connection.execute(select, (where_value,))
		for row in rows:
			if table == 'artists':
				item = Artist(row[1],row[2],row[0])
			elif table == 'artwork':
				item = Artwork(row[1],row[2],row[3],row[4],row[0])
			results.append(item)
		connection.close()
		return results


	@dispatch(str)
	def read_rows(self, table):
		results = []

		connection = sqlite3.connect(DATABASE)
		select = f'SELECT * FROM {table}'
		rows = connection.execute(select)
		for row in rows:
			if table == 'artists':
				item = Artist(row[1],row[2],row[0])
			elif table == 'artwork':
				item = Artwork(row[1],row[2],row[3],row[4],row[0])
			results.append(item)
		connection.close()
		return results


	def update_row(self, table, set_column, set_value, where_column, where_value):
		update = f'UPDATE {table} SET {set_column} = ? WHERE UPPER({where_column}) = UPPER(?)'
		with sqlite3.connect(DATABASE) as connection:
			updated = connection.execute(update, (set_value,where_value))
			rows_modified = updated.rowcount
		connection.close()

		if rows_modified == 0:
			raise ArtDatabaseError(f'Nothing modified. No entry for {where_value} under {where_column}.')


	def delete_row(self, table, delete_column, delete_value):
		delete = f'DELETE FROM {table} WHERE UPPER({delete_column}) = UPPER(?)'
		with sqlite3.connect(DATABASE) as connection:
			connection.execute(delete, (delete_value, ))
			rows_modified = updated.rowcount
		connection.close()

		if rows_modified == 0:
			raise ArtDatabaseError(f'Nothing deleted. No entry for {delete_value} under {delete_column}.')


	def clear_database(self):
		delete = f'DELETE * FROM artists'
		with sqlite3.connect(DATABASE) as connection:
			connection.execute(delete)
		connection.close()

		delete = f'DELETE * FROM artwork'
		with sqlite3.connect(DATABASE) as connection:
			connection.execute(delete)
		connection.close()
