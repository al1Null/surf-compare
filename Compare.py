import time
from pprint import pprint

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

	@staticmethod
	def dataArray(raw_data):

		data_array = []
		parsed_data = []

		for line in raw_data:
			if line[:5] != 'surf_':
				continue
			else:
				line = line.strip()
				parsed_data.append(line)


		for play in parsed_data:
			d = {}
			d['map'] = play.split(',')[0]
			d['time'] = play.split(',')[1][7:]
			d['rank'] = play.split(',')[2][7:]
			data_array.append(d)

		return data_array

	def getDataArray(self):
		self.data_array1 = self.dataArray(self.raw_data1)
		self.data_array2 = self.dataArray(self.raw_data2)


	def secTime(self):
		index = 0
		for entry1, entry2 in zip(self.data_array1, self.data_array2):
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
				self.data_array1[index] = entry1

				entry2['time_sec'] = time_sec2
				self.data_array2[index] = entry2

				index += 1


	def getBetter(self):
		index = 0
		for entry1, entry2 in zip(self.data_array1, self.data_array2):
			if entry1['map'] == entry2['map']:
				t1 = entry1['time_sec']
				t2 = entry2['time_sec']

				if t1 > t2:
					entry1['better'] = True
					self.data_array1[index] = entry1
					entry2['better'] = False
					self.data_array2[index] = entry2
					index += 1
				elif t2 > t1:
					entry1['better'] = False
					self.data_array1[index] = entry1
					entry2['better'] = True
					self.data_array2[index] = entry2
					index += 1
				else:
					raise ValueError("Same time?")




compare = Compare('al1', 'yogurtt', 'al1.txt', 'yogurtt.txt')
compare.getDataArray()
compare.secTime()
compare.getBetter()
pprint(compare.data_array2)