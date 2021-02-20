from ui import display_options, display_message
from input_management import get_input
from validation import menu_selection_exists

def main():
	while True:
		display_options()
		selection = get_input('\nWhich option would you like? ')
		if menu_selection_exists(selection):
			if selection == 'exit':
				break
			else:
				pass
		else:
			display_message('Not a valid choice. Please try again.')



if __name__ == '__main__':
	main()