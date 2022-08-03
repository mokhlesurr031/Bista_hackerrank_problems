n, m = map(int, input().split())


door = ""

for i in range(n):
    cntr = ".|."

    n_mid = n//2

    if i<n_mid:
        pattern = ((2*i+1)*cntr).center(m, "-")
        door+=pattern+"\n"

    elif i==n_mid:
        pattern = "WELCOME".center(m, "-")
        door += pattern + "\n"

    else:
        pattern = ((2*(n-1-i)+1)*cntr).center(m, "-")
        door += pattern + "\n"

print(door)