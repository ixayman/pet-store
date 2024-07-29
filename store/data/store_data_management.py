import json


class StoreDataManagement:

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'r') as f:
                store = json.load(f)
                print(f"store loaded!")
                # if not isinstance(store, list):
                #     print("Invalid format in store.json, initializing as empty list.")
                #     return []
                return store
        except FileNotFoundError:
            print(f"File store.json not found.")
            return []
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file store.json.")
            exit(-1)

    @staticmethod
    def save_to_file(data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
            print(f"Data saved to {filename}!")
