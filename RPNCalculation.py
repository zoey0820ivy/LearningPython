import types

def RPNCal(list):
    newList = []
    def Cal(myList, x):
        varA = myList[len(myList) - 2]
        varB = myList[len(myList) - 1]
        del myList[len(myList) - 1]
        del myList[len(myList) - 1]
        if x == "+":
            return varA + varB
        elif x == "-":
            return varA - varB
        elif x == "*":
            return varA * varB
        elif x == "/" :
            return varA / varB
    for a in list :
        if type(a) is types.IntType :
            newList.append(a)
        elif type(a) is types.StringType :
            newList.append(Cal(newList, a))
    return newList[len(newList) - 1]
S = RPNCal([7,8,"+",3,2,"+","/"])
print(S)

