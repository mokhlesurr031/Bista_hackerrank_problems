input_string = input()


kevin_score = 0
stuart_score = 0

for i in range(len(input_string)):
    if input_string[i] in "AEIOU":
        kevin_score += len(input_string) - i
    else:
        stuart_score += len(input_string) - i

if kevin_score == stuart_score:
    print("Draw")

if kevin_score > stuart_score:
    print("Kevin", kevin_score)

if kevin_score < stuart_score:
    print("Stuart", stuart_score)
