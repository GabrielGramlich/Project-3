from ui import display_options, display_message
from input_management import get_string
from validation import menu_selection_exists
from database_management import *
from menu import Menu

def main():
	initialize_database()
	initialize_artist_table()
	intialize_artwork_table()

	main_menu = initialize_main_menu()
	artist_menu = initialize_artist_menu()
	artwork_menu = initialize_artwork_menu()

	while True:
		display_options(main_menu)
		selection = get_string('\nWhich option would you like? ').upper()

		if menu_selection_exists(selection):
			selection()
			if selection == 'x':
				break
		else:
			display_message('Not a valid choice. Please try again.')


def display_artist_menu():
	pass


def display_artist_artwork_menu():
	pass


def initialize_main_menu():
	main_menu = Menu():
	main_menu.add_option('1', 'artist menu', display_artist_menu)
	main_menu.add_option('2', 'artwork menu', display_artwork_menu)
	main_menu.add_option('X', 'exit', exit)

	return main_menu


def initialize_artist_menu():
	artist_menu = Menu()
	artist_menu.add_option('1', 'create artist', create_artist)
	artist_menu.add_option('2', 'display artist', display_artist)
	artist_menu.add_option('3', 'delete artist', delete_artist)
	artist_menu.add_option('4', 'update name', update_artist_name)
	artist_menu.add_option('5', 'update email', update_email)

	return artist_menu


def initialize_artwork_menu():
	artwork_menu = Menu()
	artwork_menu.add_option('1', 'create artwork', create_artwork)
	artwork_menu.add_option('2', 'display artwork', display_artwok)
	artwork_menu.add_option('3', 'delete artwork', delete_artwork)
	artwork_menu.add_option('4', 'update artist', update_artist)
	artwork_menu.add_option('5', 'update name', update_artwork_name)
	artwork_menu.add_option('6', 'update price', update_price)
	artwork_menu.add_option('7', 'update availability', update_avilability)

	return artwork_menu


def create_artist():
	pass


def display_artist():
	pass


def delete_artist():
	pass


def update_artist_name():
	pass


def update_email():
	pass


def create_artwork():
	pass


def display_artwok():
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


if __name__ == '__main__':
	main()
