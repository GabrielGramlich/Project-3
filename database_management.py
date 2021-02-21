def initialize_database():
	pass


def intialize_artist_table():
	pass


def intialize_artwork_table():
	pass


def create_row():
	pass


def read_row():
	pass


def read_rows():
	pass


def update_row(table, set_column, set_value, where_column, where_value):
	with sqlite3.connect(DATABASE) as connection:
		update = f'UPDATE {table} SET {set_column} = ? WHERE {where_column} = ?'
		connection.execute(update, (set_value,where_value))
	connection.close()


def delete_row():
	pass
