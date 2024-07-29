from flask import Flask, render_template, request, redirect, url_for

from store.owner import Owner
from store.dog import Dog
from store.cat import Cat
from store.store_management import StoreManagement


class FlaskManagement:
    def __init__(self):
        self.store_management = StoreManagement()
        self.owners = self.store_management.owners
        self.pets = self.store_management.pets
        self.app = Flask(__name__, template_folder='templates')
        self.app.secret_key = '10/10uncrackable-key'
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html', owners=self.owners, pets=self.pets)

        @self.app.route('/add_owner', methods=['GET', 'POST'])
        def add_owner():
            if request.method == 'POST':
                name = request.form['name']
                phone = request.form['phone']
                owner_id = len(self.owners) + 1
                new_owner = Owner(owner_id, name, phone)
                self.store_management.add_owner(new_owner.to_dict())
                self.store_management.save()
                return redirect(url_for('index'))
            return render_template('add_owner.html')

        @self.app.route('/add_pet', methods=['GET'])
        def add_pet():
            return render_template('add_pet.html')

        @self.app.route('/species_form', methods=['GET'])
        def species_form():
            species = request.args.get('species')
            if species == 'dog':
                return redirect(url_for('add_dog'))
            elif species == 'cat':
                return redirect(url_for('add_cat'))
            else:
                return redirect(url_for('add_pet'))

        @self.app.route('/add_dog')
        def add_dog():
            return render_template('add_dog.html')

        @self.app.route('/add_cat')
        def add_cat():
            return render_template('add_cat.html')

        @self.app.route('/submit_pet', methods=['GET', 'POST'])
        def submit_pet():
            species = request.form.get('species')
            name = request.form.get('name')
            age = request.form.get('age')
            owner = "None"
            if species == 'dog':
                breed = request.form.get('breed')
                dog_id = len(self.pets) + 1
                new_dog = Dog(dog_id, name, age, breed, owner)
                self.store_management.add_pet(new_dog.to_dict())
                self.store_management.save()
            elif species == 'cat':
                indoor = 'indoor' in request.form
                cat_id = len(self.pets) + 1
                new_cat = Cat(cat_id, name, age, owner, indoor)
                self.store_management.add_pet(new_cat.to_dict())
                self.store_management.save()
            return redirect(url_for('index'))

        @self.app.route('/link_pet', methods=['GET', 'POST'])
        def link_pet():
            owner_id = request.args.get('owner')
            owner_id = int(owner_id)
            print(owner_id)
            return render_template('link_pet.html', owners=self.owners, owner_id=owner_id, pets=self.pets)

        @self.app.route('/link_pet_to_owner')
        def link_pet_to_owner():
            pet_id = request.args.get('pet_id')
            owner_id = request.args.get('owner_id')

            if pet_id and owner_id:
                pet_id = int(pet_id)
                owner_id = int(owner_id)

                # Find the pet and owner
                pet = next((pet for pet in self.pets if pet['id'] == pet_id), None)
                owner = next((owner for owner in self.owners if owner['id'] == owner_id), None)

                if pet and owner:
                    # Update the pet's owner
                    pet['owner'] = owner['id']
                    # Add the pet to the owner's pets
                    owner['pets'].append(pet["id"])
                    self.store_management.save()
                    # Redirect back to the link_pet route with the updated information
                    return redirect(url_for('link_pet', owner=owner_id))
                else:
                    return "Pet or Owner not found", 404
            else:
                return "Pet ID or Owner ID not provided", 400

        @self.app.route('/unlink_pet_from_owner')
        def unlink_pet_from_owner():
            pet_id = request.args.get('pet_id')
            owner_id = request.args.get('owner_id')
            if pet_id and owner_id:
                pet_id = int(pet_id)
                owner_id = int(owner_id)
                # Find the pet and owner
                pet = next((pet for pet in self.pets if pet['id'] == pet_id), None)
                owner = next((owner for owner in self.owners if owner['id'] == owner_id), None)
                if pet and owner:
                    # Update the pet's owner
                    pet['owner'] = None
                    # Remove the pet from the owner's pets
                    if pet["id"] in owner['pets']:
                        owner['pets'].remove(pet["id"])
                    self.store_management.save()
                    # Redirect back to the link_pet route with the updated information
                    return redirect(url_for('link_pet', owner=owner_id))
                else:
                    return "Pet or Owner not found", 404
            else:
                return "Pet ID or Owner ID not provided", 400

        @self.app.route('/remove_owner')
        def remove_owner():
            owner_id = request.args.get('owner')
            if owner_id:
                owner_id = int(owner_id)
                # Remove the owner from the owners list
                for owner in self.owners:
                    if owner['id'] == owner_id:
                        self.owners.remove(owner)
                # Update pets to remove the owner_id
                for pet in self.pets:
                    if pet['owner'] == owner_id:
                        pet['owner'] = None
                self.store_management.save()
                # Redirect back to the page showing updated information
                return redirect(url_for('index'))
            else:
                return "Owner ID not provided", 400

        @self.app.route('/remove_pet')
        def remove_pet():
            pet_id = request.args.get('pet')
            if pet_id:
                pet_id = int(pet_id)
                # Remove the pet from the pets list
                for pet in self.pets:
                    if pet['id'] == pet_id:
                        if pet['owner']:
                            # Update the owner's pets list
                            for owner in self.owners:
                                if owner['id'] == pet['owner']:
                                    owner['pets'].remove(pet["id"])
                        self.pets.remove(pet)
                self.store_management.save()
                # Redirect back to the page showing updated information
                return redirect(url_for('index'))
            else:
                return "Pet ID not provided", 400

    def run(self):
        self.app.run(debug=True)


if __name__ == '__main__':
    app = FlaskManagement()
    app.run()
