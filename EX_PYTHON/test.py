# 확장자 : Better Comments
## //  
## todo
## ?
## !
## *
## =======================================
def solution(strArr):
    answer = [ len(s) for s in strArr ]
    result = {}
    for a in answer:
        if a in result:
            result[a] += 1
        else:
            result[a] = 1
    return max(result.values())

print(solution(["a","bc","d","efg","hi"]))  # 2