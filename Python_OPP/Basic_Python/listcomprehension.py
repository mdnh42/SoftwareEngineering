numbers = [45, 87, 96, 65, 43, 90, 85, 14, 26, 61]
odds = []
for num in numbers: 
    if num%2 == 1 and num%5 == 0:
        odds.append(num)

    
print(odds)

odd_nums = [num for num in numbers if num%2 == 1 if num%5 == 0]

print(odd_nums)


players = ['Sakib', 'Musfik', 'Mustafiz', 'liton']
ages = [38, 38, 32]

age_comb = []

for player in players:
    print('player', player)
    for age in ages:
        print(player, age)
        age_comb.append([player, age])

print(age_comb)


