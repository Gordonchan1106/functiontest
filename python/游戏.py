# day1
while True:
    print("""
    第一关：
    选择
      1.前进
      2. 发起攻击

    """)
    choice1 = input("请输入您的选择：")
    if choice1 == "1":
        print("前进")
    elif choice1 == "2":
        print("发起攻击")
    print("""
    选择
      1.回到第一关
      2. 退出游戏
      3.继续

    """)
    choice2 = input("请输入您的选择：")
    if choice2 == "1":
        continue
    elif choice2 == "2":
        break

    print("""
    第二关：
    选择
      1. 购买装备
      2.查看地图
      3.回城

    
    """)
    choice3 = input("请输入您的选择：")
    if choice3 == "1":
        print("购买装备")
    elif choice3 == "2":
        print("查看地图")
    elif choice3 == "3":
        print("回城")

    break
