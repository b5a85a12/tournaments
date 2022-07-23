import math
import fractions

def solution(w,h,s):
    sum_value = 0 
    group_size = math.factorial(w)*math.factorial(h) 
    for fix_w in fix_set(w):
        for fix_h in fix_set(h):
            exp = 0
            for j in fix_h:
                for i in fix_w:
                    exp+= fractions.gcd(i,j)
            count = math.factorial(w)*math.factorial(h)//(ortho(fix_w)*ortho(fix_h)) 
            sum_value += count*pow(s,exp)
    return str(sum_value//group_size) 

def fix_set(n):
    base = []
    base.append([[]])
    base.append([[1]])
    for num in range(2, n+1):
        sub_part = []
        for i in range(num):
            for partition in base[i]:
                temp = [num-i]
                temp.extend(partition)
                temp = sorted(temp)
                if temp not in sub_part:
                    sub_part.append(temp)
        base.append(list(sub_part))
    return base[n]

def ortho(fix):
    base = 1
    base_dict = {}
    for item in fix:
        base *= item
        if item not in base_dict:
            base_dict[item]=1
        else:
            base_dict[item]+=1
    for count in base_dict.values():
        base *= math.factorial(count)
    return base


if __name__="__main__": 
    print(solution(2,3,4)==430)
    print(solution(2,2,2)==7)
