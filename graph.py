import math


def graphdata(list):

    # リストを配列に代入
    price = [y[1] for y in list]
    sold = [x[2] for x in list]

    # スタージェスの公式
    frequency = round(1 + math.log2(len(list)))

    data = [0] * frequency
    hierarchy = [0] * frequency

    # 最大値と最小値を求める
    max_price = 0
    min_price = 0
    sold_elements = 0
    for money in price:
        if sold[sold_elements] == 'sold':
            if max_price <= money:
                max_price = money
            if min_price >= money:
                min_price = money
        sold_elements += 1

    # print(max_price)
    # print(sold)

    # 階級幅
    sold_elements = 0
    average = int((max_price - min_price)/frequency/10000)
    sold_count = 0
    average = int((average+1)*10000)

    for i in range(frequency-1):
        hierarchy[i+1] = hierarchy[i]+average

    # 階級幅毎の件数
    for money in price:
        if sold[sold_elements] == 'sold':
            sold_count += 1
            data_elements = int(money / average)
            if data_elements < frequency:
                data[data_elements] += 1
            else:
                data[frequency - 1] += 1
        sold_elements += 1

    # data_textの整形
    data_text = ""
    for val in data:
        data_text += str(val)
        data_text += ","
    data_text = data_text[:-1]
    # print(data_text)

    # labels_textの整形
    labels_text = ""
    for val in hierarchy:
        labels_text += "'"
        labels_text += "\xA5"
        labels_text += str("{:,d}".format(val))
        labels_text += "~"
        labels_text += "'"
        labels_text += ","
    labels_text = labels_text[:-1]
    # print(labels_text)

    # max_sold_num
    max_sold_num = int((max(data)/10 + 1)) * 10

    # ステップ数
    step_size = 5

    if max_sold_num >= 100:
        step_size = 10
    elif max_sold_num < 30:
        step_size = 1

    result = [data_text, labels_text, max_sold_num, step_size]
    return result
