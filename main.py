from ui import display_options
from input_management import get_input

def main():
	selection = ''
	display_options()
	selection = get_input('\nWhich option would you like? ')



if __name__ == '__main__':
	main()