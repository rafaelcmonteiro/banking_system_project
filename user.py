import json
# Parent Class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_details(self):
        details = {
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        }
        return json.dumps(details)