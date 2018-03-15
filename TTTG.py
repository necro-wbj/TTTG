#! python
import random
a = [0 for _ in range(9)]
player = 1
temp = 0


def ox(a):
    if a == 0:
        return " "
    elif a == -1:
        return "X"
    elif a == 1:
        return "O"


def p():
    global a
    print(ox(a[0]) + '|' + ox(a[1]) + '|' + ox(a[2]))
    print("_", "_", "_")
    print(ox(a[3]) + "|" + ox(a[4]) + "|" + ox(a[5]))
    print("_", "_", "_")
    print(ox(a[6]) + "|" + ox(a[7]) + "|" + ox(a[8]))


def u(tem):
    global a, player
    for i in range(1, 10):
        if tem == str(i):
            a[i - 1] = player


def win():
    global a, player, test
    if a[0] != 0 and a[0] == a[1] and a[1] == a[2]:
        print("玩家：", ox(player), "獲勝!!")
        return False
    elif a[3] != 0 and a[3] == a[4] and a[4] == a[5]:
        print("玩家：", ox(player), "獲勝!!")
        return False
    elif a[6] != 0 and a[6] == a[7] and a[7] == a[8]:
        print("玩家：", ox(player), "獲勝!!")
        return False
    elif a[0] != 0 and a[0] == a[3] and a[3] == a[6]:
        print("玩家：", ox(player), "獲勝!!")
        return False
    elif a[1] != 0 and a[1] == a[4] and a[4] == a[7]:
        print("玩家：", ox(player), "獲勝!!")
        return False
    elif a[2] != 0 and a[2] == a[5] and a[5] == a[8]:
        print("玩家：", ox(player), "獲勝!!")
        return False
    elif a[0] != 0 and a[0] == a[4] and a[4] == a[8]:
        print("玩家：", ox(player), "獲勝!!")
        return False
    elif a[2] != 0 and a[2] == a[4] and a[4] == a[6]:
        print("玩家：", ox(player), "獲勝!!")
        return False
    elif a.count(0) == 0:
        print("平手!!!")
        return False
    else:
        return True


