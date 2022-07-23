import time

stateless_cache = {}

def solution(n,b):
    cycle = []
    n_t = n
    cycle.append(n_t)
    
    while True:
        #Cacheing for speed
        out = testKey(n_t,b)
        if out !=0:
            length = out
            break
        n_t = algorithm(n_t,b)
        if (n_t not in cycle):
            cycle.append(n_t)
        else:
            length = len(cycle)-cycle.index(n_t)
            break
    #print(cycle, cycle[cycle.index(n_t):])
    #stateless_cache[b][toKey(n,b)]= length
    return length

def algorithm(n,b):
    chars = [x for x in n]
    chars.sort()
    x_num = int("".join(chars[::-1]),b)
    y_num = int("".join(chars),b)
    z_str = "".join(base(x_num-y_num,b))
    z_str = '0'*(len(n)-len(z_str))+z_str
    return z_str

def testKey(n,b):
    key = toKey(n,b)
    if b in stateless_cache:
        if key in stateless_cache[b]:
            return stateless_cache[b][key]
    else:
        stateless_cache[b] = {}
    return 0

def toKey(n,b):
    chars = [x for x in n]
    chars.sort()
    key = int("".join(chars),b)

def base(n,b):
    e = n//b
    q = n%b
    if n==0:
        return ['0']
    elif e==0:
        return [str(q)]
    else:
        out = base(e,b)
        out.extend(str(q))
        return out

def generate_tests(k,b):
    tests = []
    for i in range(0,pow(b,k)):
        true_form = base(i,b)
        true_form.sort()
        true_form = "".join(true_form[::-1])
        if true_form not in tests:
            tests.append(true_form)
    return tests


if __name__=="__main__":
    print('1=', solution('1211',10))
    print('3=', solution('210022',3))
