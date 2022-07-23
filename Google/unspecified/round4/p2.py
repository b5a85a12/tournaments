def solution(entrances, exits, path):
    syntheticClean(entrances, exits, path)
    return maxFlow(path,0, len(path)-1)

def syntheticClean(entrances, exits, path):
    synthRowN, synthColN = synthetic(entrances,path)
    synthRowX, synthColX = synthetic(exits,path)
    for row in range(len(path)):
        cntCol = 0
        for col in range(len(path[row])):
            if col in entrances:
                del path[row][col-cntCol]
                cntCol+=1
            elif col in exits:
                del path[row][col-cntCol]
                cntCol+=1
        path[row].insert(0,synthColN[row])
        path[row].append(synthColX[row])
        
    cntCol = 0
    for col in range(len(synthRowN)):
        if col in entrances:
            del synthRowN[col-cntCol]
            del synthRowX[col-cntCol]
            cntCol+=1
        elif col in exits:
            del synthRowX[col-cntCol]
            del synthRowN[col-cntCol]
            cntCol+=1
    cntRow = 0
    for i in entrances:
        del path[i-cntRow]
        cntRow+=1
    for i in exits:
        del path[i-cntRow]
        cntRow+=1
    v = 0
    for e in entrances:
        v+= synthColN[e]
    synthRowN.insert(0,v)
    v = 0
    for e in exits:
        v+= synthColN[e]
    synthRowX.insert(0,v)
    v=0
    for e in entrances:
        v+= synthColX[e]
    synthRowN.append(v)
    v=0
    for e in exits:
        v+= synthColX[e]
    synthRowX.append(v)
    path.insert(0, synthRowN)
    path.append(synthRowX)


    
def synthetic(keys, path):
    row = synthetic_row(keys,path)
    col = synthetic_col(keys, path)
    return row, col
    
def synthetic_row(keys,path):
    synthetic_row = [0 for x in range(len(path))]
    for i in keys:
        for j in range(len(path[i])):
            synthetic_row[j]+=path[i][j]
    return synthetic_row

def synthetic_col(keys, path):
    synthetic_col = [0 for x in range(len(path))]
    for row in range(len(path)):
        for col in range(len(path[row])):
            if col in keys:
                synthetic_col[row]+=path[row][col]
    return synthetic_col
    
def bfs(C, F, s, t):
        queue = [s]
        paths = {s:[]}
        if s == t:
            return paths[s]
        while queue: 
            u = queue.pop(0)
            for v in range(len(C)):
                if(C[u][v]-F[u][v]>0) and v not in paths:
                    paths[v] = paths[u]+[(u,v)]
                    if v == t:
                        return paths[v]
                    queue.append(v)
        return None

def maxFlow(C, s, t):
        n = len(C) 
        F = [[0] * n for i in range(n)]
        path = bfs(C, F, s, t)
        while path != None:
            flow = min(C[u][v] - F[u][v] for u,v in path)
            for u,v in path:
                F[u][v] += flow
                F[v][u] -= flow
            path = bfs(C, F, s, t)
        return sum(F[s][i] for i in range(n))
    



if __name__=="__main__":
    a = solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])
    b = solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    print(a)
    print(b)
