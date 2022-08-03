from collections import deque


deq = deque()

num = int(input())

while num:
    inp = input().split()

    if inp[0] == "append":
        deq.append(int(inp[1]))
    if inp[0] == "appendleft":
        deq.appendleft(int(inp[1]))
    if inp[0] == "pop":
        deq.pop()
    if inp[0] == "popleft":
        deq.popleft()

    num-=1

# print(list(deq))

for i in deq:
    print(i, end=" ")