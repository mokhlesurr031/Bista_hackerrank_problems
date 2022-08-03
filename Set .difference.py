enStudent_count = int(input())
enStudents_list = set(map(int, input().split()))

frStudent_count = int(input())
frStudents_list = set(map(int, input().split()))

print(len(enStudents_list.difference(frStudents_list)))