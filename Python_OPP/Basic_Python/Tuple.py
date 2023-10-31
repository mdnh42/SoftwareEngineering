def multiple():
    return 3, 4

print(multiple())

things = 'pen', 'tripod', 'water bottle', 'phone', 'web cam', 'sunglass'

print(things[0])
print(things[-2])
print(things[3:6])


if 'phone' in things:
    print('exist')


for item in things:
    print(item)


# things[0] = 'Wagon'

print(things)

print(len(things))

mega = ([2,3, 4], [6, 8, 9])

print(type(mega))
mega[0][1] = [1,4,6]

print(mega)


