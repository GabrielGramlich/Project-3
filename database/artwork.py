class Artwork:

	def __init__(self, artist, name, price, available):
		self.db_id = 0
		self.artist = artist
		self.name = name
		self.price = price
		self.available = available


	def update_availability(self, availablile):
		self.available = availablile


	def update_id(self, db_id):
		self.db_id = db_id


	def __str__(self):
		return f'Artist: {self.artist}\nArtwork: {self.name}\nPrice: {self.price}\nAvailable: {self.available}'
