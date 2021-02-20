def get_string(message):
	selection = input(message).lower()

	return message


def get_bool(message,true,false):
	selection = validate_bool(true,false,input(message).lower(),message)
	if selection == true:
		return True
	else:
		return False


	return message
