from member_manager import MemberManager

def show_menu():
    print("========== RoboMaster 队员积分管理系统 ==========")
    print("1. 添加队员")
    print("2. 查看所有队员")
    print("3. 为队员加分")
    print("4. 为队员扣分")
    print("5. 按积分排名")
    print("6. 删除队员")
    print("7. 退出系统")
    print("================================================")
    return input("请选择操作（1-7）：")

def add_member(manager):
    print("\n----- 添加队员 -----")
    name = input("请输入队员姓名：").strip()
    if not name:
        print("❌ 姓名不能为空！")
        return
    
    group = input("请输入组别（视觉/电控/机械/运营）：").strip()
    valid_groups = ["视觉", "电控", "机械", "运营"]
    if group not in valid_groups:
        print(f"❌ 组别无效，请输入：{'/'.join(valid_groups)}")
        return
    
    member = manager.add_member(name, group)
    print(f"✅ 添加成功！队员编号：{member.member_id}，姓名：{member.name}，组别：{member.group}，初始积分：{member.score}")

def show_all_members(manager):
    print("\n----- 所有队员 -----")
    members = manager.get_all_members()
    if not members:
        print("暂无队员")
        return
    
    print("编号      姓名      组别      积分")
    print("--------------------------------------")
    for member in members:
        print(member)
    print("--------------------------------------")

def add_score(manager):
    print("\n----- 为队员加分 -----")
    member_id = input("请输入队员编号：").strip()
    
    try:
        points = int(input("请输入要加的分数："))
        if points <= 0:
            print("❌ 分数必须为正数！")
            return
    except ValueError:
        print("❌ 请输入有效的数字！")
        return
    
    member = manager.add_score(member_id, points)
    if member:
        print(f"✅ 成功为 {member.name} 增加 {points} 分，当前积分：{member.score}")
    else:
        print(f"❌ 未找到编号为 {member_id} 的队员！")

def deduct_score(manager):
    print("\n----- 为队员扣分 -----")
    member_id = input("请输入队员编号：").strip()
    
    try:
        points = int(input("请输入要扣的分数："))
        if points <= 0:
            print("❌ 分数必须为正数！")
            return
    except ValueError:
        print("❌ 请输入有效的数字！")
        return
    
    member, success = manager.deduct_score(member_id, points)
    if member:
        if success:
            print(f"✅ 成功为 {member.name} 扣除 {points} 分，当前积分：{member.score}")
        else:
            print(f"❌ 扣除分数不能大于当前积分（当前积分：{member.score}）！")
    else:
        print(f"❌ 未找到编号为 {member_id} 的队员！")

def rank_all(manager):
    print("\n----- 积分排行榜 -----")
    members = manager.rank_all()
    if not members:
        print("暂无队员")
        return
    
    medals = ["🥇", "🥈", "🥉"]
    print("排名  编号      姓名      组别      积分")
    print("--------------------------------------------")
    for i, member in enumerate(members):
        medal = medals[i] if i < 3 else f"  {i+1}"
        print(f"{medal}   {member}")
    print("--------------------------------------------")

def delete_member(manager):
    print("\n----- 删除队员 -----")
    member_id = input("请输入要删除的队员编号：").strip()
    
    member = manager.find_member(member_id)
    if not member:
        print(f"❌ 未找到编号为 {member_id} 的队员！")
        return
    
    print(f"⚠ 即将删除队员：{member.member_id}  {member.name}  {member.group}  {member.score}分")
    confirm = input("确认删除？(y/n)：").strip().lower()
    
    if confirm == 'y':
        manager.delete_member(member_id)
        print(f"✅ 队员 {member_id} {member.name} 已删除！")
    else:
        print("已取消删除")

def main():
    manager = MemberManager()
    
    while True:
        choice = show_menu()
        
        if choice == '1':
            add_member(manager)
        elif choice == '2':
            show_all_members(manager)
        elif choice == '3':
            add_score(manager)
        elif choice == '4':
            deduct_score(manager)
        elif choice == '5':
            rank_all(manager)
        elif choice == '6':
            delete_member(manager)
        elif choice == '7':
            print("\n👋 感谢使用 RoboMaster 队员积分管理系统，再见！")
            break
        else:
            print("❌ 无效选择，请输入 1-7 之间的数字！")

if __name__ == "__main__":
    main()