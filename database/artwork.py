class Artwork:

	def __init__(self, artist, name, price, available, db_id=0):
		self.artist = artist
		self.name = name
		self.price = price
		self.available = available
		self.db_id = db_id


	def update_artist(self, new_artist):
		self.artist = new_artist


	def update_name(self, new_name):
		self.name = new_name


	def update_price(self, new_price):
		self.price = new_price


	def update_availability(self, new_availablility):
		self.available = new_available


	def __str__(self):
		return f'{self.db_id}:\nArtist: {self.artist}\nArtwork: {self.name}\nPrice: {self.price}\nAvailable: {self.available}'
