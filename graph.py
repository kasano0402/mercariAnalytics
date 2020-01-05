def graphdata(list):

    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    hierarchy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    price = [y[1] for y in list]
    sold = [x[2] for x in list]

    # 最大値を求める
    maxPrice = 0
    soldElements = 0
    for x in price:
        if sold[soldElements] == 'sold':
            money = int(x)
            if maxPrice <= money:
                maxPrice = money
        soldElements += 1

    # print(maxPrice)
    # print(sold)

    # 階層の数を求める
    soldElements = 0
    average = int(maxPrice / 10)
    soldcount = 0

    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        hierarchy[i] = hierarchy[i-1]+average

    for x in price:
        if sold[soldElements] == 'sold':
            soldcount += 1
            money = int(x)
            dataElements = int(money/average)
            if dataElements != 10:
                data[dataElements] += 1
            else:
                data[9] += 1
        soldElements += 1

    # dataTextの整形
    dataText = ""
    for val in data:
        dataText += str(val)
        dataText += ","
    dataText = dataText[:-1]
    print(dataText)

    # labelsTextの整形
    labelsText = ""
    for val in hierarchy:
        labelsText += "'"
        labelsText += "\xA5"
        labelsText += str("{:,d}".format(val))
        labelsText += "~"
        labelsText += "'"
        labelsText += ","
    labelsText = labelsText[:-1]
    print(labelsText)

    # maxsoldnum
    maxSoldNum = max(data)

    result = [dataText, labelsText, maxSoldNum]
    return result
