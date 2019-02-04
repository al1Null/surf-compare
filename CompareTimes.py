import json

class CompareTimes():

	MAPS_PATH = 'maps.txt'
	
	def __init__(self, FORMATTED_DATA_PATH):
		"""
		@param FORMATTE_DATA_PATH (str) - path to the formatting data
		"""
		self.FORMATTED_DATA_PATH = FORMATTED_DATA_PATH

		with open(self.FORMATTED_DATA_PATH, 'r') as fo:
			self.compare_data = json.load(fo)

		### getting the names of the players
		players = list( self.compare_data[0]['ranks'].keys() )
		self.player1 = players[0]
		self.player2 = players[1]

		### list of maps
		with open(CompareTimes.MAPS_PATH, 'r') as fo:
			self.maps = list(map_.strip() for map_ in fo.readlines())

		### shared maps
		self.shared_maps = []
		for data_dict in self.compare_data:
			if data_dict['ranks'][self.player1] != "N/A" and data_dict['ranks'][self.player2] != "N/A":
				self.shared_maps.append(data_dict['map'])


	def getSharedMaps(self):
		"""funcion to show the maps that both players have completed
		@reeturn
		"""
		return self.shared_maps

	def getBetterCount(self, player):
		"""function gets the number of maps that a given player has a better time on
		@param player (str) - name of the player
		@return count (int) - number of maps
		"""
		pass

	def getBetterPlayer(self, map):
		"""function gets the player with the better time on a given map
		@param map (str) -
		@return 
		"""
		pass

	def getTimeDifference(self, map):
		""""""
		pass

