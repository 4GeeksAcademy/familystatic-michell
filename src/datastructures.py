from random import randint
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{
            "id": 1,
            "first_name": "John",
            "last_name": self.last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        },
        {
            "id": 2,
            "first_name": "Jane",
            "last_name": self.last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        },
        {
            "id": 3,
            "first_name": "Jimmy",
            "last_name": self.last_name,
            "age": 5,
            "lucky_numbers": [1]
        }]
    def _generate_id(self):
        return max([member["id"] for member in self._members], default=0) + 1
    def add_member(self, member):
        if "id" in member:
            new_member = {
                "id": member["id"],
                "first_name": member["first_name"],
                "last_name": self.last_name,
                "age": member["age"],
                "lucky_numbers": member["lucky_numbers"]
            }
        else:
            new_member = {
                "id": self._generate_id(),
                "first_name": member["first_name"],
                "last_name": self.last_name,
                "age": member["age"],
                "lucky_numbers": member["lucky_numbers"]
            }
        self._members.append(new_member)
        return new_member
    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                self._members.pop(i)
                return {"done": True}
        return {"done": False}
    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None
    def get_all_members(self):
        return self._members