from math import factorial as fact

def factorial(numStr):
    try :
        n = int(numStr)
        r = str(fact(n))
    except:
        r = "Error!"

    return r


def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = "Error!"
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = "Error!"
    return r



romans =[
        (1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
        (100,'C'),(90,'XC'),(50,'L'),(40,'XL'),
        (10,'X'),(9,'IX'),(5,'V'),(4,'IV'),
        (1,'I')
    ]

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n>= 4000:
        return 'Error!'


    result =''

    # 위 romans 속의 튜플을 (value, letters)라고 보고 아래 식을 만든다
    for value, letters in romans:
        # value가 입력받은 n보다 작거나 같을 때까지 반복
        while n >= value:
            # result에 로마자 letters를 붙여 나간다
            result += letters
            # 값에서 해당 튜플 속 숫자 value를 빼나간다
            n -= value

    return result


def romanToDec(romStr):
    s = romStr
    result = 0
    for value, letters in romans:
        while romStr[:len(letters)] == letters:
            romStr = romStr[len(letters):]
            result += value

    if decToRoman(result) != s:
        return "Error!"

    return result





