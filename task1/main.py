import random
num = random.randint(1,100)
count = 0
max_time = 8
print("来玩猜数字游戏啦")
print("数字范围在1到100之间")
print("最多可以猜8次哦")
while True:
    count = count + 1
    if count > max_time:
        print("次数用完咯，游戏结束")
        print("正确数字是：",num)
        break
    user = input("请输入你猜的数字：")
    if not user.isdigit():
        print("输入不对，只能填整数")
        continue
    guess = int(user)
    if guess > num:
        print("猜大啦，再往小试试")
        print("还剩",max_time-count,"次机会")
    elif guess < num:
        print("猜小啦，再往大试试")
        print("还剩",max_time-count,"次机会")
    else:
        print("太棒了，猜对啦！")
        print("一共猜了",count,"次")
        break
