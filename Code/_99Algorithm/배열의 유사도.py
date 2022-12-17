
s1 = ["a", "b", "c"]
s2 = ["com", "b", "d", "p", "c"]

count = 0

for i in s1:
    for j in s2:
        if i == j: 
            count += 1


print(count)