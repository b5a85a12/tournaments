failure = 'impossible'
def solution(m,f):
    m = int(m)
    f = int(f)
    generations = 0
    if m<1 or f<1:
            return failure
    while m>1 or f>1:
        if m==f or m<1 or f<1 or (m%2==0 and f%2==0):
            return failure
        elif m>f:
            [m,f,s] = transform(m,f)
            generations+=s
        else:
            [f,m,s] = transform(f,m)
            generations+=s
    return str(generations)

def transform(a,b):
    surplus = a//b
    if (a%b==0):
        surplus -=1
    a = a-surplus*b
    return [a,b,surplus]

if (__name__=="__main__"):
    print(solution('2','1')=='1')
    print(solution('4','7')=='4')
    print(solution('4','2')=='impossible')
    
