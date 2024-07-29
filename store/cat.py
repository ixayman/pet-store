from store.data.store_data_management import StoreDataManagement
from store.pet import Pet


class Cat(Pet):
    def __init__(self,id, name, age, owner, indoor):
        super().__init__(id, name, "cat", age, owner)
        self.indoor = indoor
        self._vaccinated = False

    def __str__(self):
        return f"Cat: {self.name}, indoor: {self.indoor}, age: {self.age()}, owner: {self.owner}"

    def to_dict(self):
        return {
            "id": self._id,
            "name": self.name,
            "species": self.species,
            "indoor": self.indoor,
            "age": self.calculate_age(),
            "owner": self.owner,
            "vaccinated": self._vaccinated
        }

