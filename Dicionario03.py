my_dict = {'name': 'alice', 'age': 35, 'city': 'new york'}

print(f"original dictionary: {my_dict}")

my_dict['profession'] = 'doctor'
my_dict['last name'] = 'silva'
my_dict['nacionality'] = 'corean'
my_dict['hobby'] = 'play instruments'
print(f"updated dictionary after adding 'profession': {my_dict}")

my_dict['age'] = 40
my_dict['city'] = 'brasil'
print(f"updated dictionary after modification: {my_dict}")

print('city:', my_dict['city'])
