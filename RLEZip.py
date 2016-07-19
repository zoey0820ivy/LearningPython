
def RLEZip(a):
    l = len(a)
    n = 0
    num = 1
    returnString = ""
    tempStr = ""
    while (n < l - 1):
        if a[n] == a[n + 1]:
            tempStr = a[n]
            num += 1
        else:
            if num == 1:
                saveStr = a[n]
            else:
                saveStr = str(num) + tempStr
            num = 1
            tempStr = ""
            returnString += saveStr
        if n == l - 2 and a[n] == a[n + 1]:
            returnString += str(num) + tempStr
        elif n == l - 2 and a[n] != a[n + 1]:
            returnString += a[n + 1]
        n += 1
    return returnString
S = RLEZip("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB")
print (S)

