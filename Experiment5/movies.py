# Input number of movies
n = int(input("Enter number of movies: "))
movies = {}

for i in range(n):
    print(f"\nEnter details for movie {i+1}")
    
    name = input("Movie name: ")
    year = int(input("Release year: "))
    director = input("Director name: ")
    cost = float(input("Production cost: "))
    collection = float(input("Collection made: "))
    
    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }
print("\n--- All Movie Details ---")
for name, details in movies.items():
    print(f"\nMovie Name: {name}")
    print("Year:", details["year"])
    print("Director:", details["director"])
    print("Production Cost:", details["cost"])
    print("Collection:", details["collection"])


print("\n--- Movies Released Before 2015 ---")
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)

print("\n--- Movies That Made Profit ---")
for name, details in movies.items():
    if details["collection"] > details["cost"]:
        print(name)

director_name = input("\nEnter director name to search: ")

print(f"\n--- Movies Directed by {director_name} ---")
for name, details in movies.items():
    if details["director"].lower() == director_name.lower():
        print(name)
