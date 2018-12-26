import json

class CompareMaps():

	COMPARE_DATA_PATH = 'compare.json'
	MAPS_PATH = 'maps.txt'

	def __init__(self):
		with open(self.COMPARE_DATA_PATH, 'r') as fo:
			next(fo)
			self.compare_data = json.load(fo)

		players = list( self.compare_data[0]['ranks'].keys() )
		self.player1 = players[0]
		self.player2 = players[1]

		self.player1_completed_maps = []
		self.player2_completed_maps = []

		for entry in self.compare_data:
			if entry['ranks'][self.player1] != 'N/A':
				self.player1_completed_maps.append(entry['map'])
			if entry['ranks'][self.player2] != 'N/A':
				self.player2_completed_maps.append(entry['map'])

		with open(self.MAPS_PATH, 'r') as fo:
			self.maps = list(map_.strip() for map_ in fo.readlines())

	def totalCompletedMaps(self):
		"""
		@return a tuple of # of completed maps index 0 - p1, index 1 - p2
		"""
		player1_completed_maps_count = len(self.player1_completed_maps)
		player2_completed_maps_count = len(self.player2_completed_maps)

		return (player1_completed_maps_count, player2_completed_maps_count)


	def neitherCompletedMaps(self):
		""""""
		neither_completed = []

		for map_ in self.maps:
			if (map_ not in self.player1_completed_maps) and (map_ not in self.player2_completed_maps):
				neither_completed.append(map_)

		return neither_completed

	def bothCompletedMaps(self):
		""""""
		both_completed = []

		for map_ in self.maps:
			if (map_ in self.player1_completed_maps) and (map_ in self.player2_completed_maps):
				both_completed.append(map_)

		return both_completed


	def uniquePlayer1CompletedMaps(self):
		""""""
		unique_player1_completed = []

		for map_ in self.maps:
			if (map_ in self.player1_completed_maps) and (map_ not in self.player2_completed_maps):
				unique_player1_completed.append(map_)

		return unique_player1_completed


	def uniquePlayer2CompletedMaps(self):
		""""""
		unique_player2_completed = []

		for map_ in self.maps:
			if (map_ not in self.player1_completed_maps) and (map_ in self.player2_completed_maps):
				unique_player2_completed.append(map_)

		return unique_player2_completed



	def __str__(self):
		return str(self.compare_data)


if __name__ == '__main__':
	c = CompareMaps()
	print(c)
	print(c.player1)
	print(c.player2)
	print(c.totalCompletedMaps())
	print(c.neitherCompletedMaps())
	print(c.bothCompletedMaps())
