import time
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)

class CompareFormatter():

	def __init__(self, player1, player2, p1_file, p2_file):
		self.player1 = player1
		self.player2 = player2
		self.p1_file = p1_file
		self.p2_file = p2_file

		with open(self.p1_file, 'r') as f:
			self.raw_data1 = f.readlines()

		with open(self.p2_file, 'r') as f:
			self.raw_data2 = f.readlines()

		with open("maps.txt", 'r') as f:
			self.maps = [map_.strip() for map_ in f.readlines()]

	def isValid(self):
		pass

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


	def comparePlayers(self):

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
				entry = self.data2[player1_maps.index(map_)]

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




	# def getBetter(self):
	# 	index = 0
	# 	for entry1, entry2 in zip(self.data1, self.data2):
	# 		if entry1['map'] == entry2['map']:
	# 			t1 = entry1['time_sec']
	# 			t2 = entry2['time_sec']

	# 			if t1 > t2:
	# 				entry1['better'] = True
	# 				self.data1[index] = entry1
	# 				entry2['better'] = False
	# 				self.data2[index] = entry2
	# 				index += 1
	# 			elif t2 > t1:
	# 				entry1['better'] = False
	# 				self.data1[index] = entry1
	# 				entry2['better'] = True
	# 				self.data2[index] = entry2
	# 				index += 1
	# 			else:
	# 				raise ValueError("Same time?")




compare = CompareFormatter('al1', 'yogurtt', 'al1.txt', 'yogurtt.txt')
# pprint(compare.maps)
compare.parseFormatData()
compare.addSecond()
compare.addPercent()
compare.comparePlayers()
pp.pprint(compare.compareData)

with open('compare.json', 'w+') as fo:
	fo.write(f"// {compare.player1} & {compare.player2}" + '\n')
	json.dump(compare.compareData, fo, indent=4)
	print('Done writing to json file')

exit(0)


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