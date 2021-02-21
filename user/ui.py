def get_string(message):
	selection = input(message).lower()

	return message


def get_bool(message,true,false):
	selection = get_string(message)
	while not is_valid_bool(true,false,selection):
		display_message(f'Invalid selection. Please select {true} or {false}.')
		selection = get_string(message)
	if selection == true:
		return True
	else:
		return False


def display_options(menu):
	print(str(menu))


def display_message(message):
	print(message)


def refresh(lines):
	'''This method moves the line of the terminal being printed on up via the special character written,
	  and then prints blank spaces along the the previously written lines to wipe them out, and then moves
	  the cursor back up to begin a new series of prints. The 'lines' argument sent should be the amount
	  of lines printed by the last section of output, placing the cursor after the last command sent to
	  the terminal with only blank lines after.'''
	for i in range(lines):
		sys.stdout.write("\033[F") # Cursor up one line
	for i in range(lines):
		print(' '*60)	# Clears any previously printed characters up end of terminal line
	for i in range(lines):
		sys.stdout.write("\033[F") # Cursor up one line
	sys.stdout.flush()
