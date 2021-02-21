class Artwork:

	def __init__(self, artist, name, price, available):
		self.artist = artist
		self.name = name
		self.price = price
		self.available = available


	def update_availability(self, availablile):
		self.available = availablile


	def __str__(self):
		return f'Artist: {self.artist}\nArtwork: {self.name}\nPrice: {self.price}\nAvailable: {self.available}'
