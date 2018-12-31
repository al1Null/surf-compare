### main script

from CompareValidator import CompareValidator
from CompareFormatter import CompareFormatter
from CompareMaps import CompareMaps
from CompareTimes import CompareTimes
from CompareRanks import CompareRanks

### ENTERED DATA
PLAYER1_RAW_DATA_PATH = 'raw_data/al1.txt'
PLAYER2_RAW_DATA_PATH = 'raw_data/peter.txt'

player1_name = 'al1'
player2_name = 'peter'




### VALIDATION
validator = CompareValidator(PLAYER1_RAW_DATA_PATH, PLAYER2_RAW_DATA_PATH)

is_valid = validator.isValid()
is_synced = validator.isSynced()

if is_valid and is_synced:
	print("The data of both players is valid and in sync, ready to be formatted")
else:
	raise ValueError("NOT VALID DATA")


### FORMATTING
formatter = CompareFormatter(player1_name, player2_name, PLAYER1_RAW_DATA_PATH, PLAYER2_RAW_DATA_PATH)

formatter.parseFormatData()
formatter.addPercent()
formatter.addSecond()
formatter.comparePlayersFormat()
formatter.createJSON()

# now we have the path to the formatted data, we can start comparing the maps, times, and ranks.
FORMATTED_DATA_PATH = formatter.getPath()




### MAPS COMPARE
mapsComparator = CompareMaps(FORMATTED_DATA_PATH)

# player 1
completed_maps_player1 = mapsComparator.completedMaps(1)
uncompleted_maps_player1 = mapsComparator.uncompletedMaps(1)
print()
print("{} has completed {} out of {} maps.".format(player1_name, len(completed_maps_player1), mapsComparator.TOTAL_MAPS_COUNT))
print("They are: {}".format(completed_maps_player1))

print("{} has {} map(s) to finish".format(player1_name, len(uncompleted_maps_player1)))
print("They are: {}".format(uncompleted_maps_player1))

# player 2
completed_maps_player2 = mapsComparator.completedMaps(2)
uncompleted_maps_player2 = mapsComparator.uncompletedMaps(2)
print("{} has completed {} out of {} maps.".format(player2_name, len(completed_maps_player2), mapsComparator.TOTAL_MAPS_COUNT))
print("They are: {}".format(completed_maps_player2))

print("{} has {} map(s) to finish".format(player2_name, len(uncompleted_maps_player2)))
print("They are: {}".format(uncompleted_maps_player2))

# both players
neither_completed = mapsComparator.neitherCompletedMaps()
both_completed = mapsComparator.bothCompletedMaps()
print("There are {} maps that neither player has finished".format(len(neither_completed)))
print("They are: {}".format(neither_completed))

print("There are {} maps that both players have finished".format(len(both_completed)))
print("They are: {}".format(both_completed))

unique_completed_maps_player1 = mapsComparator.uniqueCompletedMaps(1)
print("{} has completed {} maps that {} has not".format(player1_name, len(unique_completed_maps_player1), player2_name))
print("They are: {}".format(unique_completed_maps_player1))

unique_completed_maps_player2 = mapsComparator.uniqueCompletedMaps(2)
print("{} has completed {} maps that {} has not".format(player2_name, len(unique_completed_maps_player2), player1_name))
print("They are: {}".format(unique_completed_maps_player2))



### TIMES COMPARE



### RANKS COMPARE

