from ui import display_options
from input_management import get_input

def main():
	while True:
		display_options()
		selection = get_input('\nWhich option would you like? ')
		if selection == 'exit':
			break
		else:
			pass



if __name__ == '__main__':
	main()