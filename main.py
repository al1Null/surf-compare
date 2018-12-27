### main script

from CompareValidator import CompareValidator
from CompareFormatter import CompareFormatter
from CompareMaps import CompareMaps
from CompareTimes import CompareTimes
from CompareRanks import CompareRanks

### ENTERED DATA
PLAYER1_RAW_DATA_PATH = 'raw_data/terry.txt'
PLAYER2_RAW_DATA_PATH = 'raw_data/jacket.txt'

PLAYER1_NAME = 'Terry'
PLAYER2_NAME = 'Jacket'

### VALIDATION
validator = CompareValidator(PLAYER1_RAW_DATA_PATH, PLAYER2_RAW_DATA_PATH)

is_valid = validator.isValid()
is_synced = validator.isSynced()

if is_valid and is_synced:
	print("The data of both players is valid and in sync, ready to be formatted")
else:
	raise ValueError("NOT VALID DATA")


### FORMATTING
formatter = CompareFormatter(PLAYER1_NAME, PLAYER2_NAME, PLAYER1_RAW_DATA_PATH, PLAYER2_RAW_DATA_PATH)

formatter.parseFormatData()
formatter.addPercent()
formatter.addSecond()
formatter.comparePlayersFormat()
formatter.createFormattedJSON()

print(formatter)


