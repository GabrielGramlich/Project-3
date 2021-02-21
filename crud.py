from database.database_management import *
from user.ui import get_string, display_options
from database.artist import Artist
from database.artwork import Artwork
from user.validation import is_int

def create_artist(manager):
	name = get_string('What is the artist\'s name? ')
	email = get_string('What is the artist\'s email? ')
	artist = Artist(name, email)
	manager.create_row('artists', artist)

	return artist


def display_all_artists(manager):
	return display_all(manager, 'artists')


def delete_artist(manager):
	display_all_artists(manager)
	selection = ''
	while not is_int(selection):
		selection = get_string('Which artist would you like to delete? ')
	delete_row('artist', 'artist_id', selection)


def update_artist_name(manager):
	artists = display_all_artists(manager)
	selection = ''
	while not is_int(selection):
		selection = get_string('Which artist would you like to update? ')
	artist = artists[int(selection) - 1]	# Index of the artist selected
	update_value = get_string(f'What is their new name? ')
	manager.update_row('artists', 'name', update_value, 'artist_id', artist.db_id)


def update_email(manager):
	artists = display_all_artists(manager)
	selection = ''
	while not is_int(selection):
		selection = get_string('Which artist would you like to update? ')
	artist = artists[int(selection) - 1]	# Index of the artist selected
	update_value = get_string(f'What is their new email? ')
	manager.update_row('artists', 'email', update_value, 'artist_id', artist.db_id)


def create_artwork(manager):
	pass


def display_all_artwok(manager):
	return display_all('artwork')


def delete_artwork(manager):
	display_all_artwork()
	selection = ''
	while not is_int(selection):
		selection = get_string('Which artist would you like to delete? ')
	delete_row('artwork', 'artwork_id', selection)


def update_artist(manager):
	pass


def update_artwork_name(manager):
	pass


def update_price(manager):
	pass


def update_avilability(manager):
	pass


def display_all(manager, table):
	items = manager.read_rows(table)
	for item in items:
		display_options(item)

	return items
