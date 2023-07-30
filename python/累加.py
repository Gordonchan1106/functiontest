# day1
# s = 0
# for i in range(1,101):
#     s += i
#
# print(s)

# day2
ret = 0
for i in range(1, 101):
    if i % 13 == 0:
        ret += i
    else:
        pass
print(ret)

# while True:
#     print("""
#       1.前进
#       2. 发起攻击
#       3. 购买装备
#       4.查看地图
#       5.回城
#
#
#     """)
#     choice = input("请输入您的选择：")
#     if choice == "1":
#         print("前进")
#     elif choice == "2":
#         print("发起攻击")
#     elif choice == "3":
#         print("购买装备")
#     elif choice == "4":
#         print("查看地图")
#     elif choice == "5":
#         print("回城")
#     else:
#         break


for r in range(1, 101):
    area = 3.1415926 * r ** 2
    if area > 1000:
        print(f"半径为{r}的圆的面积：{area}")
        break


print(10000%320)