k = int(input())

def convertNumber(a):
    quantity = 1
    resultBuilder=''
    for digitIndex in range(len(a)):
        countedDigit = a[digitIndex]
        if digitIndex < len(a) - 1:
            if countedDigit == a[digitIndex+1]:
                quantity += 1
            else:
                resultBuilder += str(quantity) + a[digitIndex]
                quantity = 1
        else:
            resultBuilder += str(quantity) + a[digitIndex]
            return resultBuilder

def sequenceElement(k):
    if k == 1:
        return '1'
    if k == 2:
        return '11'
    result = '11'
    for i in range(2, k):
        result = convertNumber(result)
    return result
    
print(sequenceElement(k))
