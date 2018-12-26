from CompareMaps import CompareMaps

def CompareRanks(CompareMaps):

	def __init__(self):
		"""we can only compare the ranks for maps that both players have completed"""
		
		super(CompareRanks, self).__init__()


	def __str__(self):
		return str(self.player1_completed_maps)

		# with open(self.COMPARE_DATA_PATH, 'r') as fo:
		# 	next(fo)
		# 	self.compare_data = json.load(fo)

		# players = list( self.compare_data[0]['ranks'].keys() )
		# self.player1 = players[0]
		# self.player2 = players[1]

		# self.player1_completed_maps = []
		# self.player2_completed_maps = []

		# for entry in self.compare_data:
		# 	if entry['ranks'][self.player1] != 'N/A':
		# 		self.player1_completed_maps.append(entry['map'])
		# 	if entry['ranks'][self.player2] != 'N/A':
		# 		self.player2_completed_maps.append(entry['map'])

		

	
c = CompareRanks(CompareMaps)
print(c)