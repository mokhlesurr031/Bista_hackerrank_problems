inp = input()

print(any([char.isalnum() for char in inp]))
print(any([char.isalpha() for char in inp]))
print(any([char.isdigit() for char in inp]))
print(any([char.islower() for char in inp]))
print(any([char.isupper() for char in inp]))