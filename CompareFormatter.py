import json

class CompareFormatter():

	MAPS_PATH = 'maps.txt'
	with open(MAPS_PATH, 'r') as f:
		maps = [map_.strip() for map_ in f.readlines()]


	def __init__(self, player1, player2, p1_file, p2_file):
		self.player1 = player1
		self.player2 = player2
		self.p1_file = p1_file
		self.p2_file = p2_file

		with open(self.p1_file, 'r') as f:
			self.raw_data1 = f.readlines()

		with open(self.p2_file, 'r') as f:
			self.raw_data2 = f.readlines()


	@staticmethod
	def parseFormat(raw_data):

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
		self.data1 = self.parseFormat(self.raw_data1)
		self.data2 = self.parseFormat(self.raw_data2)


	def addSecond(self):
		index = 0
		for entry in self.data1:
			time_sec = 0

			t = entry['time'].split(':')

			time_sec += int(t[0]) * 60  
			time_sec += int(t[1])
			time_sec += float('.' + t[2])

			entry['time_second'] = time_sec
			self.data1[index] = entry
			index += 1

		index = 0
		for entry in self.data2:
			time_sec = 0

			t = entry['time'].split(':')

			time_sec += int(t[0]) * 60  
			time_sec += int(t[1])
			time_sec += float('.' + t[2])

			entry['time_second'] = time_sec
			self.data2[index] = entry
			index += 1


	def addPercent(self):
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

		compareData = []

		map_index = 0

		while map_index < len(CompareFormatter.maps):

			map_ = CompareFormatter.maps[map_index]
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

	def createFormattedJSON(self):
		FILE_NAME = "{}&{}".format(self.player1, self.player2)
		FILE_PATH = "FormattedCompares/{}.json".format(FILE_NAME)
		with open(FILE_PATH, 'w+') as fo:
			json.dump(self.compareData, fo, indent=4)




### return an error, check each map completions of each map,
### ensure that all of them are equal
### ie if playerone is 12/438 on a map
### player2's time must be in form n/438
### --- total map completeing have to equal --

# pring compare should return one dict 
# {
# 	'map': 'surf_map_name',
# 	'times': {
# 		'player1': ['normal_time', 'seconds_time'],
# 		'player1': ['normal_time', 'seconds_time']
# 		},
# 	'ranks': {
# 		'player1': ['normal_rank', 'rank_percentage?'],
# 		'player1': ['normal_rank', 'rank_percentage?']
# 		}
# }