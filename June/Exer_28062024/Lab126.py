class Car:
    name = None
    password = "123"


    def __init__(self):
        print("I am called when object is created")


    def change_password(self):
        self.password = "456"


