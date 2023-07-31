# day1
def studen_register(name, age, course = 'PY',country = 'NZ'):
    print("-----注册学生信息---------")
    print("姓名：", name)
    print("年龄", age)
    print("国籍", country)
    print("课程", course)
    # print(name,age,args,args[0])
    if age > 22:
      return False
    else:
      return True
# studen_register("pao", 22)
register_status = studen_register("gordon",22,course = "sport", country = 'CN')
print(register_status)
if register_status :
   print("register succeeded")
else:
   print("over age")



