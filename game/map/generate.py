


class World(object):
    """Base class for all map objects in current/generated game"""

    def __init__(self, xdim, ydim):
        self.xdim = xdim
        self.ydim = ydim
	self.tiles = list((x, y) for x in range(xdim) for y in range(ydim))
	self.size = len(self.tiles)


class Chunk(World):
    """Defines a chunk, which is a chunk of the world that will be loaded in memory. Necessary for world to be procedurally generated."""

    def __init__():
	pass
