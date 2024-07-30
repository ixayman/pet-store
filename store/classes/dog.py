from store.classes.pet import Pet


class Dog(Pet):
    def __init__(self, id, name, age, breed, owner):
        super().__init__(id, name, "dog", age, owner)
        self.breed = breed
        self._vaccinated = False

    def __str__(self):
        return f"Dog: {self.name}, breed: {self.breed}, age: {self.age()}, owner: {self.owner}"

    def to_dict(self):
        return {
            "id": self._id,
            "name": self.name,
            "species": self.species,
            "breed": self.breed,
            "age": self.calculate_age(),
            "owner": self.owner,
            "vaccinated": self._vaccinated
        }
