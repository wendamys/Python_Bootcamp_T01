class User:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"User(name='{self.name} age='{self.age})'"
