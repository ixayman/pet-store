from store.data.store_data_management import StoreDataManagement


class StoreManagement:
    def __init__(self):
        self.owners = StoreDataManagement.load_from_file('data/owner.json')
        self.pets = StoreDataManagement.load_from_file('data/pet.json')

    def add_owner(self, owner):
        self.owners.append(owner)
        return self.owners

    def add_pet(self, pet):
        self.pets.append(pet)
        return self.pets

    def save(self):
        StoreDataManagement.save_to_file(self.owners, 'data/owner.json')
        StoreDataManagement.save_to_file(self.pets, 'data/pet.json')

    def get_owners(self):
        return self.owners

    def get_pets(self):
        return self.pets
