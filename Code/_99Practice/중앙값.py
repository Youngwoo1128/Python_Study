"""
중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 
예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 정수 배열 array가 매개변수로 주어질 때, 
중앙값을 return 하도록 solution 함수를 완성해보세요.

[1, 2, 7, 10, 11] -> 7
[9, -1, 0] -> 0

1. 배열을 받고 정렬한다.
2. 가장 가운데에 있는 index 값을 리턴한다.


"""

answerArray = [1, 2, 3, 4, 5]

for i in range(len(answerArray) - 1, 0, -1) :
    for j in range(i):
        if (answerArray[j] > answerArray[j + 1]):
            temp = answerArray[j]
            answerArray[j] = answerArray[j + 1]
            answerArray[j + 1] = temp
        else: continue

index = len(answerArray) // 2
print(answerArray[index])

#  다른 방법
answerArray.sort()
print(answerArray[len(answerArray) // 2])