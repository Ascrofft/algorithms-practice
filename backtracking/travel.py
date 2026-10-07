class City:
    """Each Country has nine Cities."""
    def __init__(self, country, number, color):
        self.number = number
        "The number of the city (1 through 9) within this Country system."

        self.country = country
        "The Country object that this City belongs to."

        self.color = color
        "The color of this City: 'r', 'g', 'b' or 'y'."

        self.train_cities = []
        "A list of City objects to/from which train travel is possible."

    def __repr__(self):
        return self.country.name + str(self.number)

    def dump(self):
        "Print a description of the City."
        print(f"    City {self} color={self.color} train_cities={self.train_cities}")


class Country:
    """The World consists of nine Countries."""
    def __init__(self, name, city_colors, trains):
        self.name = name
        "The name of the Country. For example: 'B'."

        self.agreement_countries = []
        "A list of Country objects for which a travel agreement exists."

        self.cities = {}
        "A dictionary of City objects, keyed by the city number (1 through 9)."

        for number, color in enumerate(city_colors):
            self.cities[1+number] = City(self, 1+number, color)

        for (a, b) in trains:
            city_a = self.cities[a]
            city_b = self.cities[b]
            city_a.train_cities.append(city_b)
            city_b.train_cities.append(city_a)
    
    def __repr__(self):
        return self.name
    
    def dump(self):
        "Print a description of the `Country` and its `City`s."
        print(f"  Country {self} agreement_countries={[str(g) for g in self.agreement_countries]}")
        for p in self.cities.values():
            p.dump()


class World:
    """Creating a World object will automatically create all its Countries and Cities."""
    def __init__(self):
        data = [
            ("A", "rbyrryrry", "BCD", [(1, 2), (1, 4), (3, 6), (6, 9), (7, 8)]),
            ("B", "rryyrrbrg", "DFK", [(1, 2), (5, 6)]),
            ("C", "rrbrgbrgy", "DE", [(1, 4), (1, 2), (2, 3), (4, 7), (5, 6), (5, 8)]),
            ("D", "bbbbbbrry", "F", [(1, 4), (2, 3)]),
            ("E", "ggbryyggy", "FG", [(1, 4), (2, 3), (5, 6), (7, 8), (6, 9)]),
            ("F", "bbgrggbgg", "H", [(1, 2), (2, 3), (3, 6), (6, 9), (7, 8)]),
            ("G", "ggggyggyy", "H", [(2, 3), (4, 5), (8, 9)]),
            ("H", "yyyyggyyb", "K", [(1, 2), (2, 3), (4, 7), (5, 6), (8, 9)]),
            ("K", "yryygrybr", "", [(1, 4), (4, 7), (7, 8), (8, 9)]),
        ]

        self.countries = {}
        "A dictionary of Country objects, keyed by the Country name (like 'K')."

        for (name, city_colors, _agreements, trains) in data:
            self.countries[name] = Country(name, city_colors, trains)

        for (name, _city_colors, agreements, _trains) in data:
            for other_country_name in agreements:
                self.countries[name].agreement_countries.append(self.countries[other_country_name])
                self.countries[other_country_name].agreement_countries.append(self.countries[name])

    def dump(self):
        "Print a description of the World and its `Country`s and `City`s."
        print("World")
        for p in self.countries.values():
            p.dump()

    def find_route(self, origin, target):
        """Given an `origin` city name and `target` city name, return a list of cities
        specifying a path between the two. If there is no path, `None` is returned.

        This method does not necessarily return the shortest or fastest route, but the route
        will never include the same city twice.

        Example:
            world.find_route('C1', 'K5') → ['C1', 'C4', 'A4', 'A1', 'A2', 'D2', 'F2', 'F3', 'F6', 'H6', 'H5', 'K5']
            world.find_route('C1', 'K8') → None

        The actual work is done by the recursive _find_route_recurse() function.
        """
        origin_city = self.countries[origin[0]].cities[int(origin[1])]
        target_city = self.countries[target[0]].cities[int(target[1])]
        return _find_route_recurse(origin_city, target_city, set())


def _find_route_recurse(origin_city: City, target_city: City, visited: set):
    """The recursive functions that does the actual work of finding a path between
    `origin_city` and `target_city`. The cities in the `visited` set do not need
    to be explored again.

    Returns `None` if no path exists. Otherwise, returns a list of city names
    connecting the origin to the target.

    The _ in front of the function name indicates that the function should be considered
    'private', meaning other modules should never have to call the function directly.
    """
    if origin_city == target_city:
        return [origin_city]

    visited.add(origin_city)

    possible_cities = origin_city.train_cities.copy()

    for country in origin_city.country.agreement_countries:
        flight_city = country.cities[origin_city.number]

        if origin_city.color == flight_city.color:
            possible_cities.append(flight_city)

    for city in possible_cities:
        if city in visited:
            continue

        result = _find_route_recurse(city, target_city, visited)

        if result is not None:
            return [origin_city] + result

    return None


if __name__ == "__main__":

    world = World()
    world.dump()

    print(world.find_route('C1', 'C4')) # Only by train
    print(world.find_route('C1', 'C7')) # Only by train with a hop
    print(world.find_route('C1', 'K5')) # From here going abroad

    # One of the following may not have a possible route...
    print(world.find_route('C1', 'B1'))
    print(world.find_route('C1', 'D2'))
    print(world.find_route('C1', 'K8'))
