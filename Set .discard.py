n = int(input())
s = set(map(int, input().split()))

commands = int(input())

while commands:
    inp = input().split()

    if inp[0] == "pop":
        s.pop()

    if inp[0] == "remove":
        s.remove(int(inp[1]))

    if inp[0] == "discard":
        s.discard(int(inp[1]))

    commands-=1


print(sum(s))


