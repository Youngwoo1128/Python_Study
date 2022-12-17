def solution(serial):
    answer = ''
    gender = serial[0] + serial[1]
    
    #성별
    if gender == '01':
        answer = answer + 'male/'
    else : 
        answer = answer + 'female/'
    
    #부서 
    departmant = serial[2] + serial[3]
    
    if departmant == '10':
        answer = answer + 'operation/'
        
    elif departmant == '11':
        answer = answer + 'sales/'
        
    elif departmant == '12':
        answer = answer + 'develop/'
        
    elif departmant == '13':
        answer = answer + 'finance/'
        
    elif departmant == '14':
        answer = answer + 'law/'
        
    else:
        answer = answer + 'research/'
        
    #팀
    
    team = serial[4] + serial[5]
    
    if serial[4] == '0':
        answer = answer + (serial[5] + "team/")
    else :
        answer = answer + (team + "team/")
    
    #유효성
    validNumber = int(serial[6] + serial[7])
    
    num = 0
    
    for i in range(6):
        num = num + int(serial[i])
       
    if num % 13 == validNumber: 
        answer = answer + 'valid'
    else :
        answer = answer + 'invalid'
        
    
    return answer


print(solution('02131003'))