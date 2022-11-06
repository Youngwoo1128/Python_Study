"""
2차원 리스트 
똑같음
"""
person_info = [
    ["유재석", 51, "남"],
    ["노홍철", 74, "남"],
    ["하하", 44, "남"]
]

print(person_info)
print(person_info[0][0])
print(person_info[1][1])

"""
append 를 한다면?
"""
person_info.append(["정준하", 50, "남"])
print(person_info)

del person_info[1]
print(person_info)
# [['유재석', 51, '남'], ['하하', 44, '남'], ['정준하', 50, '남']]
