score_lst = []
A = []
B = []
C = []
numbers = int(input('请输入本班人数：'))
number = 0
a = 0
b = 0
c = 0
for item in range(numbers ):
    number += 1
    score = float(input(f'请输入第{number}学生的学习成绩：'))
    score_lst.append(score)
    if score >= 90:
        A.append(number - 1)
        A.append(score)
        a += 1
    elif score >= 60:
        B.append(number - 1)
        B.append(score)
        b += 1
    else:
        C.append(number - 1)
        C.append(score)
        c += 1
print(f"""
统计如下
本班学习成绩90分以上的人数为+{a}，分别为{A}
本班学习成绩60分以上的人数为+{b}，分别为{B}
本班学习成绩90分以上的人数为+{c}，分别为{C}
""")
