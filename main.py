from pprint import pprint



def getDataArray(file_path):

	data_array = []

	with open(file_path, 'r') as f:
		parsed_data = []
		for line in f.readlines():
			if line[:5] != 'surf_':
				continue
			line = line.strip()
			parsed_data.append(line)


	for play in parsed_data:
		d = {}
		d['map'] = play.split(',')[0]
		d['time'] = play.split(',')[1][7:]
		d['rank'] = play.split(',')[2][7:]
		data_array.append(d)

	return data_array

# pprint(len(data_array))


def getMaps(raw_data_file):
	""" function gets all the current surf maps available to play on the server
	@param raw_data_file (str) - needs to be data of a player who has beaten all the maps
	"""
	with open(raw_data_file, 'r') as f:
		surf_maps = []
		for line in f.readlines():
			if line[:5] != 'surf_':
				continue
			surf_map = line.split(',')[0].strip()
			surf_maps.append(surf_map)


	with open('maps.txt', 'w+') as f:
		for map_ in surf_maps:
			f.write(map_ + '\n')

	print("'maps.txt' has been updated")


better_times_count_1 = 0
better_times_count_2 = 0

def player1_count():
	global better_times_count_1
	better_times_count_1 += 1

def player2_count():
	global better_times_count_2
	better_times_count_2 += 1


def compare(raw_data_file_1, raw_data_file_2):
	player_1_array = getDataArray(raw_data_file_1)
	player_2_array = getDataArray(raw_data_file_2)

	print(f'Player 1 has beaten {str(len(player_1_array))} maps')
	print(f'Player 2 has beaten {str(len(player_2_array))} maps')


	for entry1, entry2 in zip(player_1_array, player_2_array):
		if entry1['map'] == entry2['map']:
			t1 = entry1['time']
			t2 = entry2['time']

			# print(t1, t2)
			player1_count() if t1 < t2 else player2_count()
			

		# pprint(player_1_array)
		# pprint(player_2_array)


# getMaps('al1.txt')
compare('al1.txt', 'yogurtt.txt')

print(better_times_count_1, better_times_count_2)

### kitsune time is like 2sec faster