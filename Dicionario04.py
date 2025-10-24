d = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'doctor'}

print(f"original dictionary: {d}")

del d ['profession']
print(f"Updated dictionary after removing 'profession': {d}")

print("Printing all key-value pairs:")
for key, value in d.items():
    print(f"{key}: {value}")
def check_key_exists(d,chave):
    return chave in d
key1 = input('Enter the key: ')
print(f"Does '{key1}' exists? {'yes' if check_key_exists(d, key1) == True else 'no'}")

keys = ["name", "salary"]
for k in keys:
    d.pop(k)
print(d)

