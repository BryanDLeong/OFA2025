import random
from random import randint


# #math
# a=12
# b=4

# sum = a+b #12
# difference = a-b #8
# product = a*b #48
# quotient = a/b #3
# remainder = a%b #0
# exponent = a**b #27036

# x=10
# x +=5
# print(x)
# x -= 3
# print(x)
# x*=2
# print(x)
# x/=4
# print(x)

# x="5"
# y=3

# result = x + str(y)
# print(result)


# #lists
# foods = ["ramen", "pho", "sushi", "tacos", "noodle soup"]
# print(foods[1])


# #conditionals
# age = 18
# if age >= 18:
#     print("Yoiu can vote")
# else:
#     print("you are not old enough")

# num = 10
# if num > 0:
#     print("positive")
# elif num == 0:
#     print("zero")
# else:
#     print("negative")


# #loops
# for i in range(5):
#     print("*" * (i+1))

# for i in range(5):
#     print(str(i+1) * 5)

# #booleons
# a = True
# b = False
# print(a and not b)

# my_list = [
#     [1,2,3],
#     [4,5,6]
# ]

# print(my_list[1][1])
# print(my_list[len(my_list)-1])

# for i in range(1,21):
#     if i%3 == 0:
#         print(i)

# # break and continue
# jungle =["tiger", "gorilla","snake", "exit"]
# jungle = [random.choice(jungle),random.choice(jungle),random.choice(jungle),"exit"]

# for animal in jungle:
#     if animal == "exit":
#         print("you've escaped!")
#         break
#     elif animal == "gorilla":
#         print("you encountered a gorilla stay calm")
#         continue
#     print(f"encountered {animal} be careful")


# #functions
# def greet_customer(today_special,store):
#     print(f"Welcome to {store} store.")
#     print(f"Our special is {today_special}.")
#     print("Ask if you need anything!")
# print("Cleanup on aisle 6")
# greet_customer("pizza","a")
# greet_customer("pain","a")

# def math(num1, num2):
#     add = (num1 + num2)
#     minus = (num1 - num2)
#     multiply = (num1 * num2)
#     divide = (num1 / num2)

#     return add, minus, multiply, divide
# print(*math(3,4), sep="\n")

# def num_game(min, max, tries):
#     win = False
#     attempts = 1
#     secret_num = random.randint(min,max)
#     while win == False:
#         guess = int(input(f"guess a number between {min}-{max} within {tries} tries: "))
#         if guess == secret_num:
#             win = True
#             print("You guessed the number")
#         elif guess > secret_num:
#             print("Lower")
#         else:
#             print("Higher")
#         if attempts >= tries:
#             print("You Lose!")
#             print(f"The secret number was {secret_num}")
#             break
#         attempts +=1
# num_game(1,20,10)

# yts = []
# yts.append("a")
# yts.append("b")
# yts.append("c")
# yts.append("d")
# yts.append("e")

# for yt in yts:
#     print(yt)

# print(yts[1])
# yts[1] = yts[random.randint(1,5)]
# yts.pop(random.randint(1,5))
# print(yts)


# # list manipulation
# even = [x for x in range(1,21) if x%2==0]
# print(even)

# additional_list =[1,2,3,4,5]
# added = [add+10 for add in additional_list]
# print(added)

# age_list = [17,20,46,13,29,30,15,10]
# ages = [age for age in age_list if age<20]
# print(ages)

# while True:
#     text = input("Type 'exit' to stop: ")
#     if text == "exit":
#         print("Goodbye!")
#         break  # exit the loop
#     else:
#         print("You typed:", text)

# def pickone(list):
#     choice = random.randint(0,len(list)-1)
#     print(list[choice])

# letter = ["a","b","c"]

# pickone(letter)
# print(random.choice(letter))


# #Try and Except
# try:
#     # Code that might cause an error
#     value = int(input("Enter a number: "))
#     print("You entered:", value)
# except ValueError:
#     # Code that runs if an error happens
#     print("Oops! That was not a valid number.")

# nums = ["hello","1","69","209","","789","fghj"]
# nums2 = []

# for num in nums:
#     try:
#         nums2.append(float(num))
#     except ValueError:
#         continue

# print(sum(nums2)/len(nums2))


# #Lower()
# fruits = ["apple", "date", "cherry"]
# fruit = input("Pick a fruit: ").lower()

# if fruit in fruits:
#     print("fruit found")
# else:
#     print("fruit not found")


# #Split() and Strip()
# fruits = "apple,date,cherry"
# print(fruits.split(","))

# clean_fruit = []
# for fruit in fruits:
#     clean_fruit.append(fruit.strip())
# print(clean_fruit)


# books = [
#     ["The Hobbit", "J.R.R. Tolkien", "Fantasy"],
#     ["1984", "George Orwell", "Dystopian, Science Fiction"],
#     ["To Kill a Mockingbird", "Harper Lee", "Fiction, Drama"],
#     ["The Fellowship of the Ring", "J.R.R. Tolkien", "Fantasy, Adventure"],
#     ["Brave New World", "Aldous Huxley", "Dystopian, Science Fiction"],
#     ["Pride and Prejudice", "Jane Austen", "Romance, Classic Literature"],
# ]

# def filter_books_by_genre(target_genre):
#     matching_books = []
#     for book in books:
#         book[2].split(",")
#         if target_genre in book[2]:
#             matching_books.append(book)
#     return matching_books

# results = filter_books_by_genre("Science Fiction")
# #print(*results, sep='\n')
# for item in results:
#     print(*item)


# #Dictionary
# country_capitals = {
#   "United States": "Washington D.C.",
#   "Italy": "Naples",
#   "England": "London"
# }

# country_capitals["Japan"] = "Tokyo" # appending to dict
# country_capitals.update({"Korea":"Seoul"}) # appending to dict

# del country_capitals["Korea"] # deleting to dict

# print(country_capitals)
# print(country_capitals.get("United States"))
# print(country_capitals.keys())
# print(country_capitals.values())
# print(country_capitals.popitem()) # removes last
# print(country_capitals.pop("Italy")) # removes with key

# # print dictionary keys one by one
# for country in country_capitals:
#     print(country)

# print("----------")

# # print dictionary values one by one
# for country in country_capitals:
#     capital = country_capitals[country]
#     print(capital)

# student = {
#     "Bryan": 16,
#     "grade": "A",
# }

# print(student.keys())

# student["Bryan"] = 19
# print(student["Bryan"])
# print(student["school"])  # KeyError


# #Review
# fruits = ["apple", "banana", "cherry", "date"]
# person = {
#     "name": "Bob", 
#     "age": 25, 
#     "city": "Chicago"
# }

# print(fruits[2])
# print(person.get("age"))
# print(person["age"])

# dict = {"name": "Alice"}
# print(dict["age"])     #KeyError
# print(dict.get("age")) #prints none

# word = "hello"
# print(word.upper())

# class Dog:
#     def __init__(self, name):
#         self.name = name
    
    # def bark(self):
        # print(f"{self.name} says woof!")

# dog1 = Dog("Ella")
# dog1.bark()

# class Cat:
#     def __init__(self,name):
#         self.name = name

#     def meow(self):
#         print(self.name + " says meow!")

# cat1 = Cat("Midas")
# cat1.meow()

from PIL import Image
image = Image.open('681.png')
image.show()




