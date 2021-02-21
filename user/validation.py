from ui import display_message
from input_management import get_string

def menu_selection_exists():
	pass


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
