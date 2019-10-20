switcherAravt={
           '조': 1000000000000,
           '억': 100000000,
           '만': 10000,
           '천': 1000,
           '백': 100,
           '십': 10
           }

switcherAravtEsreg={
           13: '억',
           9: '조',
           5:'만',
           4: '천',
           3: '백',
           2: '십'
           }

switcherNum={
    '구': 9,
    '팔': 8,
    '칠': 7,
    '육': 6,
    '오': 5,
    '사': 4,
    '삼': 3,
    '이': 2,
    '일': 1
    }

switcherNumEsreg={
    9: '구',
    8: '팔',
    7: '칠',
    6: '육',
    5: '오',
    4: '사',
    3: '삼',
    2: '이',
    1: '',
    0: ''
}
    
def parse2IntList(numStr):
    aravtList=['조','만','천','백','십']
    intList = []
    i=0
    
    while i < len(numStr):
        ucode = numStr[i].encode('utf-8')
        if ucode in aravtList:
            aravt = switcherAravt.get(ucode, False)
            print(aravt)
            if aravt == False:
               return False
            last = 0
            integer = aravt
            j=len(intList)-1
            while j >= 0:
                if intList[j]<aravt:
                    last+=intList[j]
                    intList.pop()
                j-=1
            if last>0 and last<aravt:
                integer = last*aravt

            intList.append(integer)
        else:
            integer = switcherNum.get(ucode, False)
            if integer == False:
               return False
            intList.append(integer)
        i+=1
        print(intList)
    return intList

def parse2Int(numList):
    sum = 0
    i=0
    while i < len(numList):
        sum+=numList[i]
        i+=1

    return sum

def getNum():
    while True:
        numStr = raw_input('Please enter integer in hangul to add.Ex: 일십만 \n')
        numList = parse2IntList(numStr)
        
        if numList == False: 
            print('Please enter correctly. Ex: 일십만\n')
        else:
            num = parse2Int(numList)
            return num

def num2Str(num):
    numStr = str(num)
    result=""
    i=0
    while i<len(numStr):
        integer = int(numStr[i])
        result = result+(switcherNumEsreg.get(integer, False))
        if result == False:
            return False
       
        aravt = switcherAravtEsreg.get(len(numStr)-i, False)
        if aravt != False and integer!=0:
            result = result + aravt
        i+=1

    return result
        
        
        

        
while True:
    first = getNum();
    
    sec = getNum();
    
    result = num2Str(first+sec)
    if result == False:
       print('Please enter correctly')
    else:
        print('Result is '+result+'\n\n\n' )


