'''Using https://pypi.org/project/multipledispatch/ to overload the row creation'''

from multipledispatch import dispatch
import sqlite3
from artwork import Artwork
from artist import Artist

DATABASE = 'art.sqlite'

def intialize_artist_table():
	with sqlite3.connect(DATABASE) as connection:
		connection.execute('CREATE TABLE IF NOT EXISTS artists (name text, email_address text)')
	connection.close()


def intialize_artwork_table():
	with sqlite3.connect(DATABASE) as connection:
		connection.execute('CREATE TABLE IF NOT EXISTS artwork (artist text, name text, price numeric, available boolean)')
	connection.close()


@dispatch(string, string, string)
def create_row(table, column1, column2):
	with sqlite3.connect(DATABASE) as connection:
		insert = f'INSERT INTO {table} values (?, ?)'
		connection.execute(insert, (column1, column2))
	connection.close()


@dispatch(string, string, string, string, string)
def create_row(table, column1, column2, column3, column4):
	with sqlite3.connect(DATABASE) as connection:
		insert = f'INSERT INTO {table} values (?, ?, ?, ?)'
		connection.execute(insert, (column1, column2, column3, column4))
	connection.close()


@dispatch(string, string, string)
def read_rows(table, where_column, where_value):
	results = []

	connection = sqlite3.connect(DATABASE)
	select = f'SELECT {columns} FROM {table} WHERE {where_column} = ?'
	rows = connection.execute(select, (where_value,))
	for row in rows:
		if table == artists:
			item = Artist(row[0],row[1])
		elif table == artwork:
			item = Artwork(row[0],row[1],row[2],row[3])
		results.append(item)
	connection.close()
	return results


@dispatch(string)
def read_rows(table):
	results = []

	connection = sqlite3.connect(DATABASE)
	select = f'SELECT * FROM {table}'
	rows = connection.execute(select)
	for row in rows:
		if table == artists:
			item = Artist(row[0],row[1])
		elif table == artwork:
			item = Artwork(row[0],row[1],row[2],row[3])
		results.append(row)
	connection.close()
	return results


def update_row(table, set_column, set_value, where_column, where_value):
	with sqlite3.connect(DATABASE) as connection:
		update = f'UPDATE {table} SET {set_column} = ? WHERE {where_column} = ?'
		connection.execute(update, (set_value,where_value))
	connection.close()


def delete_row(table, delete_column, delete_value):
	with sqlite3.connect(DATABASE) as connection:
		delete = f'DELETE FROM {table} WHERE {delete_column} = ?'
		connection.execute(delete, (delete_value, ))
	connection.close()