a = "3.14"
b = float(a)
c = float("-5.5")
print(type(b), type(c))

a = "3"
b = float(a)
c = float("-5")
print(type(b), type(c))
# 정수로 타입 캐스팅 가능한 String은 Float으로도 가능
# 아마 허용 가능한 byte수가 float 더 많아서 일 듯 