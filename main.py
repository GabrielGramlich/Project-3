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
		display_options()
		selection = get_string('\nWhich option would you like? ')
		if menu_selection_exists(selection):
			if selection == 'exit':
				break
			else:
				switch_menu(selection)
		else:
			display_message('Not a valid choice. Please try again.')


def initialize_crud_menu():
	crud_menu = Menu()
	crud_menu.add_option('1', 'create', create)
	crud_menu.add_option('2', 'read', read)
	crud_menu.add_option('3', 'update', update)
	crud_menu.add_option('4', 'delete', delete)
	crud_menu.add_option('X', 'exit', exit)
	
	return menu


def initialize_artist_menu():
	pass


def initialize_artwork_menu():
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
	is_artist = get_bool(f'Would you like to {selection} an artist or artwork? ','artist','artwork')
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
