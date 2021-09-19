T = int(input())

for idx in range(T):
    N = int(input())
    S = input()
    count = 0
    travels = [0] * N

    for i, house in enumerate(S):
        house = int(house)
        if house == 1:
            travels[i] = 0
            count += 1

            j = i + 1
            k = i

            while j < N and int(S[j]) != 1:
                travels[j] = j - i
                j += 1

            if count == 1:
                while k >= 0:
                    travels[k] = i - k
                    k -= 1

            else:
                while k > 0 and travels[k - 1] > (i - k + 1):
                    if int(S[k - 1]) == 1:
                        continue
                    travels[k - 1] = i - k + 1
                    k -= 1

    result = sum(travels)
    print("Case #{}: {}".format(idx + 1, result))
