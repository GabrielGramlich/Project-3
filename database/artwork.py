class Artwork:

	def __init__(self, artist, name, price, available, db_id=0):
		self.artist = artist
		self.name = name
		self.price = price
		self.available = available
		self.db_id = db_id


	def update_availability(self, availablile):
		self.available = availablile


	def __str__(self):
		return f'{self.db_id}:\nArtist: {self.artist}\nArtwork: {self.name}\nPrice: {self.price}\nAvailable: {self.available}'
