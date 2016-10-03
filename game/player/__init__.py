



class Player(object):
	"""docstring for Player"""
	def __init__(self, name):
		super(Player, self).__init__()
		
		self.name = name
		self.hp_capacity = 10
		self.hp_current = 10
		self.inventory = [item.Bread, item.Knife]
		self.pace = 1
		self.level = 1

		self.spawn = None
		