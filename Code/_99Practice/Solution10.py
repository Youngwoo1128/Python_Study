def solution(text, anagram, sw):
    anagramSize = len(anagram)
    
    array = ["0"] * anagramSize
    
    convertList = list(text)
    
    pointer = 0
    
    if sw:
        while pointer < anagramSize:
            for i in anagram:
                array[i] = convertList[pointer]
            pointer += 1
            
    else:
        while pointer < anagramSize:
            for i in anagram:
                array[pointer] = convertList[i]
            pointer += 1
            
    answer = "".join(array)
    return answer


result = solution("Hello", [4, 2, 0, 1, 3], True)
print(result)