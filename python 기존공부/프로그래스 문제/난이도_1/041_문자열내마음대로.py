def solution(strings, n):
    #sort를 건드려 볼까
    temp=list(zip(map(lambda x:x[n],strings),strings))
    key=[x[0] for x in temp]
    key.sort()
    diction=dict.fromkeys(key,[])
    for x in temp:
        diction[x[0]].append(x[1])
    for x in diction:
        diction[x].sort()
    return diction

solution(["sun", "bed", "car"],1)
