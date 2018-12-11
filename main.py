from pprint import pprint


data_array = []

with open('al1.txt', 'r') as f:
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




getMaps('al1.txt')