#Movie recommendation
#Based on genre (type of movie) - user input
#list of movies - {lists, tuples and dictionaries}

#! name = "azubiafrica" - variable
# azubiafrica, 2023, summer - catherine
# catherine = ["azubiafrica", 2023, "summer"]
# catherine = ("azubiafrica", 2023, "summer")
# catherine = {
#     "program":"azubiafrica",
#     "year":2023,
#     "cohort":"summer"
# }

#our program to recommend based on input.

#List of movies - our database
movies = [
        (   
        "indiana jones",
        "action"
        ), #0
        (   
        "Vacation",
        "comedy"
        ), #1
    ("Matrix","sci-fi"), #3
    ("Avengers","action"),
    ("Toy Story","animation"),
        ]

# print(movies[0]) #('indiana jones', 'action')
# print(movies[0][0]) #indiana jones
# print(movies[0][1]) #action


# movie engine
def movie_recommender():
    recommended_movie = ""

    for movie_loop in movies:
        if (movie_loop[1] == genre_choice):
            recommended_movie = movie_loop[0]
        
    return recommended_movie



# user input
genre_choice = input("Enter genre: ")
print("Based on ",genre_choice," We recommend:", movie_recommender(),"movies")
