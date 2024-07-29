import json

from store.data.store_data_management import StoreDataManagement


class Pet:
    total_pets = 0

    def __init__(self, id, name, species, age, owner):
        self._id = id
        self.name = name
        self.species = species
        self.age = age
        self.owner = owner
        self._vaccinated = False
        Pet.total_pets += 1

    @property
    def vaccinated(self):
        return self._vaccinated

    @vaccinated.setter
    def vaccinated(self, value):
        self._vaccinated = value

    def calculate_age(self):
        return float(self.age) / 7.0

    def __del__(self):
        Pet.total_pets -= 1

    def __eq__(self, other):
        return self.name == other.name and self.species == other.species

