T = int(input())

for idx in range(T):
    # D = days total, N = number of attractions, K = number of max attractions
    N, D, C, M = [int(c) for c in input().split(" ")]
    animals = [c for c in input()]

    popable = True

    while popable and animals:
        if animals[0] == "D":
            if D > 0:
                D -= 1
                C += M
                animals.pop(0)
            else:
                popable = False
        else:
            if C > 0:
                C -= 1
                animals.pop(0)
            else:
                popable = False


    if animals == ["C"] * len(animals):
        answer = "YES"
    else: answer = "NO"

    print("Case #{}: {}".format(idx + 1, answer))
