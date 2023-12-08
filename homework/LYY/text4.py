a = int(input('请输入a：'))
b = int(input('请输入几个a相加：'))
i = 0
d = 0
for item in range(b):
    i += 1
    d += a*10**(b-i)*i
print(d)