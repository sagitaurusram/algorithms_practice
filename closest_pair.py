import math

X_AXIS = 0
Y_AXIS = 1


def distance(inp_one, inp_two):
    return math.sqrt(math.pow(inp_one[0]-inp_two[0], 2) + math.pow(inp_one[1]-inp_two[1], 2))


def closest_split_pair(left_points, right_points, delta):
    n = len(left_points)
    x_bar = 0
    new_delta = 0
    i = 0
    new_points = [0, 0, 0]
    for x in range(n):
        x_bar = x_bar + left_points[x][0]
    for x in range(n):
        x_bar = x_bar + right_points[x][0]
    x_bar = x_bar / (2 * n)
    strip_points = []
    for point in left_points:
        if abs(point[0] - x_bar) <= delta:
            strip_points.append((point[0], point[1], 1))
    for point in right_points:
        if abs(point[0] - x_bar) <= delta:
            strip_points.append((point[0], point[1], 0))
    strip_points_reversed = []
    for point in strip_points:
        strip_points_reversed.append((point[1], point[0], point[2]))
    strip_points_reversed.sort()
    strip_points = []
    for point in strip_points_reversed:
        strip_points.append((point[1], point[0], point[2]))
    for point_num in range(len(strip_points)):
        i = point_num + 1
        tmp_point = (strip_points[point_num][0], strip_points[point_num][1])
        while i + point_num < (len(strip_points)) and i < point_num + 7: #i.e compare next 7 points from right strip
            tmp_next = (strip_points[i][0], strip_points[i][1])
            if distance(tmp_point, tmp_next) < delta:
                new_delta = distance(tmp_point, tmp_next)
                new_points = [tmp_point, tmp_next, new_delta]
            i = i + 1
    return new_points


def sort_points(inp_points, sort_axis):
    return 0


def closest_pair(inp_points):
    out_pair = (0, 0)
    if len(inp_points) == 3:
        pair_one = inp_points[0]
        pair_two = inp_points[1]
        pair_three = inp_points[2]
        d_one_two = distance(pair_one, pair_two)
        d_two_three = distance(pair_two, pair_three)
        d_one_three = distance(pair_one, pair_three)
    elif len(inp_points) == 2:
        return [inp_points[0], inp_points[1], distance(inp_points[0], inp_points[1])]
    else:
        n = len(inp_points)
        left_min_dist = closest_pair(inp_points[:int(n/2)])
        right_min_dist = closest_pair(inp_points[int(n/2):])
        split_min_dist = closest_split_pair(inp_points[:int(n/2)], inp_points[int(n/2):], min(left_min_dist[2], right_min_dist[2]))
        if split_min_dist[2] == 0:
            if left_min_dist[2] < right_min_dist[2]:
                return left_min_dist
            else:
                return right_min_dist
        return split_min_dist



points = [(-1, 3), (-1, -1), (1, 1), (2, 0.5), (2, -1), (3, 3), (4, 2), (4,-0.5)]
points.sort()
print(points)
solution = closest_pair(points)
print('correct answer is (1,1) and (2, 0.5)')
print('given by prog  is '+str(solution))
