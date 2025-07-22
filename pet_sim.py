class Pet:
    def __init__(
        self,
        name: str,
        animal_type: str,
        hunger: int = 0,
        starved: int = 0,
        happiness: int = 100,
        energy=100,
    ):
        self.name = name
        self.animal_type = animal_type
        self.hunger = hunger
        self.starved = starved
        self.happiness = happiness
        self.energy = energy

    def eat(self):
        if self.hunger >= 10:
            self.hunger -= 10
        else:
            self.hunger = 0
        print(f"{self.name} has eaten. Hunger is now {self.hunger}")
        return self.hunger

    def play(self):
        if self.happiness < 100:
            self.happiness += 10
        else:
            self.happiness = 100

        if self.hunger < 100:
            self.hunger += 5
        else:
            self.hunger = 100

        if self.energy >= 15:
            self.energy -= 15
        else:
            self.energy = 0

        print(f"{self.name} Played and is happier. Happiness is now {self.happiness}")
        print(f"{self.name}'s hunger has increased. Hunger is now {self.hunger}")
        print(f"{self.name}'s energy has decreased. Energy is now {self.energy}")

        return self.happiness, self.hunger, self.energy

    def status(self):
        print(
            rf"""
---- {self.name} ----
Type: {self.animal_type}
Hunger: {self.hunger}
Happiness: {self.happiness}
energy: {self.energy}
"""
        )

    def sleep(self):
        if energy < 100:
            energy += 10
        else:
            energy = 100
        print(f"{self.name}'s energy has increased. Energy is now {self.energy}")
        return self.energy

    # def is_dead(self):
    #     if self.hunger == 100 and self.starved < 5:
    #         self.starved += 1
    #         return self.starved
    #     else:
    #         self.starved = 0


pets = []


def create_pets():
    num_pets = int(input("How many Pets do you want? "))
    for i in range(num_pets):
        pet_type = input("What type of pet do you want? ")
        pet_name = input("Enter it's name: ")
        pets.append([pet_name.capitalize(), pet_type.capitalize(), 100, 0, 100, 100])


create_pets()

while True:
    print("")
    print(
        r"""What would you like to do?
1. Feed a pet
2. Play with a pet
3. Sleep with a pet
4. Check a pets status
5. Exit"""
    )

    choice1 = int(input(""))

    if choice1 == 5:
        break
    else:
        num = 1
        print("")
        print("Choose a pet")
        for pet in pets:
            print(f"{num}. {pet[0]} the {pet[1]}")
            num += 1

    choice2 = int(input(""))

    pet = Pet(
        pets[choice2 - 1][0],
        pets[choice2 - 1][1],
        pets[choice2 - 1][2],
        pets[choice2 - 1][3],
    )
    if choice1 == 1:
        pet_hunger = pet.eat()
        pets[choice2 - 1][2] = pet_hunger
    elif choice1 == 2:
        pet_happiness, pet_hunger, pet_energy = pet.play()
        pets[choice2 - 1][4] = pet_happiness
        pets[choice2 - 1][2] = pet_hunger
        pets[choice2 - 1][5] = pet_energy
    elif choice1 == 3:
        pet_energy = pet.sleep()
        pets[choice2 - 1][5] = pet_energy
    elif choice1 == 4:
        pet.status()

    # pet_starved = pet.is_dead()
    # pets[choice2 - 1][3] = pet_starved

    # if pet_starved == 5:
    #     print(f"{pets[choice2 - 1][0]} has died")
    #     pets.pop(choice2 - 1)

    # if pets == []:
    #     print("You have lost all your pets")
    #     restart = input("Would you like to create another pet? Y/N ")
    #     if restart.lower() == "y":
    #         create_pets()
    #     else:
    #         break

    for pet in pets:
        if pet[2] == 100:
            pet[3] += 1
        else:
            pet[3] = 0

        if pet[3] >= 5:
            pets.pop(pets.index(pet))
            print(f"{pet[0]} has died")

    if pets == []:
        print("You have lost all your pets")
        restart = input("Would you like to create another pet? Y/N ")
        if restart.lower() == "y":
            create_pets()
        else:
            break
