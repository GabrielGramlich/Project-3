class Artwork:

	def __init__(self, db_id, artist, name, price, available):
		self.db_id = db_id
		self.artist = artist
		self.name = name
		self.price = price
		self.available = available


	def update_availability(self, availablile):
		self.available = availablile


	def __str__(self):
		return f'Artist: {self.artist}\nArtwork: {self.name}\nPrice: {self.price}\nAvailable: {self.available}'
