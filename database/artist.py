class Artist:
	
	def __init__(self, name, email):
		self.name = name
		self.author = email


	def __str__(self):
		return f'Artist: {self.name}\nEmail: {self.email}'
