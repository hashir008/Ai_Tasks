movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

total_budget = 0
for movie in movies:
    total_budget += movie[1]

average_budget = total_budget / len(movies)

print(f"Average budget: ${average_budget:,.2f}\n")

count_above_average = 0

for title, budget in movies:
    if budget > average_budget:
        difference = budget - average_budget
        print(f"{title} is ${difference:,.2f} above the average.")
        count_above_average += 1

print(f"\nNumber of movies above average: {count_above_average}")
