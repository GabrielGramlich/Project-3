from ui import display_options, display_message
from input_management import get_string
from validation import menu_selection_exists
from database_management import *

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
	switch[selection]()
	'''Oh! I didn't put in the citation. It's this:
	  https://stackoverflow.com/questions/7857837/is-this-a-pythonic-method-of-executing-functions-as-a-python-switch-statement'''


def create():
	pass


def read():
	pass


def update():
	pass


def delete():
	pass


if __name__ == '__main__':
	main()