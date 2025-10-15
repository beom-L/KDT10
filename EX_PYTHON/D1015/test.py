def solution(babbling):
    answer = 0
    ong_r = ["aya", "ye", "woo", "ma"]
    
    for bab in babbling:

        for ong in ong_r:
            bab = bab.replace(ong,'')
        if len(bab) == 0:
            answer += 1
            
    return answer

print(solution(input()))