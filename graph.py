def hoge(list):

    date = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    hierarchy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    price = [y[1] for y in list]
    sold = [x[2] for x in list]

    # 最大値を求める
    max = 0
    soldElements = 0
    for x in price:
        if sold[soldElements] == 'sold':
            tmp = x.split('¥')
            money = int(tmp[1])
            if max <= money:
                max = money
        soldElements += 1

    print(max)
    print(sold)

    # 階層の数を求める
    soldElements = 0
    average = int(max / 10)
    soldcount = 0

    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        hierarchy[i] = hierarchy[i-1]+average

    for x in price:
        if sold[soldElements] == 'sold':
            soldcount += 1
            tmp = x.split('¥')
            money = int(tmp[1])
            dateElements = int(money/average)
            if dateElements != 10:
                date[dateElements] += 1
            else:
                date[9] += 1
        soldElements += 1

    print(soldcount)
    print(hierarchy)
    print(date)
