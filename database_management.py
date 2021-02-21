def initialize_database():
	pass


def intialize_artist_table():
	pass


def intialize_artwork_table():
	pass


def create_row():
	pass


def read_row(table, where_column, where_value):
	results = []

	connection = sqlite3.connect(DATABASE)
	select = f'SELECT {columns} FROM {table} WHERE {where_column} = ?'
	rows = connection.execute(select, (where_value,))
	for row in rows:
		results.append(row)
	connection.close()
	return results


def read_rows(table):
	results = []

	connection = sqlite3.connect(DATABASE)
	select = f'SELECT * FROM {table}'
	rows = connection.execute(select)
	for row in rows:
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
