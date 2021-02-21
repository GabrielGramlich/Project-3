class Artist:
	
	def __init__(self, name, email):
		self.name = name
		self.email = email


	def __str__(self):
		return f'Artist: {self.name}\nEmail: {self.email}'
