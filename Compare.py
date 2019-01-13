import sys
import argparse

### importing modules
from CompareValidator import CompareValidator
from CompareFormatter import CompareFormatter

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
	validator = CompareValidator(player1, player2)

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
	formatter = CompareFormatter(player1, player2)

	formatter.parseFormatData()
	formatter.addPercent()
	formatter.addSecond()
	formatter.comparePlayersFormat()
	formatter.createJSON()

	# now we have the path to the formatted data, we can start comparing the maps, times, and ranks.
	FORMATTED_DATA_PATH = formatter.getPath() ### YAY now we can actually start comparing

	##### COMPARING ######
	### COMPARING MAPS ###

	### COMPARING TIMES ###

	### COMPARING RANKS ###

			