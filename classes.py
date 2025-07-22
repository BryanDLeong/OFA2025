import pprint
from pprint import pprint

# class Smartphone:
#     def __init__(self, brand, model, storage):  # Class constructor
#         self.brand = brand  # Initializes brand
#         self.model = model  # Initializes model
#         self.storage = storage  # Initializes storage

#     def display_info(self):  # Method to display smartphone info
#         print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB")


# # Creating two objects
# #my_phone = Smartphone("Apple", "iPhone 13", ) TypeError if no default
# my_phone = Smartphone("Apple", "iPhone 13", 128)
# your_phone = Smartphone("Samsung", "Galaxy S22", 256)

# # Using a method to display info about the phones
# my_phone.display_info()  # Outputs -> Smartphone: Apple iPhone 13, Storage: 128GB
# your_phone.display_info()  # Outputs -> Smartphone: Samsung Galaxy S22, Storage: 256GB

# class book:
#     def __init__(self,title:str = "unknown",author:str = "unknown",year:int = "unknown"):
#         self.title = title
#         self.author = author
#         self.year = year

#     def describe(self):
#         print(f"Title: {self.title} Author: {self.author} Published: {self.year}")

#     def is_classic(self):
#         if self.year <1970:
#             # print(True)
#             return True

#     def __str__(self):
#         return str(self.__dict__)

# book1 = book("Animal Farm", "George Orwell", 1945)

# book1.describe()
# book1.is_classic()
# book1.__str__()

class Cat:
    def __init__(self, name):
        self.name = name

class Owner:
    def __init__(self, cat):
        self.cat = cat

    def __str__(self):
        return f"Owner of cat named {self.cat.name}"

cat1 = Cat("Whiskers")     
owner = Owner(cat1)            
#print(owner.cat.name)     
print(owner)
