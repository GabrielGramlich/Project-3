from database_management import *

def crud(action):
	action()


def create_artist():
	pass


def display_all_artists():
	display_all('artists')


def delete_artist():
	display_all_artists()
	selection = ''
	while not is_int(selection):
		selection = get_string('Which artist would you like to delete? ')
	delete_row('artist', 'artist_id', selection)


def update_artist_name():
	pass


def update_email():
	pass


def create_artwork():
	pass


def display_all_artwok():
	display_all('artwork')


def delete_artwork():
	display_all_artwork()
	selection = ''
	while not is_int(selection):
		selection = get_string('Which artist would you like to delete? ')
	delete_row('artwork', 'artwork_id', selection)


def update_artist():
	pass


def update_artwork_name():
	pass


def update_price():
	pass


def update_avilability():
	pass


def display_all(table):
	items = database_management.read_rows(table)
	for item in items:
		display_options(item)
