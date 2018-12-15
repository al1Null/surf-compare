import time
import pprint

pp = pprint.PrettyPrinter(indent=4)

class Compare():

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


	def comparePlayers(self):

		compareData = []

		for map_ in self.maps:
			d = {}
			d['map'] = map_


			for entry1, entry2 in zip(self.data1, self.data2):

				temp_d['ranks'] = {}
				temp_d['times'] = {}

				### for first player
				p_rank1 = {self.player1: [ entry1['rank'] ]}#, entry1['rank_percent'] ]}
				p_time1 = {self.player1: [ entry1['time'], entry1['time_sec'] ]}
				d['ranks'].update(p_rank1)
				temp_d['times'].update(p_time1)

				# for second player
				p_rank2 = {self.player2: [ entry2['rank'] ]}#, entry2['rank_percent'] ]}
				p_time2 = {self.player2: [ entry2['time'], entry2['time_sec'] ]}
				d['ranks'].update(p_rank2)
				temp_d['times'].update(p_time2)

			compareData.append(d)

		self.compareData = compareData



	def addSecond(self):
		index = 0
		for entry1, entry2 in zip(self.data1, self.data2):
			if entry1['map'] == entry2['map']:
				time_sec1 = 0
				time_sec2 = 0

				t1 = entry1['time'].split(':')
				t2 = entry2['time'].split(':')

				time_sec1 += int(t1[0]) * 60
				time_sec2 += int(t2[0]) * 60

				time_sec1 += int(t1[1])
				time_sec2 += int(t2[1])

				time_sec1 += float('.' + t1[2])
				time_sec2 += float('.' + t2[2])

				entry1['time_sec'] = time_sec1
				self.data1[index] = entry1

				entry2['time_sec'] = time_sec2
				self.data2[index] = entry2

				index += 1



	def addPercent(self):
		pass





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




compare = Compare('al1', 'yogurtt', 'al1.txt', 'yogurtt.txt')
# pprint(compare.maps)
compare.parseFormatData()
compare.addSecond()
pp.pprint(compare.data1)
compare.comparePlayers()
pp.pprint(compare.compareData)
exit(0)
# compare.secTime()
# compare.getBetter()


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