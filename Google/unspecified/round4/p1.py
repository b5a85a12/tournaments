import itertools

def solution(times, time_limit):
    floyd(times)
    for i in range(len(times)):
        if times[i][i]<0:
            return [x for x in range(len(times)-2)]


    for i in range(len(times)-1,0,-1):
        for permutation in itertools.permutations(range(1, len(times)-1),i):
            time = 0
            path = [0]
            path.extend(permutation)
            path.append(len(times)-1)
            for j in range(len(path)-1):
                time += times[path[j]][path[j+1]]
            if time<=time_limit:
                return sorted([x-1 for x in permutation])
    return []


def floyd(distance):
    for k in range(len(distance)):
        for i in range(len(distance)):
            for j in range(len(distance)):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])


if __name__=="__main__":
    times1 = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
    time_limit1 = 1
    times2 = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
    time_limit2 = 3
    times3 = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, -1, -1], [9, 3, 2, 0, -1], [9, 3, 2, -1, 0]]
    time_limit3 = 1
    print(solution(times1, time_limit1))
    print(solution(times2, time_limit2))
    print(solution(times3, time_limit3))

    
