from database_management import *

def crud(action):
	action()


def create_artist():
	pass


def display_all_artists():
	artists = database_management.read_rows('artists')
	for artist in artists:
		display_options(artist)
	pass


def delete_artist():
	pass


def update_artist_name():
	pass


def update_email():
	pass


def create_artwork():
	pass


def display_all_artwok():
	pass


def delete_artwork():
	pass


def update_artist():
	pass


def update_artwork_name():
	pass


def update_price():
	pass


def update_avilability():
	pass