print("1111",end="***")
print("2222")
print("4444")

print("6"*10)


# 分支语句

a = -10

if a > 0:
    print("a是正数")
    print("9999")
else:
    print("a不是正数")

# age = input("请输入一个年龄：")
#
# age = int(age)
#
# if age > 12 and age <30:
#     print("青年")
#
# print(age)


score = 97

if score >= 90 and score <= 100:
    print("成绩为A")
elif score >= 80 and score <90:
    print("B")
elif score >= 70 and score <80:
    print("C")
elif score >= 60 and score <70:
    print("D")
elif score >= 0 and score <60:
    print("E")
else:
    print("不合法输入")


# 产生随机数
import random

while True:

    computer = random.randint(0,2)

    player = input("请输入：剪刀(0) 石头(1) 布(2):")

    player = int(player)

    if ((player == 0) and (computer == 2)) or ((player == 1) and (computer == 0)) or ((player == 2) and (computer == 1)):
        print("我赢了")
    elif player == computer:
        print("平手")
    else:
        print("输了，洗洗手再来")