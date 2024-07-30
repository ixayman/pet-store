class Pet:

    def __init__(self, id, name, species, age, owner):
        self._id = id
        self.name = name
        self.species = species
        self.age = age
        self.owner = owner
        self._vaccinated = False

    @property
    def id(self):
        return self._id

    @property
    def vaccinated(self):
        return self._vaccinated

    @vaccinated.setter
    def vaccinated(self, value):
        self._vaccinated = value

    def calculate_age(self):
        return float(self.age) * 7.0

    def __eq__(self, other):
        return self.name == other.name and self.species == other.species
