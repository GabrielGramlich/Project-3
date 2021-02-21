class Artist:
	
	def __init__(self, db_id=0, name, email):
		self.db_id = db_id
		self.name = name
		self.email = email


	def __str__(self):
		return f'Artist: {self.name}\nEmail: {self.email}'
