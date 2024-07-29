from flask import Flask, render_template, request, redirect, flash, url_for

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
                print(self.owners)
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
            owner = request.form.get('owner')
            if species == 'dog':
                breed = request.form.get('breed')
                dog_id = len(self.pets) + 1
                new_dog = Dog(dog_id, name, age, breed, owner)
                self.store_management.add_pet(new_dog.to_dict())
                self.store_management.save()
                print(f"Dog: {name}, Age: {age}, Owner: {owner}, Breed: {breed}")
            elif species == 'cat':
                indoor = 'indoor' in request.form
                cat_id = len(self.pets) + 1
                new_cat = Cat(cat_id, name, age, owner, indoor)
                self.store_management.add_pet(new_cat.to_dict())
                self.store_management.save()
                print(f"Cat: {name}, Age: {age}, Owner: {owner}, Indoor: {indoor}")
            return redirect(url_for('index'))

    def run(self):
        self.app.run(debug=True)


if __name__ == '__main__':
    f = FlaskManagement()
    f.run()
