def solution(data,n):
    count = {}
    for number in data:
        count[number] = count.get(number,0)+1
    return [x for x in data if count[x]<=n ]

if __name__ == "__main__":
    a = [1,2,3]
    b = [1,2,2,3,3,3,4,5,5]
    c = [5, 10, 15, 10, 7]
    print(solution(a,0))
    print(solution(b,1))
    print(solution(c,1))
    print(solution(c,-1))
