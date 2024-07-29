from store.data.store_data_management import StoreDataManagement


class Owner:
    def __init__(self,id, name, phone):
        self._id = id
        self.name = name
        self.phone = phone
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def remove_pet(self, pet):
        self.pets.remove(pet)

    def __str__(self):
        return f"Owner: {self.name}, pets: {self.pets}"

    def to_dict(self):
        return {
            "id": self._id,
            "name": self.name,
            "phone": self.phone,
            "pets": self.pets
        }

