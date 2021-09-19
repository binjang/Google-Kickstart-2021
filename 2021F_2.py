T = int(input())

for idx in range(T):
    # D = days total, N = number of attractions, K = number of max attractions
    D, N, K = [int(s) for s in input().split(" ")]
    days = []

    for idx2 in range(N):
        h, s, e = [int(s) for s in input().split(" ")]
        days.append([h ,s, e])
    days.sort(key = lambda x: x[0], reverse = True)

    options = []
    for i, elem in enumerate(days):
        count = 1
        sum = elem[0]
        for elem2 in range(i + 1, N):
            if len((set(range(elem[1], elem[2] + 1)) & set(range(days[elem2][1], days[elem2][2] + 1)))) > 0 and count < K:
                sum += days[elem2][0]
                count += 1
        options.append(sum)
        
    print("Case #{}: {}".format(idx + 1, sorted(options)[-1]))
