"""
	Containers are objects which implement __contains__ method.
		Sadly i couldn't find more info about its characteristic.

		Syntax:

			<element> in <container>
"""

# Lets imagine an object which
#	represents map, with a method
#	for checking is coordinates
#	inside its boundaries

from collections import namedtuple


class Map:
    def __init__(self, width_start: float,
                 width_end: float,
                 height_start: float,
                 height_end: float):
        self.width_start = width_start
        self.width_end = width_end
        self.height_start = height_start
        self.height_end = height_end
        self._points_on_map = list()

    def __contains__(self, coordinates: namedtuple):
        width, height = coordinates
        if height > self.height_end or height < self.height_start:
            return False
        if width > self.width_end or width < self.width_start:
            return False
        return True

    def __add__(self, coordinates: namedtuple):
        """ Adding to map, always is related to
                 expanding points on it, with new
                 position
        """
        points_on_map = self._points_on_map
        return points_on_map.append(coordinates)


def mark_point_on_map(map: Map, coordinates: namedtuple):
    if coordinates in map:
        map = map + coordinates


City = namedtuple(
    "City", "x y")


width_MAX = 58.919438
width_MIN = 43.123456
height_MAX = 23.145136
height_MIN = 8.435646

warsaw = City(52.22977, 21.01178)

poland = Map(width_MIN, width_MAX,
             height_MIN, height_MAX)

print("Is Warsaw in Poland?",
      warsaw in poland)

mark_point_on_map(poland, warsaw)

print("Points on map", poland._points_on_map)

print(f"Map {poland=}")
