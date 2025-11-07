# 확장자 : Better Comments
## //  
## todo
## ?
## !
## *
## =======================================
def solution(s):
    ret = []
    result = []
    for i in s:
        ret.append(s.count(i))
    for idx, n in enumerate(ret):
        if n == 1:
            result.append(s[idx])
    result.sort()
    return ''.join(result)

print(solution("hello"))  # 2