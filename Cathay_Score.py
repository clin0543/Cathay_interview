def dealData(data):
    """Suggest input dict"""
    #No limit Score Like 0~100
    #TODO Best->Discuss setting Excel/csv Format
    data_type = type(data)
    print('Input Type:', data_type)
    if data_type == int or data_type == float:
        return digitLogic(data)
    elif data_type == list:
        return listLogic(data)
    elif data_type == dict:
        return dictLogic(data)
    else:
        print('Type Error, Plase input type: int/float/list/dict')
        raise TypeError

def digitLogic(data):
    if data < 40:
        print('Score < 40, Return original Score')
        return data
    else:
        if data%5 >= 3:
            print('Conform, Add point')
            return ((int(data/5))+1)*5
        else:
            print('Score>40 & Score/5 < 3, Return original Score')
            return data

def listLogic(data):
    allscore = []
    for index in data:
        allscore.append(digitLogic(index))
    return allscore

def dictLogic(data):
    allscore = {}
    keyerror = 0
    for k,v in data.items():
        print(k,v)
        if k == '':
            allscore['NoName'+str(keyerror)] = digitLogic(v)
            keyerror += 1
        else:
            allscore[k] = digitLogic(v)
    # print(allscore)
    return allscore

if __name__ == '__main__':
    print('If you want to increase Excel/CSV function, please contact ????@gmail.com')
    print('---(Version1.0.0 Suggest use dict)---')
    Score = {'甲':91, '乙':82.99, '丙':73.33, '':44} #input Data

    try:
        print(dealData(Score))
    except:
        print('Check Input Data')
