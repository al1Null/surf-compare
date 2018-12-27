class CompareValidator():

	def __init__(self, player1_path, player2_path):
		self.player1_raw_data = []
		self.player2_raw_data = []

		with open(player1_path, 'r') as f:
			for line in f.readlines():
				self.player1_raw_data.append(line.strip())

		with open(player2_path, 'r') as f:
			for line in f.readlines():
				self.player2_raw_data.append(line.strip())

	def isValid(self):
		"""method ensures that both users' draw data is valid
		test by look at the first five charaters of each entry"""
		for line in self.player1_raw_data:
			if not line[0:5] == 'surf_':
				return False
			else:
				pass

		for entry in self.player2_raw_data:
			if not line[0:5] == 'surf_':
				return False
			else:
				pass

		return True

	def isSynced(self):
		"""methods tests that each entry data for both users is in sync with one-another"""
		player1s_map_completes = []
		player2s_map_completes = []
		shared_entries = []

		for entry in self.player1_raw_data:
			if entry.split(' ')[0] in [entry.split(' ')[0] for entry in self.player2_raw_data]:
				shared_entries.append(entry.split(' ')[0])


		for entry in self.player1_raw_data:
			map_ = entry.split(' ')[0]
			if map_ in shared_entries:
				denominator = entry.split('/')[-1]
				player1s_map_completes.append(denominator)


		for entry in self.player2_raw_data:
			map_ = entry.split(' ')[0]
			if map_ in shared_entries:
				denominator = entry.split('/')[-1]
				player2s_map_completes.append(denominator)


		if sorted(player1s_map_completes) == sorted(player2s_map_completes):
			return True
		else:
			return False

