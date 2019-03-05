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


	def getBetterPlayer(self, map_):
		"""function gets the player with the better time on a given map
		@param map (str) - 
		@return 
		"""
		if map_ not in self.shared_maps:
			return None # players need to both have completed the map
		else:
			for data in self.compare_data:
				if map_ == data['map']:
					player_1_time = data['times'][self.player1][1]
					player_2_time = data['times'][self.player2][1]
					if player_1_time < player_2_time:
						return self.player1
					elif player_2_time < player_1_time:
						return self.player2
					else:
						return None # rare case if same time

	
	def getWorsePlayer(self, map_):
		""""""
		if map_ not in self.shared_maps:
			return None # players need to both have completed the map
		else:
			for data in self.compare_data:
				if map_ == data['map']:
					player_1_time = data['times'][self.player1][1]
					player_2_time = data['times'][self.player2][1]
					if player_1_time > player_2_time:
						return self.player1
					elif player_2_time > player_1_time:
						return self.player2
					else:
						return None # rare case if same time


	def getBetterCount(self, player):
		"""function gets the number of maps that a given player has a better time on
		@param player (str) - name of the player
		@return count (int) - number of maps
		"""
		count = 0
		for map_ in self.shared_maps:
			better_player = self.getBetterPlayer(map_)
			if better_player == player:
				count += 1
			else:
				pass

		return count



	def getTimeDifference(self, map_):
		""""""
		for data in self.compare_data:
			if data['map'] == map_:
				player_1_time = data['times'][self.player1][1]
				player_2_time = data['times'][self.player2][1]
				difference = abs(player_1_time - player_2_time)
				return difference

