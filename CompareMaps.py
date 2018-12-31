import json

class CompareMaps():

	MAPS_PATH = 'maps.txt'
	with open(MAPS_PATH, 'r') as fo:
		maps = list(map_.strip() for map_ in fo.readlines())

	TOTAL_MAPS_COUNT = len(maps)

	def __init__(self, FORMATTED_DATA_PATH):
		""""""
		self.FORMATTED_DATA_PATH = FORMATTED_DATA_PATH

		with open(self.FORMATTED_DATA_PATH, 'r') as fo:
			self.compare_data = json.load(fo)

		### getting the names of the players
		players = list( self.compare_data[0]['ranks'].keys() )
		self.player1 = players[0]
		self.player2 = players[1]

		self.player1_completed_maps = []
		self.player2_completed_maps = []

		### finds completed maps for each player
		for entry in self.compare_data:
			if entry['ranks'][self.player1] != 'N/A':
				self.player1_completed_maps.append(entry['map'])
			if entry['ranks'][self.player2] != 'N/A':
				self.player2_completed_maps.append(entry['map'])



	def completedMaps(self, player):
		"""
		@param player (int) player 1 or 2
		"""
		# case statement
		if player == 1:
			return self.player1_completed_maps
		elif player == 2:
			return self.player2_completed_maps

	def uncompletedMaps(self, player):
		""""""
		# case statement
		if player == 1:
			uncompletedMaps = [map_ for map_ in CompareMaps.maps if map_ not in self.player1_completed_maps]
			return uncompletedMaps
		elif player == 2:
			uncompletedMaps = [map_ for map_ in CompareMaps.maps if map_ not in self.player2_completed_maps]
			return uncompletedMaps


	def neitherCompletedMaps(self):
		""""""
		neither_completed = []

		for map_ in CompareMaps.maps:
			if (map_ not in self.player1_completed_maps) and (map_ not in self.player2_completed_maps):
				neither_completed.append(map_)

		return neither_completed

	def bothCompletedMaps(self):
		""""""
		both_completed = []

		for map_ in CompareMaps.maps:
			if (map_ in self.player1_completed_maps) and (map_ in self.player2_completed_maps):
				both_completed.append(map_)

		return both_completed


	def uniqueCompletedMaps(self, player):
		""""""
		unique_completed_maps = []

		if player == 1:
			for map_ in CompareMaps.maps:
				if (map_ in self.player1_completed_maps) and (map_ not in self.player2_completed_maps):
					unique_completed_maps.append(map_)
			return unique_completed_maps

		elif player == 2:
			for map_ in CompareMaps.maps:
				if (map_ in self.player2_completed_maps) and (map_ not in self.player1_completed_maps):
					unique_completed_maps.append(map_)
			return unique_completed_maps

			
