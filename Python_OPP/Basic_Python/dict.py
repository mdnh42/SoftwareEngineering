numbers = [12, 56, 98, 78, 56, 12, 6, 98]

person = ['Kala Chan', 'Kalipur', 23, 'Student']
#key value pair 
# dicionary 
# object 
# hash table 
# overlap with set 

person1 = {'name': 'Kala Pakhi', 'address': 'kalipur', 'age':23, 'job': 'bekar'}
print(person1)
print(person1['job'])
print(person1.keys())
print(person1.values())

person1['Language'] = 'python'
del person1['name']
print(person1)

for k, v in person1.items():
    print(k, v)