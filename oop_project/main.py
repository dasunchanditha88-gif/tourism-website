import json

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class Tourist(User):
    def __init__(self, user_id, name, email, nationality, preferences, itinerary):
        super().__init__(user_id, name, email)
        self.nationality = nationality
        self.preferences = preferences
        self.itinerary = itinerary

    def display_info(self):
        print(f"--- Tourist Profile: {self.name} ---")
        print(f"ID: {self.user_id} | Nationality: {self.nationality}")
        print(f"Interests: {', '.join(self.preferences)}")
        print(f"Current Stops: {', '.join(self.itinerary)}\n")

# --- Logic to Load and Manage Data ---

def load_tourists(file_path):
    tourist_objects = []
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for item in data['tourists']:
                # Instantiate OOP object from JSON data
                t = Tourist(
                    item['user_id'], 
                    item['name'], 
                    item['email'], 
                    item['nationality'], 
                    item['preferences'],
                    item['current_itinerary']
                )
                tourist_objects.append(t)
    except FileNotFoundError:
        print("Data file not found.")
    
    return tourist_objects

# Execution
if __name__ == "__main__":
    # Load data from the JSON file
    my_tourists = load_tourists('tourists.json')

    # Accessing methods within the OOP objects
    for tourist in my_tourists:
        tourist.display_info()
        