from user.ui import display_message, get_string

def menu_selection_exists(menu, selection):
	return menu.is_valid(selection)


def is_valid_bool(true,false,selection):
	if selection == true:
		return True
	elif selection == false:
		return True
	else:
		return False


def is_int(test_int):
	try:
		good_int = int(test_int)
		return True
	except ValueError:
		return False
