num = int(input())

countries = set()

while num:
    country = input()
    countries.add(country)
    num-=1

# print(countries)
print(len(countries))