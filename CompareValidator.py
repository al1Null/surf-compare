import os

class CompareValidator():
	"""
	Validates the
	"""
	PATH = 'raw_data/'

	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		pass


	def isValidEntries(self):
		"""
		checks the raw_data/ dir to see if both players' data files are there
		"""
		file_names = os.listdir(CompareValidator.PATH)
		names = [name.lower()[:-4] for name in file_names]
		
		not_founds = []
		if self.player1.lower() not in names:
			not_founds.append(self.player1)	
		
		if self.player2.lower() not in names:
			not_founds.append(self.player2)

		if len(not_founds) == 0:
			return True
		else:
			for player in not_founds:
				print(player + "'s data file is not found in 'raw_data/' directory. \nDouble check that it's there, and that it was entered correctly.")
			return False

	def constructRawData(self):
		"""

		can only be run after isValidEntries() is True
		"""
		self.player1_raw_data = []
		self.player2_raw_data = []
		PLAYER1_PATH = CompareValidator.PATH + self.player1 + '.txt'
		PLAYER2_PATH = CompareValidator.PATH + self.player2 + '.txt'

		with open(PLAYER1_PATH, 'r') as f:
			for line in f.readlines():
				self.player1_raw_data.append(line.strip())

		with open(PLAYER2_PATH, 'r') as f:
			for line in f.readlines():
				self.player2_raw_data.append(line.strip())

	def isValidData(self):
		"""method ensures that both users' draw data is valid
		test by look at the first five charaters of each entry"""
		### player 1
		for line in self.player1_raw_data:
			if not line[0:5] == 'surf_':
				return False
			else:
				pass

		### player 2
		for entry in self.player2_raw_data:
			if not line[0:5] == 'surf_':
				return False
			else:
				pass

		### if all passes
		return True

	def isSyncedData(self):
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

	# def __str__(self):
	# 	""" """
	# 	s1 = self.isValidEntries()
	# 	s2 = self.isValidData()
	# 	s3 = self.isSyncedData()

	# 	return """
	# isValidEntries() --> %r
	# isValidData()    --> %r
	# isSyncedDat()    --> %r
	# 	""" % (s1, s2, s3)

