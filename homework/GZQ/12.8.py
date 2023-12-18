# 题目： 学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
score=(float(input('请输入分数')))
if (score>=90):
    print('A')
elif(score>=60):
    print('B')
else:
    print('C')

# 题目：对10个数进行排序 利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。

# list1=[x for x in range(1,10000)]
#
# list2=sorted(list1)
# print(list2)

# 题目：按相反的顺序输出列表的值。
items = ['Python', 'Java', 'Go', 'Kotlin', 'Python']
items.reverse()
print(items)

#
# 题目：**求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
a=int(input('a='))
n=int(input('n='))
x=0
y=0
for t in range (0,n):
    x+=a*10**t
    y+=x
print(y)

