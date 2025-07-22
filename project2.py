import csv

def calculate_average_rating(movies):
    rating_Sum = 0
    no_rating = 0
    for rate in movies:
        try:
            rating_Sum += float(rate[2])
        except ValueError:
            no_rating += 1
            continue
    #print(rating_Sum/len(movies))
    return rating_Sum/(len(movies)-no_rating)

def find_highest_rated(movies):
    rates = []
    for movie in movies:
        rates.append(movie[2])  
    #print(movies[rates.index(max(rates))][0])
    return movies[rates.index(max(rates))][0]

def filter_by_title(movies, index):
    matching = []
    title = input("What title are you looking for? ")
    for movie in movies:
        if title.lower() in movie[index].lower():
            matching.append(movie)
    #print(*matching, sep="\n")
    return matching

def filter_by_rating(movies, index):
    matching = []
    rating = input("What is the minimun rating you are looking for? ")
    for movie in movies:
        if movie[index]> rating:
            matching.append(movie)
    #print(*matching, sep="\n")
    return matching

def filter_by_genre(movies, index):
    matching = []
    genre = input("What genre are you looking for? ")

    for movie in movies:
        if genre.lower() in movie[index]:
            matching.append(movie)
    #print(*matching, sep="\n")
    return matching

data_path = '/Users/missionbit/Documents/PYTHON_MISSIONBIT/data/scifi.csv'

"""with open(data_path, 'r') as file: 
   reader = csv.reader(file) 
   for row in reader: 
      print(row)"""

"""with open(data_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows()"""

def load_movies(file):
    with open(data_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            movies.append([row[1],row[5].lower(),row[6]])
        for movie in movies:
            if movie[2] == "":
                movie[2] = "No Rating"
    movies.pop(0)

    #print(movies, sep="\n")

def save_analysis(results, filename): 
    with open(filename, 'w') as file:
        file.write(results)

def user_menu():
    menu_option = ["Title", "Genre", "Rating"]
    print("Filter through movies:")
    for option in menu_option:
        print(option)
    choice1 = input("What would you like to filter? ")
    choice2 = input("Would you like to add another filer? Y/N ")

    def search():
        data_path = '/Users/missionbit/Documents/PYTHON_MISSIONBIT/data/movie_analysis'
        if choice2 == "Y" or choice2 == "y":
            choice3 = input("What else would you like to filter? ")
            if choice1.lower() == "title" and choice3.lower() == "rating":
                title = filter_by_title(movies,0)
                ratings = filter_by_rating(title,2)
                save_analysis(str(ratings), data_path)
                print(*ratings, sep='\n')
            elif choice1.lower() == "rating" and choice3.lower() == "title":              
                ratings = filter_by_rating(movies,2)
                title = filter_by_title(ratings,0)
                save_analysis(str(title), data_path)
                print(*title, sep='\n')           
            elif choice1.lower() == "rating" and choice3.lower() == "genre":
                ratings = filter_by_rating(movies,2)
                genres = filter_by_genre(ratings,1)
                save_analysis(str(genres), data_path)
                print(*genres, sep='\n')
            elif choice1.lower() == "genre" and choice3.lower() == "rating":
                genres = filter_by_genre(movies,1)
                ratings = filter_by_rating(genres,2)
                save_analysis(str(ratings), data_path)
                print(*ratings, sep='\n')           
            elif choice1.lower() == "title" and choice3.lower() == "genre":
                title = filter_by_title(movies,0)
                genres = filter_by_genre(title,1)
                save_analysis(str(genres), data_path)
                print(*genres, sep='\n')                
            else:
                genres = filter_by_genre(movies,1)
                title = filter_by_title(genres,0)
                save_analysis(str(title), data_path)
                print(*title, sep='\n')
        else:
            if choice1.lower() == "title":
                title = filter_by_title(movies,0)
                save_analysis(str(title), data_path)
                print(*title, sep='\n')
            elif choice1.lower() == "rating":
                ratings = filter_by_rating(movies,2)
                save_analysis(str(ratings), data_path)
                print(*ratings, sep='\n')
            else:
                genres = filter_by_genre(movies,1)
                save_analysis(str(genres), data_path)
                print(*genres, sep='\n')
    search()

"""movies = [
    ["Black Panther: Wakanda Forever",
    "Action, Adventure, Drama",
    6.9],
    ["Avatar: The Way of Water",
    "Action, Adventure, Fantasy",
    7.8],
    ["Plane",
    "Action, Thriller",
    6.5]
]

if movies[0][2] > 8:
    print("Great movie!")
elif movies[0][2] > 5:
    print("Okay movie")
else:
    print("Not worth watching")

for movie in movies:
    print(f"{movie[0]} {str(movie[2])}")
"""
movies = []

load_movies(data_path)
# average_rating = calculate_average_rating(movies)
# highest_rated = find_highest_rated(movies)
# genres = filter_by_genre(movies,1)
# ratings = filter_by_rating(movies,2)
# title = filter_by_title(movies,0)


# data_path = '/Users/missionbit/Documents/PYTHON_MISSIONBIT/data/movie_analysis'
# save_analysis(str(title), data_path)

# user_menu()
# print(average_rating)
# print(highest_rated)
print(*movies, sep='\n')