def ai():
    global a, temp, player
    if a[0] != 0 and a[1] == 0 and a[0] == a[2]:
        temp = 2
        print("偵錯1")
    elif a[2] != 0 and a[5] == 0 and a[2] == a[8]:
        temp = 6
        print("偵錯2")
    elif a[6] != 0 and a[7] == 0 and a[6] == a[8]:
        temp = 8
        print("偵錯3")
    elif a[0] != 0 and a[3] == 0 and a[0] == a[6]:
        temp = 4
        print("偵錯4")

    elif a[0] != 0 and a[0] != player and a[1] != 0 and a[1] != player and a[2] == 0:
        temp = 3
        print("偵錯5")
    elif a[0] != 0 and a[0] != player and a[3] != 0 and a[3] != player and a[6] == 0:
        temp = 7
        print("偵錯6")
    elif a[2] != 0 and a[2] != player and a[1] != 0 and a[1] != player and a[0] == 0:
        temp = 1
        print("偵錯7")
    elif a[2] != 0 and a[2] != player and a[5] != 0 and a[5] != player and a[8] == 0:
        temp = 9
        print("偵錯8")
    elif a[6] != 0 and a[6] != player and a[3] != 0 and a[3] != player and a[0] == 0:
        temp = 1
        print("偵錯9")
    elif a[6] != 0 and a[6] != player and a[7] != 0 and a[7] != player and a[8] == 0:
        temp = 9
        print("偵錯10")
    elif a[8] != 0 and a[8] != player and a[5] != 0 and a[5] != player and a[2] == 0:
        temp = 3
        print("偵錯11")
    elif a[8] != 0 and a[8] != player and a[7] != 0 and a[7] != player and a[6] == 0:
        temp = 7
        print("偵錯12")

    elif a[1] != 0 and a[1] != player and a[4] != 0 and a[4] != player:
        temp = 8
        print("偵錯13")
    elif a[3] != 0 and a[3] != player and a[4] != 0 and a[4] != player:
        temp = 6
        print("偵錯14")
    elif a[5] != 0 and a[5] != player and a[4] != 0 and a[4] != player:
        temp = 4
        print("偵錯15")
    elif a[7] != 0 and a[7] != player and a[4] != 0 and a[4] != player:
        temp = 2
        print("偵錯16")
    elif a[0] != 0 and a[0] == a[8] and a[0] != player:
        if a[1] == 0:
            temp = 2
        elif a[3] == 0:
            temp = 4
        elif a[5] == 0:
            temp = 6
        elif a[7] == 0:
            temp = 8
    elif a[2] != 0 and a[0] == a[6] and a[2] != player:
        if a[1] == 0:
            temp = 2
        elif a[3] == 0:
            temp = 4
        elif a[5] == 0:
            temp = 6
        elif a[7] == 0:
            temp = 8
    elif a[4] == 0:
        temp = 5
        print("偵錯17")

    elif a[4] == player and a[0] == player and a[2] == 0:
        temp = 3
        print("偵錯18")
    elif a[4] == player and a[0] == player and a[6] == 0:
        temp = 7
        print("偵錯19")
    elif a[4] == player and a[2] == player and a[0] == 0:
        temp = 1
        print("偵錯20")
    elif a[4] == player and a[2] == player and a[8] == 0:
        temp = 9
        print("偵錯21")
    elif a[4] == player and a[6] == player and a[0] == 0:
        temp = 1
        print("偵錯22")
    elif a[4] == player and a[6] == player and a[8] == 0:
        temp = 9
        print("偵錯23")
    elif a[4] == player and a[8] == player and a[2] == 0:
        temp = 3
        print("偵錯24")
    elif a[4] == player and a[8] == player and a[6] == 0:
        temp = 7
        print("偵錯25")

    elif a[0] == 0 and a[8] == 0:
        temp = 1
        print("偵錯26")
    elif a[2] == 0 and a[6] == 0:
        temp = 3
        print("偵錯27")

    elif a[6] == 0 and a[4] == a[2]:
        temp = 7
        print("偵錯28")
    elif a[8] == 0 and a[4] == a[0]:
        temp = 9
        print("偵錯29")
    elif a[2] == 0 and a[4] == a[6]:
        temp = 3
        print("偵錯28")
    elif a[0] == 0 and a[4] == a[8]:
        temp = 1
        print("偵錯29")
    else:
        temp = a.index(0) + 1
        print("偵錯其他")


def act(arr):
    global a
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = 1
        elif arr[i] < 0:
            arr[i] = -1
        else:
            arr[i] = 0


def ai2():
    global a, temp
    import random
    weight = [[random.triangular(-1, 1)for _ in range(9)]for _ in range(10)]
    h = [0 for _ in range(10)]
    s = [random.random() for _ in range(10)]
    baise = [random.random() for _ in range(9)]
    weight2 = [[random.triangular(-1, 1)for _ in range(10)]for _ in range(9)]
    output = [0 for _ in range(9)]

    for i in range(9):
        for j in range(10):
            h[j] += a[i] * weight[j][i] + s[j]
    act(h)
    for i in range(10):
        for j in range(9):
            output[j] += h[i] * weight2[j][i] + baise[j]
    act(output)

    print(output)

    cho = []
    for i in range(9):
        if a[i] == 0 and output[i] == 1:
            cho.append(i + 1)
    t = random.choice(cho)
    temp = t

    # print(a)
    # print(weight)
    # print(s)
    # print(h)
    # print(weight2)
    # print(baise)
    # print(output)

    # import random
    # r = random.randint(0, 8)
    # if a[r] != 0:
    #     ai2()
    # else:
    #     temp = r + 1


def human():
    global temp, a
    temp = input('請輸入格位：')
    while a[int(temp) - 1] != 0:
        temp = input('輸入錯誤!請重新輸入：')


while win():
    if player == 1:
        human()
    else:
        ai()
    u(str(temp))
    p()
    if player == 1:
        player = -1
    else:
        player = 1
    print("-----------------------------")
    print(a)
    print("-----------------------------")
# ai2()
