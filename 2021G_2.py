import sys

T = int(input())

for idx in range(T):
    K = int(input())
    x_list = []
    y_list = []

    lower_x = []
    upper_x = []
    lower_y = []
    upper_y = []

    for coord in range(K):
        coords = [int(c) for c in input().split(" ")]
        x_range = [coords[0], coords[2]]
        y_range = [coords[1], coords[3]]

        lower_x.append(coords[0])
        upper_x.append(coords[2])
        lower_y.append(coords[1])
        upper_y.append(coords[3])

        x_list.append(x_range)
        y_list.append(y_range)

    lower_x.sort()
    lower_y.sort()
    upper_x.sort()
    upper_y.sort()

    if K == 1:
        lwr_idx = 0
        upr_idx = 0
    elif K == 2:
        lwr_idx = 0
        upr_idx = 1
    else:
        lwr_idx = K // 2 - 1
        upr_idx = K // 2 + 1

    x_min = sys.maxsize
    ans_x = 0
    for x in range(lower_x[lwr_idx], upper_x[upr_idx] + 1):
        x_dist = 0
        for r in x_list:
            if x >= r[0] and x <= r[1]:
                x_dist += 0
            elif x > r[1]:
                x_dist += (x - r[1])
            else:
                x_dist += (r[0] - x)
        if x_min > x_dist:
            x_min = x_dist
            ans_x = x
            # print("x: ", x, "x_dist: ", x_dist)

    y_min = sys.maxsize
    ans_y = 0
    for y in range(lower_y[lwr_idx], upper_y[upr_idx] + 1):
        y_dist = 0
        for r in y_list:
            if y >= r[0] and y <= r[1]:
                y_dist += 0
            elif y > r[1]:
                y_dist += (y - r[1])
            else:
                y_dist += (r[0] - y)
        if y_min > y_dist:
            y_min = y_dist
            ans_y = y
            # print("y: ", y, "y_dist: ", y_dist)

    print("Case #{}: {} {}".format(idx + 1, ans_x, ans_y))
