import json

class Formatter():

	RAW_PATH = 'raw_data/'
	MAPS_PATH = 'maps.txt'

	def __init__(self, player1, player2):
		"""
		construct both players data, and list of all maps
		"""
		self.player1 = player1
		self.player2 = player2
		self.p1_file = Formatter.RAW_PATH + self.player1 + '.txt' 
		self.p2_file = Formatter.RAW_PATH + self.player2 + '.txt'

		### player one data
		with open(self.p1_file, 'r') as f:
			self.raw_data1 = f.readlines()

		### player two data
		with open(self.p2_file, 'r') as f:
			self.raw_data2 = f.readlines()

		### list of all maps
		with open(Formatter.MAPS_PATH, 'r') as f:
			self.maps = [map_.strip() for map_ in f.readlines()]


	@staticmethod
	def parseFormat(raw_data):
		""" 
		parses through the raw data and formats it
		"""
		formatted_data = []
		parsed_data = []

		### data is parsed
		for line in raw_data:
			if line[:5] != 'surf_':
				continue
			else:
				line = line.strip()
				parsed_data.append(line)

		### data is then formatted
		for play in parsed_data:
			d = {}
			d['map'] = play.split(',')[0]
			d['time'] = play.split(',')[1][7:]
			d['rank'] = play.split(',')[2][7:]
			formatted_data.append(d)

		return formatted_data

	def parseFormatData(self):
		""" 
		calls parseFormat() on the raw data for each player
		"""
		self.data1 = self.parseFormat(self.raw_data1)
		self.data2 = self.parseFormat(self.raw_data2)


	def addSecond(self):
		"""
		adds 'time_second' to data dict of both players
		this is needed for further analysis / comparing
		"""
		### player one's data
		index_1 = 0
		for entry in self.data1:
			### getting time in seconds
			time_sec = 0
			t = entry['time'].split(':')

			time_sec += int(t[0]) * 60  
			time_sec += int(t[1])
			time_sec += float('.' + t[2])

			### add to data dict
			entry['time_second'] = time_sec
			self.data1[index_1] = entry
			index_1 += 1

		### player two's data
		index_2 = 0
		for entry in self.data2:
			### getting time in seconds
			time_sec = 0
			t = entry['time'].split(':')

			time_sec += int(t[0]) * 60  
			time_sec += int(t[1])
			time_sec += float('.' + t[2])
			
			### add to data dict
			entry['time_second'] = time_sec
			self.data2[index_2] = entry
			index_2 += 1


	def addPercent(self):
		"""
		adds 'rank_percent' to data dict
		this is needed for further analysis / comparing
		"""
		index = 0
		for entry in self.data1:
			rank = entry['rank'].split('/')

			numerator = int(rank[0])
			denominator = int(rank[1])
			percentage = round((100 * (numerator/denominator)), 2)

			entry['rank_percent'] = percentage
			self.data1[index] = entry
			index += 1

		index = 0
		for entry in self.data2:
			rank = entry['rank'].split('/')

			numerator = int(rank[0])
			denominator = int(rank[1])
			percentage = round((100 * (numerator/denominator)), 2)

			entry['rank_percent'] = percentage
			self.data2[index] = entry
			index += 1


	def comparePlayersFormat(self):
		"""
		formats the data into a json/ dict structure
		so it can easily be compared and analyzed
		(see bottom of file for structure)
		"""
		compareData = []
		map_index = 0

		while map_index < len(self.maps):
			map_ = self.maps[map_index]
			d = {'map': map_}

			d['ranks'] = {}
			d['times'] = {}

			player1_maps = [entry['map'] for entry in self.data1]
			player2_maps = [entry['map'] for entry in self.data2]

			### PLAYER ONE
			if map_ in player1_maps:
				entry = self.data1[player1_maps.index(map_)]

				p_rank1 = {self.player1: [ entry['rank'], entry['rank_percent'] ]}
				p_time1 = {self.player1: [ entry['time'], entry['time_second'] ]}
		
				d['ranks'].update(p_rank1)
				d['times'].update(p_time1)
			else:
				d['ranks'].update({self.player1: "N/A"})
				d['times'].update({self.player1: "N/A"})

			### PLAYER TWO
			if map_ in player2_maps:
				entry = self.data2[player2_maps.index(map_)]

				p_rank2 = {self.player2: [ entry['rank'], entry['rank_percent'] ]}
				p_time2 = {self.player2: [ entry['time'], entry['time_second'] ]}

				d['ranks'].update(p_rank2)
				d['times'].update(p_time2)
			else:
				d['ranks'].update({self.player2: "N/A"})
				d['times'].update({self.player2: "N/A"})


			compareData.append(d)
			map_index += 1


		self.compareData = compareData

	def createJSON(self):
		"""
		writes neatly formatted data to a json file
		"""
		FILE_NAME = "{}&{}".format(self.player1, self.player2)
		FILE_PATH = "formatted_compares/{}.json".format(FILE_NAME)
		with open(FILE_PATH, 'w+') as fo:
			json.dump(self.compareData, fo, indent=4)
		print("Formatted JSON file has been successfully created! (Path: {})".format(FILE_PATH))

	def getPath(self):
		"""
		returns the path of the formatted json file
		"""
		FILE_NAME = "{}&{}".format(self.player1, self.player2)
		return "formatted_compares/{}.json".format(FILE_NAME)





##### FORMATTING OF DATA JSON/DICT
# {
# 	'map': 'surf_map_name',
# 	'times': {
# 		'player1': ['normal_time', 'seconds_time'],
# 		'player2': ['normal_time', 'seconds_time']
# 		},
# 	'ranks': {
# 		'player1': ['normal_rank', 'rank_percentage'],
# 		'player2': ['normal_rank', 'rank_percentage']
# 		}
# }
# 
# 'normal_time' format     - '0X:0X:0X'
# 'seconds_time' format    -  00X
# 'normal_rank' format     - '0X/0Y'
# 'rank_percentage' format -  0.0X
# 
#####