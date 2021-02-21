from ui import display_message
from input_management import get_string

def menu_selection_exists(menu, selection):
	return menu.is_valid(selection)
	pass


def is_valid_bool(true,false,selection):
	if selection == true:
		return True
	elif selection == false:
		return True
	else:
		return False
