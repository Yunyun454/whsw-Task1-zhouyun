import random
target: float = round(random.uniform(1.0, 100.0), 2)
count = 0
max_times = 8
precision = 1.0
print("猜数字小游戏（带精度判断）")
print("数字范围：1.0 ~ 100.0")
print("误差在1.0以内都判定为猜对")
print("总共只有8次猜测机会")
while True:
    count += 1
    if count > max_times:
        print("次数全部用完，游戏结束")
        print("真实数字是：", target)
        break

    input_str: str = input("输入你猜测的数值：")
    try:
        guess_num = float(input_str)
    except ValueError:
        print("输入格式错误，请输入数字！")
        count -= 1
        continue
    diff = abs(guess_num - target)
    if diff < precision:
        print("数值接近，符合精度要求，猜对啦！")
        print("本次总共猜测次数：", count)
        break
    elif guess_num > target:
        print("数值偏大了")
        print("剩余机会：", max_times - count)
    else:
        print("数值偏小了")
        print("剩余机会：", max_times - count)