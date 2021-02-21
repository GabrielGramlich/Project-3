from user.ui import display_options, display_message, get_string
from user.validation import menu_selection_exists
from database.database_management import *
from user.menu import Menu
from crud import *

def main():
	artdbmanager = ArtDatabaseManager

	main_menu = initialize_main_menu()

	while True:
		display_options(main_menu)
		selection = get_string('Which option would you like? ').upper()

		if menu_selection_exists(main_menu, selection):
			action = main_menu.get_action(selection)
			next_action = action()
			if selection == 'X':
				break
			next_action(artdbmanager)
		else:
			display_message('Not a valid choice. Please try again.')


def artist_action():
	action = None
	artist_menu = initialize_artist_menu()
	while action == None:
		action = get_action(artist_menu)

	return action


def artwork_action():
	action = None
	artwork_menu = initialize_artwork_menu()
	while action == None:
		action = get_action(artwork_menu)

	return action


def get_action(menu):
	display_options(menu)
	selection = get_string('Which option would you like? ').upper()

	if menu_selection_exists(menu, selection):
		action = menu.get_action(selection)
		return action
	else:
		display_message('Not a valid choice. Please try again.')
		return None


def initialize_main_menu():
	main_menu = Menu()
	main_menu.add_option('1', 'artist menu', artist_action)
	main_menu.add_option('2', 'artwork menu', artwork_action)
	main_menu.add_option('X', 'exit', exit)

	return main_menu


def initialize_artist_menu():
	artist_menu = Menu()
	artist_menu.add_option('1', 'create artist', create_artist)
	artist_menu.add_option('2', 'display all artists', display_all_artists)
	artist_menu.add_option('3', 'delete artist', delete_artist)
	artist_menu.add_option('4', 'update name', update_artist_name)
	artist_menu.add_option('5', 'update email', update_email)

	return artist_menu


def initialize_artwork_menu():
	artwork_menu = Menu()
	artwork_menu.add_option('1', 'create artwork', create_artwork)
	artwork_menu.add_option('2', 'display all artwork', display_all_artwok)
	artwork_menu.add_option('3', 'delete artwork', delete_artwork)
	artwork_menu.add_option('4', 'update artist', update_artist)
	artwork_menu.add_option('5', 'update name', update_artwork_name)
	artwork_menu.add_option('6', 'update price', update_price)
	artwork_menu.add_option('7', 'update availability', update_avilability)

	return artwork_menu


if __name__ == '__main__':
	main()
