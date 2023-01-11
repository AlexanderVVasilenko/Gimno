import random

team1 = [round(random.randint(5, 9) + (random.randint(0, 100) / 100), 2) for _ in range(20)]
team2 = [round(random.randint(5, 9) + (random.randint(0, 100) / 100), 2) for _ in range(20)]
winners = [team1[x] if team1[x] > team2[x] else team2[x] for x in range(20)]

print(f"Первая команда: {team1}")
print(f"Вторая команда: {team2}")
print(f"Победители тура: {winners}")
