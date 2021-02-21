class Artist:
	
	def __init__(self, name, email, db_id=0):
		self.name = name
		self.email = email
		self.db_id = db_id


	def __str__(self):
		return f'Artist: {self.name}\nEmail: {self.email}'
