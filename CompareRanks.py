import json

class CompareRanks():

	MAPS_PATH = 'maps.txt'

	def __init__(self, FORMATTED_DATA_PATH, player1, player2):
		""""""
		with open(FORMATTED_DATA_PATH, 'r') as fo:
			self.compare_data = json.load(fo)
		
		self.player1 = player1
		self.player2 = player2

		### list of maps
		with open(CompareRanks.MAPS_PATH, 'r') as fo:
			self.maps = list(map_.strip() for map_ in fo.readlines())

		### shared maps
		self.shared_maps = []
		for data_dict in self.compare_data:
			if data_dict['ranks'][self.player1] != "N/A" and data_dict['ranks'][self.player2] != "N/A":
				self.shared_maps.append(data_dict['map'])

	def getSharedMaps(self):
		"""funcion to show the maps that both players have completed
		@return
		"""
		return self.shared_maps


	def getOver50PercentileMaps(self, player):
		""""""
		over_50_percentile_maps = []
		for data in self.compare_data:
			map_ = data['map']
			if data['ranks'][player] == 'N/A':
				continue
			percentile = data['ranks'][player][1]
			if percentile > 50:
				over_50_percentile_maps.append(map_)

		return over_50_percentile_maps

	def get50PercentileMaps(self, player):
		""""""
		_50_percentile_maps = []
		for data in self.compare_data:
			map_ = data['map']
			if data['ranks'][player] == 'N/A':
				continue
			percentile = data['ranks'][player][1]
			if percentile < 50:
				_50_percentile_maps.append(map_)

		return _50_percentile_maps

	def get25PercentileMaps(self, player):
		""""""
		_25_percentile_maps = []
		for data in self.compare_data:
			map_ = data['map']
			if data['ranks'][player] == 'N/A':
				continue
			percentile = data['ranks'][player][1]
			if percentile < 25:
				_25_percentile_maps.append(map_)

		return _25_percentile_maps

	def get10PercentileMaps(self, player):
		""""""
		_10_percentile_maps = []
		for data in self.compare_data:
			map_ = data['map']
			if data['ranks'][player] == 'N/A':
				continue
			percentile = data['ranks'][player][1]
			if percentile < 10:
				_10_percentile_maps.append(map_)

		return _10_percentile_maps

	def get05PercentileMaps(self, player):
		""""""
		_05_percentile_maps = []
		for data in self.compare_data:
			map_ = data['map']
			if data['ranks'][player] == 'N/A':
				continue
			percentile = data['ranks'][player][1]
			if percentile < 5:
				_05_percentile_maps.append(map_)

		return _05_percentile_maps

	def get01PercentileMaps(self, player):
		""""""
		_25_percentile_maps = []
		for data in self.compare_data:
			map_ = data['map']
			if data['ranks'][player] == 'N/A':
				continue
			percentile = data['ranks'][player][1]
			if percentile < 1:
				_25_percentile_maps.append(map_)

		return _25_percentile_maps


	def getHalfPercentileMaps(self, player):
		""""""
		half_percentile_maps = []
		for data in self.compare_data:
			map_ = data['map']
			if data['ranks'][player] == 'N/A':
				continue
			percentile = data['ranks'][player][1]
			if percentile < 0.5:
				half_percentile_maps.append(map_)

		return half_percentile_maps

	def getPoint1PercentileMaps(self, player):
		""""""
		point_1_percentile_maps = []
		for data in self.compare_data:
			map_ = data['map']
			if data['ranks'][player] == 'N/A':
				continue
			percentile = 1 - data['ranks'][player][1]
			if percentile < 0.1:
				poin_1_percentile_maps.append(map_)

		return point_1_percentile_maps

	def getBetterPlayer(self, map_):
		""""""
		for data in self.compare_data:
			if data['map'] == map_:
				player_1_map_rank = data['ranks'][self.player1][1]
				player_2_map_rank = data['ranks'][self.player2][1]
				### this is the percentile, so we want to return the player that has the lower number
				if player_1_map_rank > player_2_map_rank:
					return self.player2 
				elif player_2_map_rank > player_1_map_rank:
					return self.player1


	def getWorsePlayer(self, map_):
		""""""
		for data in self.compare_data:
			if data['map'] == map_:
				player_1_map_rank = data['ranks'][self.player1][1]
				player_2_map_rank = data['ranks'][self.player2][1]
				### this is the percentile, so we want to return the player that has the higher number
				if player_1_map_rank > player_2_map_rank:
					return self.player1
				elif player_2_map_rank > player_1_map_rank:
					return self.player2


	def getRankDifference(self, map_):
		""""""
		for data in self.compare_data:
			if data['map'] == map_:
				player_1_map_rank = data['ranks'][self.player1][0]
				player_1_map_rank = int(player_1_map_rank.split('/')[0])
				player_2_map_rank = data['ranks'][self.player2][0]
				player_2_map_rank = int(player_2_map_rank.split('/')[0])
				difference = abs(player_1_map_rank - player_2_map_rank)
				return difference


		

