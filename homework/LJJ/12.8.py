1.#学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
number = float(input("请输入你的分数："))
if number >= 90:
    print("A")
elif number < 60 :
    print("C")
else:
    print("B")

2.#对10个数进行排序 利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
number_list = eval(input("请输入十个数字："))
number_list = list(number_list)

count = 1
while count < 9 :
    num_min = min(number_list[count:9])
    num_1 = number_list.index(num_min)
    if number_list[count-1] > number_list[num_1]:
        number_list[count-1],number_list[num_1] \
            = number_list[num_1],number_list[count-1]
    count += 1
print(number_list)

3.#按相反的顺序输出列表的值。
number_list = eval(input("请输入："))
number_list = list(number_list)
print(number_list[::-1])

4.#**求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
a = str(input("请输入a的值:"))
count = float(input("请输入相加次数："))
i = 1
s = 0
while i < (count + 1):
    num = int(a * i)
    s += num
    i += 1
print(s)
