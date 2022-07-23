def solution(l):
    out_sum = 0
    counter = [0 for x in range(0,len(l))]
    for i in range(0,len(l)):
        for j in range(0,i):
            if l[i]%l[j] == 0:
                counter[i]+=1
                out_sum += counter[j]
                
    return out_sum

if __name__ == "__main__":
    list1 = [1,1,1]
    list2 = [1,2,3,4,5,6]
    list3 = [2,3,4]
    list4 = [1,1,1,1,1]
    list5 = [2,3,4,1,2]
    list6 = [4,3,2,1,2,4]
    print(solution(list1))
    print(solution(list2))
    print(solution(list3))
    print(solution(list4))
    print(solution(list5))
    print(solution(list6))
