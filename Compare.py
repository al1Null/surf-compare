import sys
import argparse

### importing modules
from Validator import Validator
from Formatter import Formatter
from CompareMaps import CompareMaps
from CompareTimes import CompareTimes

###
# python Compare.py Albert Clark6
###

### file being run directly
if __name__ == "__main__":
	### arg parser
	parser = argparse.ArgumentParser(description="...")
	parser.add_argument('player1', type=str, help="Name of first player")
	parser.add_argument('player2', type=str, help="Name of second player")
	args = parser.parse_args()

	player1 = args.player1
	player2 = args.player2

	##### VALIDATION #####
	validator = Validator(player1, player2)

	if not validator.isValidEntries():
		sys.exit(0)

	validator.constructRawData()

	if validator.isValidData():
		print("Both players' data is valid")
	else:
		sys.exit("Data is not valid")

	if validator.isSyncedData():
		print("Data is synced between players\n")
	else:
		sys.exit("Data is not synced")

	# print(validator)


	##### FORMATTING #####
	formatter = Formatter(player1, player2)

	formatter.parseFormatData()
	formatter.addPercent()
	formatter.addSecond()
	formatter.comparePlayersFormat()
	formatter.createJSON()

	# now we have the path to the formatted data, we can start comparing the maps, times, and ranks.
	FORMATTED_DATA_PATH = formatter.getPath() ### YAY now we can actually start comparing


	##### COMPARING ######
	### MAPS COMPARE ###
	compareMaps = CompareMaps(FORMATTED_DATA_PATH)
	player1_uncompleted_maps = compareMaps.uncompletedMaps(1)
	player2_uncompleted_maps = compareMaps.uncompletedMaps(2)
	neither_completed_maps = compareMaps.neitherCompletedMaps()
	both_completed_maps = compareMaps.bothCompletedMaps()
	player1_unique_completed_maps = compareMaps.uniqueCompletedMaps(1)
	player2_unique_completed_maps = compareMaps.uniqueCompletedMaps(2)

	# Maps Compare output
	print()
	print("There are {} maps that {} has not completed\n They are: {}\n".format(len(player1_uncompleted_maps), player1, player1_uncompleted_maps))
	print("There are {} maps that {} has not completed\n They are: {}\n".format(len(player2_uncompleted_maps), player2, player2_uncompleted_maps))
	print()
	print("There are {} maps that both players have not completed\n They are: {}\n".format(len(neither_completed_maps), neither_completed_maps))
	print("There are {} maps that both players have completed\n They are: {}\n".format(len(both_completed_maps), both_completed_maps))
	print()
	print("here are {} maps that {} has completed that {} has not\n They are {}\n".format(len(player1_unique_completed_maps), player1, player2, player1_unique_completed_maps))
	print("here are {} maps that {} has completed that {} has not\n They are {}\n".format(len(player2_unique_completed_maps), player2, player1, player2_unique_completed_maps))
	print()

	### TIMES COMPARE ###
	compareTimes = CompareTimes(FORMATTED_DATA_PATH)
	shared_maps = compareTimes.getSharedMaps()
	player1_better_count = getBetterCount(player1)
	player2_better_count = getBetterCount(player2)
	

	# Times Compare output
	print("{} has a better time on {}/{} maps compared to {}".format(player1, player1_better_count, len(shared_maps), player2))
	print("{{ has a better time on {}/{} maps compared to {}".format(player2, player2_better_count, len(shared_maps), player1))

	for map_ in shared_maps:
		better_player = compareTimes.getBetterPlayer(map_)
		worse_player = compareTime.getWorsePlayer(map_)
		time_difference = compareTimes.getTimeDifference(map_, better_player)
		print("{} beat {} by {}s on {}".format(better_player, worse_player, time_differnce, map_))

	### RANKS COMPARE ###

			