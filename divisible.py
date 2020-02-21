nominatorUpOffSet = 1
nominatorLowOffSet = 1
denominator = 2019
tempRemaider =1
resultAt =0ls


while nominatorUpOffSet < 10000:

    #move UpOffSet if it is too small
    while tempRemaider < denominator:
        nominatorUpOffSet = nominatorUpOffSet + 1
        tempRemaider = tempRemaider + 10**(nominatorUpOffSet - nominatorLowOffSet)
    #
    resultAt = 0

    while tempRemaider % 10 != 0:
        tempRemaider = tempRemaider - denominator
        resultAt = resultAt +1

    tempRemaider = tempRemaider / 10
    nominatorLowOffSet = nominatorLowOffSet + 1

    print( "Pos:"+str(resultAt)+"  remainder:" + str(tempRemaider))
    if tempRemaider == 0:
        break
   # print(resultAt)
print(nominatorUpOffSet)


    
