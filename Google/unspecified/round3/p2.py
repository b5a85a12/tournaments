def solution(n):
    return non_recurse(int(n))

def non_recurse(n):
    count = 0
    while n>1:
        if n%2==0:
            n = n//2
        elif n==3 or n%4 ==1:
            n = n-1
        else:
            n = n+1
        count+=1
    return count
      

if __name__=="__main__":
    print(solution('1')==0)
    print(solution('4')==2)
    print(solution('15')==5)
    print(solution('59')==8)
