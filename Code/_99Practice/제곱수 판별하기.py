"""
어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 
정수 n이 매개변수로 주어질 때, 
n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.
144 -> 1
976 -> 2
"""

param = 144
answer = 0
string = str(param**(1/2))

if string[len(string) - 1] == '0' :
    answer = 1
else :
    answer = 2

print(answer)

one = 1
print(one.is_integer())