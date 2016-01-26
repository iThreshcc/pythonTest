#coding: utf-8
#File: login.py
#Author: 小东邪iThresh <iThresh@ithresh.cc>
#实现用户注册，登录，登录锁定等功能

print("HI! 请选择你接下来的操作！")
print("1:注册用户\n2:登录系统")

action = input()

if (action == "1"):
    print("您选择了注册用户，正在跳转请稍后...")

    userName = input("请输入用户名:")
    userPass = input("请输入密码:")

    file = open("user.txt", 'a+')
    userInfo = '%s,%s,unlock\n'%(userName,userPass)
    file.write(userInfo)
    file.close()
    print("注册成功！正在登录中，请等待...")
    print("HI!,"+ userName +"登录成功！")

elif (action == "2"):
    print("您选择了登录系统，正在跳转请稍后...")
    gCount = 0

    while True:
        userName = input("请输入用户名:")
        userPass = input("请输入密码:")

        file = open("user.txt", 'r+')
        userInfos = file.readlines()

        for line in userInfos:
            info = line.rstrip('\n').split(',')

            infoName = info[0]
            infoPass = info[1]
            infoStat = info[2]

            # 先判断是否用户锁定
            if (userName == infoName and userPass == infoPass and infoStat == "lock") :
                print("账户已锁定")
                exit()
            elif (userName == infoName and userPass == infoPass and infoStat == "unlock") :
                print("HI!,"+ infoName +"登录成功！")
            elif (userName == infoName) :
                gCount += 1

                # 同一用户输入错误三次，锁定
                if (gCount == 3) :
                    # 清空文件，这里不知道为什么没有用
                    file.truncate()
                    userInfo = '%s,%s,lock\n'%(userName,infoPass)

                    userInfos.remove(line)
                    userInfos.insert(0, userInfo)

                    file.writelines(userInfos)

                    print("账户已锁定")
                    exit()

                print("登录失败，请重新登录！", gCount)
                break
            else:
                print("登录失败，请重新登录！")
                break

        file.close()
