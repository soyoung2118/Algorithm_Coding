def solution(survey, choices):
    scores = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}    
    
    score_map = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    
    for i in range(len(survey)):
        first, second = survey[i][0], survey[i][1]  # 비동의, 동의
        choice = choices[i]
        
        if choice < 4:  # 비동의 
            scores[first] += score_map[choice]
        elif choice > 4:  # 동의
            scores[second] += score_map[choice]
    
    answer = ""
    
    if scores["R"] >= scores["T"]:
        answer += "R"
    else: 
        answer += "T"
    
    if scores["C"] >= scores["F"]:
        answer += "C"  
    else: 
        answer += "F"
    
    if scores["J"] >= scores["M"]:
        answer += "J"  
    else: 
        answer += "M"
    
    if scores["A"] >= scores["N"]:
        answer += "A"  
    else: 
        answer += "N"
    
    return answer


