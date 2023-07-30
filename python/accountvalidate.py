accouts = {
    # "alex"
    # "alex" : ["alexabc123!","1"],
}
f = open("account.db", "r")
for line in f:
    line = line.strip().split(",")
    accouts[line[0]] = line
print(accouts)

while True:
    user = input("Username:").strip()
    if user not in accouts:
        print("user is invalid")
        continue
    count = 0
    while count < 3:
        passwd = input("Password").strip()
        if passwd == accouts[user][1]:
            print(f"welcome {user}...log in succeed")
            exit("bye....")
        else:
            print("Wrong Password")
        count += 1
    if count == 3:
        print(f"输错了{count},需要锁定账号{user}...")
        accouts[user][1] = "1"
        f2 = open("account.db", "w")
        for user, val in accouts.items():
            line = ",".join(val) + "\n"
            f2.write(line)
        f2.close()
        exit("bye.")
