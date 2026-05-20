import random
def guess_number_game():
    print("游戏")
    min_num=1
    max_num=100
    max_attempts=7
    while True:
        target=random.randint(min_num,max_num)
        print(f"\n输入一个{min_num}~{max_num}之间的数字，有{max_attempts}次机会")
        guess_history=[]
        attempts=0
        success=False
        while attempts<max_attempts:
            while True:
                try:
                    guess=int(input(f"\n输入你猜的数字："))
                    if min_num<=guess<=max_num:
                        break
                    else:
                            print(f"错误 请输入{min_num}~{max_num}之间的数字")
                except ValueError:
                        print("错误 请输入一个整数")
            attempts +=1
            remaining=max_attempts-attempts
            if guess<target:
                print(f"错误 猜小了 你还有{remaining}次机会")
                guess_history.append(f"{guess}↑")
            elif guess>target:
                print(f"错误 猜大了 你还有{remaining}次机会")
                guess_history.append(f"{guess}↓")
            else:
                print(f"你答对了 答案就是{target}")
                print(f"你一共尝试了{attempts}次")
                guess_history.append(f"{guess}√")
                success=True
                break
        if not success:
            print(f"\n 游戏结束 次数用完了，正确答案是{target}")
        print("\n你的猜测轨迹:")
        print("→".join(guess_history))
        choice=input("\n重新开始游戏（输入y继续，n退出）:")
        if choice!='y':
            print("游戏结束")
            break
if __name__=="__main__": 
    guess_number_game()