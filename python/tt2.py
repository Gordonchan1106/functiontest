# day1
account = {}

f = open("account.db", "r")
for line in f:
    line = line.strip().split(",")
    account[line[0]] = line

print(account)

while True:
    user = input("Username:").strip()
    if user not in account:
        print("invalid user")
        continue
    elif account[user][2] == "1":
        print("User has been locked")
        continue
    count = 0
    while count < 3:
        passwd = input("Password: ").strip()
        if passwd == account[user][1]:
            print(f"{user}log in succeed")
            exit("bye...")
        else:
            print("Wrong Password")
        count += 1
    if count == 3 :
        print(f"Invalid Password,{user} will be locked")
        account[user][1] = "1"
        f2 = open("account.db", "w")
        for user, val in account.items():
            line = ",".join(val) + "\n"
            f2.write(line)
        f2.close()
        exit("bye.")