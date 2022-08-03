from collections import Counter


total_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
shoe_sizes_count = Counter(shoe_sizes)
total_customer = int(input())

total_income = 0

while total_customer:
    size, price = map(int, input().split())

    if shoe_sizes_count[size]:
        total_income +=price
        shoe_sizes_count[size]-=1

    total_customer-=1


print(total_income)