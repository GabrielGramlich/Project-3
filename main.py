from ui import display_options, display_message
from input_management import get_string
from validation import menu_selection_exists
from database_management import *
from menu import Menu

def main():
	initialize_database()
	initialize_artist_table()
	intialize_artwork_table()

	while True:
		is_artist = get_bool(f'Would you like to the artist menu or artwork menu? ','artist','artwork')

		selection = get_string('\nWhich option would you like? ')
		if menu_selection_exists(selection):
			if selection == 'exit':
				break
			else:
				switch_menu(selection)
		else:
			display_message('Not a valid choice. Please try again.')


def initialize_artist_menu():
	artist_menu = Menu()
	artist_menu.add_option('1', 'create artist', create_artist)
	artist_menu.add_option('1', 'display artist', display_artist)
	artist_menu.add_option('1', 'delete artist', delete_artist)
	artist_menu.add_option('2', 'update name', update_artist)
	artist_menu.add_option('3', 'update email', create_artist)
	artist_menu.add_option('3', 'exit', exit)
	pass


def initialize_artwork_menu():
	artwork_menu = Menu()
	artwork_menu.add_option('1', 'create artwork', create_artwork)
	artwork_menu.add_option('1', 'display artwork', display_artwok)
	artwork_menu.add_option('2', 'delete artwork', delete_artwork)
	artwork_menu.add_option('1', 'update artist', create_artwork)
	artwork_menu.add_option('1', 'update name', create_artwork)
	artwork_menu.add_option('1', 'update price', create_artwork)
	artwork_menu.add_option('1', 'update availability', create_artwork)
	artwork_menu.add_option('3', 'exit', exit)
	pass


def switch_menu(selection):
	'''Apparently python doesn't have a switch statement, which cool, whatever,
	  but this provides a cool workaround for it. I don't know if it'll work until
	  I test it, but if not, I'll change it to a basic if-elif-else thingy.'''
	switch = {
	'create':create,
	'read':read,
	'update':update,
	'delete':delete
	}
	switch[selection](is_artist)
	'''Oh! I didn't put in the citation. It's this:
	  https://stackoverflow.com/questions/7857837/is-this-a-pythonic-method-of-executing-functions-as-a-python-switch-statement'''


def create(is_artist):
	if is_artist:
		pass
	else:
		pass


def read(is_artist):
	if is_artist:
		pass
	else:
		pass


def update(is_artist):
	if is_artist:
		pass
	else:
		pass


def delete(is_artist):
	if is_artist:
		pass
	else:
		pass


if __name__ == '__main__':
	main()
