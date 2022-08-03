element_count = int(input())
elements = set(map(int, input().split()))

other_set_count = int(input())

for i in range(other_set_count):
    operation = input().split()
    items = set(map(int, input().split()))

    if operation[0] == "intersection_update":
        elements.intersection_update(items)
    if operation[0] == "update":
        elements.update(items)
    if operation[0] == "symmetric_difference_update":
        elements.symmetric_difference_update(items)
    if operation[0] == "difference_update":
        elements.difference_update(items)

print(sum(elements))