from ui import display_message
from input_management import get_string

def menu_selection_exists(menu, selection):
	return is_int(selection) or menu.is_valid(selection) or selection = 'x'
	pass


def is_int(test_int):
	try:
		good_int = int(test_int)
		return True
	except ValueError:
		return False


def invalid_bool(true,false,selection,message):
	while True:
		if selection == true:
			break
		elif selection == false:
			break
		else:
			display_message(f'Invalid selection. Please select {true} or {false}.')
			selection = get_string(message)

	return selection
