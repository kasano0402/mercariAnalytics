def graphdata(list):

    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    hierarchy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    price = [y[1] for y in list]
    sold = [x[2] for x in list]

    # 最大値を求める
    maxPrice = 0
    soldElements = 0
    for money in price:
        if sold[soldElements] == 'sold':
            if maxPrice <= money:
                maxPrice = money
        soldElements += 1

    # print(maxPrice)
    # print(sold)

    # 階層の数を求める
    soldElements = 0
    average = int(maxPrice/10000)
    soldcount = 0
    average = int((average+1)*1000)
    # print(average)

    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        hierarchy[i] = hierarchy[i-1]+average

    for money in price:
        if sold[soldElements] == 'sold':
            soldcount += 1
            dataElements = int(money / average)
            print(dataElements)
            if dataElements < 10:
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
    # print(dataText)

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
    # print(labelsText)

    # maxsoldnum
    maxSoldNum = int((max(data)/10 + 1)) * 10

    stepsize = 5

    if maxSoldNum >= 100:
        stepsize = 10
    elif maxSoldNum < 10:
        stepsize = 1

    result = [dataText, labelsText, maxSoldNum, stepsize]
    return result
