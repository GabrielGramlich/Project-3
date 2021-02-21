from database.database_management import *
from user.ui import get_string
from database.artist import Artist
from database.artwork import Artwork

def create_artist(manager):
	name = get_string('What is the artist\'s name? ')
	email = get_string('What is the artist\'s email? ')
	artist = Artist(name, email)
	create_row('artist', 'name', 'email')

	return artist


def display_all_artists(manager):
	display_all(manager, 'artists')


def delete_artist(manager):
	display_all_artists()
	selection = ''
	while not is_int(selection):
		selection = get_string('Which artist would you like to delete? ')
	delete_row('artist', 'artist_id', selection)


def update_artist_name(manager):
	pass


def update_email(manager):
	pass


def create_artwork(manager):
	pass


def display_all_artwok(manager, manager):
	display_all('artwork')


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
