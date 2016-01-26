#coding:utf-8

#购物车列表
goodsCat = {}

#用户信息
global USERINFO
USERINFO = []

# 商品列表
global GOODS
GOODS = {
    "1": {"name":"Apple iPhone 6s", "price":"4888.00"},
    "2": {"name":"Apple iPhone 6s plus", "price":"6388.00"},
    "3": {"name":"Apple MacBook Pro", "price":"17988.00"},
    "4": {"name":"Apple MacBook air", "price":"5688.00"},
    "5": {"name":"Apple Watch Sport", "price":"2438.00"},
    "6": {"name":"Apple Watch Edition", "price":"126800.00"}
}

# 判断用户是否登录
global ISGOTO
ISGOTO = True

# 已购商品列表
global GOODIDS
GOODIDS = []

# 用户登录模块
def login(go = 0):
    global ISGOTO
    global USERINFO
    print("欢迎来到 iThresh 登录系统!")

    while ISGOTO:
        userName = input("请输入用户名：")
        userPass = input("请输入用户密码：")

        if (userName != "" and userPass != ""):
            userData = open("user.txt", 'r')
            userInfos = userData.readlines()

            for user in userInfos:
                info = user.rstrip().split(',')
                infoName = info[0]
                infoPass = info[1]

                if (userName == infoName and userPass == infoPass):
                    print("登录成功! 欢迎会员" + userName)
                    USERINFO = info
                    ISGOTO = False
                    if (go == 0):
                        showGoods()
                    else:
                        buyGoods(go)

                    break
                else:
                    print("Error: 用户名，密码有误，请重新输入！")

            userData.close()
        else:
            print("Error: 请输入用户名，密码")

# 商品展示
def showGoods():
    print("Hi, 欢迎选购商品")

    global GOODS
    for k, info in GOODS.items():
        info = """Id:%s, Name:%s, Price:%s"""%(k, info["name"], info["price"]+"元")
        print(info)

    # (输入C进入购物车结算)
    global GOODIDS
    while True:
        inputId = input("请输入商品ID，来选购您的商品。输入C进入购物车结算: ")
        if (inputId != "" and inputId != "C" and inputId != "c"):
            GOODIDS.append(inputId)
        elif (inputId == "C" or inputId == "c"):
            cat(GOODIDS)
            break

# 购物车
def cat(ids):
    print("欢迎来到购物车结账 ^_^")
    print("下面是您选购的商品")

    global GOODS
    allPrice = 0.0
    goodsNum = 0
    for index, id in enumerate(ids):
        good = GOODS.get(id)
        if (good):
            info = """Id:%s, Name:%s, Price:%s"""%(index+1, good["name"], good["price"]+"元")
            print(info)
            allPrice += float(good["price"])
            goodsNum += 1
        else:
            print("Error: 我们的商城没有 " + id + " 这件商品，十分抱歉。")

    msg = """你好！你共买了 %s 件商品，总价: %s"""%(goodsNum, allPrice)
    print(msg)

    isBuy = input("是否结算y/n：")
    if (isBuy == "y" or isBuy == "Y"):
        buyGoods(allPrice)
    elif (isBuy == "n" or isBuy == "N"):
        showGoods()

# 支付
def buyGoods(allPrice):
    global USERINFO
    global ISGOTO

    if (not ISGOTO):
        userMone = float(USERINFO[2])
        payMone = userMone-allPrice
        if (userMone >= allPrice):
            msg = """支付完成！共花费%s元,帐户余额%s"""%(allPrice, payMone)
            print(msg)

            USERINFO[2] = payMone
            userData = open("user.txt", 'w+')
            msg = """%s,%s,%s"""%(USERINFO[0], USERINFO[1], USERINFO[2])
            userData.writelines(msg)
            userData.close()
        else:
            print("SOS，账户余额不足。正在跳转充值界面...")
            iPay(allPrice)
    else:
        login(allPrice)

# 充值
def iPay(allPrice):
    global USERINFO
    print("正在充值100万，不差钱...")
    userData = open("user.txt", 'w+')
    msg = """%s,%s,%s"""%(USERINFO[0], USERINFO[1], (float(USERINFO[2])+1000000))
    userData.writelines(msg)
    userData.close()
    USERINFO[2] = float(USERINFO[2]) + 1000000
    buyGoods(allPrice)

# 主入口
def main() :
    print("欢迎来到 iThresh 商城！")

    tips = {1: "登录", 2: "购物"}

    for k, v in tips.items():
        print(k,"." + v)

    select = input("请输入您要进行的操作~\n")

    if (select == "1"):
        login()
    elif (select == "2"):
        showGoods()


if __name__ == "__main__":
    main()