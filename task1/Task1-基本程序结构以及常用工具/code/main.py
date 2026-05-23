"""
猜数游戏 - 适合初学者的版本
学习了：变量、输入输出、条件判断、循环、列表、异常处理、函数
"""

import random


def get_decimal_places(text):
    """
    获取字符串中小数点后有几位数字
    例如: "1.00" 返回 2, "100" 返回 0
    """
    if '.' in text:
        # 按小数点分割，取小数部分
        decimal_part = text.split('.')[1]
        return len(decimal_part)
    return 0


def generate_random_number(min_val, max_val):
    """
    根据区间端点的精度生成随机数
    """
    # 获取最小值的精度（小数位数）
    decimal_places = get_decimal_places(str(min_val))

    if decimal_places == 0:
        # 没有小数，生成整数
        return random.randint(int(min_val), int(max_val))
    else:
        # 有小数，生成指定精度的浮点数
        return round(random.uniform(float(min_val), float(max_val)), decimal_places)


def play_game():
    """
    运行一轮猜数游戏
    """
    print("\n" + "=" * 40)
    print("欢迎来到猜数游戏！")
    print("=" * 40)

    # ================== 第一步：设置猜测范围 ==================
    while True:
        try:
            min_input = input("请输入猜测范围的最小值（例如：1 或 1.00）：")
            max_input = input("请输入猜测范围的最大值（例如：100 或 100.00）：")

            min_val = float(min_input)
            max_val = float(max_input)

            if min_val >= max_val:
                print("错误：最小值必须小于最大值，请重新输入！")
                continue

            break
        except ValueError:
            print("错误：请输入有效的数字！")

    # ================== 第二步：设置最大尝试次数 ==================
    while True:
        try:
            max_attempts = int(input("请输入最大尝试次数（例如：10）："))
            if max_attempts <= 0:
                print("错误：尝试次数必须大于0！")
                continue
            break
        except ValueError:
            print("错误：请输入整数！")

    # ================== 第三步：生成随机数 ==================
    target = generate_random_number(min_val, max_val)
    print(f"\n我已经想好了一个数字（范围：{min_val} ~ {max_val}）")
    print(f"你有 {max_attempts} 次猜测机会，加油！\n")

    # 存储猜测历史
    history = []
    attempts = 0

    # ================== 第四步：开始猜测循环 ==================
    while attempts < max_attempts:
        # 计算剩余次数
        remaining = max_attempts - attempts
        print(f"剩余尝试次数：{remaining}")

        # 获取玩家输入
        while True:
            try:
                guess_input = input("请输入你猜的数字：")
                guess = float(guess_input)

                # 判断精度：如果原始输入是整数字符串，就转换为整数比较
                if '.' not in guess_input and guess == int(guess):
                    guess = int(guess)
                break
            except ValueError:
                print("错误：请输入有效的数字！")

        attempts += 1

        # ================== 第五步：判断猜测结果 ==================
        if guess == target:
            # 猜对了！
            print(f"\n🎉 恭喜你猜对了！答案是 {target}")
            print(f"你总共尝试了 {attempts} 次")

            # 记录这次猜测
            history.append((guess, "="))
            break

        elif guess < target:
            # 猜小了
            print(f"太小了 ↑（你猜的是 {guess}）")
            history.append((guess, "↑"))
        else:
            # 猜大了
            print(f"太大了 ↓（你猜的是 {guess}）")
            history.append((guess, "↓"))

    # ================== 第六步：游戏结束处理 ==================
    if attempts >= max_attempts and (attempts == 0 or history[-1][1] != "="):
        print(f"\n😢 游戏结束！正确答案是 {target}")

    # ================== 第七步：显示猜测轨迹 ==================
    if history:
        print("\n你的猜测轨迹：", end="")
        trajectory = ""
        for guess, result in history:
            if result == "=":
                trajectory += f"{guess} √"
            elif result == "↑":
                trajectory += f"{guess} ↑ → "
            else:
                trajectory += f"{guess} ↓ → "

        # 去掉最后多余的 " → "
        trajectory = trajectory.rstrip(" → ")
        print(trajectory)

    # ================== 第八步：询问是否再来一局 ==================
    while True:
        again = input("\n是否再来一局？（输入 yes 继续，其他退出）：")
        if again.lower() in ['yes', 'y', '是', '1']:
            return True  # 继续游戏
        else:
            return False  # 退出游戏


# ================== 主程序入口 ==================
if __name__ == "__main__":
    print("=" * 50)
    print("          欢迎来到猜数游戏！")
    print("=" * 50)

    while True:
        continue_game = play_game()
        if not continue_game:
            print("\n感谢游玩，再见！👋")
            break
