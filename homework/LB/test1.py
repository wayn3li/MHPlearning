"""

Version: 0.1
Author: libai
Time： 2023/12/8 18:09
"""
from functools import reduce

# 1.
# 题目：
# 学习成绩 >= 90
# 分的同学用A表示，60 - 89
# 分之间的用B表示，60
# 分以下的用C表示。
# ```python
score = int(input("输入成绩"))


def judge(score):
    if score >= 90:
        print("A")
    elif 60 < score < 89:
        print('B')
    else:
        print('C')




# 2.
# 题目：对10个数进行排序
# 利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
# ```python
N = 10
l = []

for i in range(N):
    l.append(int(input("请输入")))

for i in range(N - 1):
    min = i
    for j in range(i + 1, N):
        if l[min] > l[j]:
            min = j
    l[i], l[min] = l[min], l[i]

    print('从小到大排序：')
    for i in range(N):
        print(l[i])


# 3.
# 题目：按相反的顺序输出列表的值

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits_r = fruits[::-1]
fruits.reverse()
print(fruits)  # ['Python', 'Python', 'Kotlin', 'Java', 'Go']
print(fruits_r)

# 4.
# 题目：求s = a + aa + aaa + aaaa + aa...a的值，其中a是一个数字。例如2 + 22 + 222 + 2222 + 22222(
#     此时共有5个数相加)，几个数相加由键盘控制。

Tn = 0
Sn = []
n = int(input('n = '))
a = int(input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)

Sn = reduce(lambda x, y: x + y, Sn)
print("计算和为：", Sn)

