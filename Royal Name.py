names = ["Albert II","Polo IV","Alexander V","Elizabeth XXV", "Albert XL","Polo XLVI","William IX","Edward XXXIX", "Elizabeth XIX"]
# names = ["Richard V", "Richard II", "Richard X"]
# names = ["Louis IX", "Louis VIII"]
# names = ["Philippe I", "Philip II"]
dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
def romanToInt(roman):
    res = 0
    for i, c in enumerate(roman):
        currVal = dic[c]
        nextVal = dic[roman[i + 1]] if i < len(roman) - 1 else 0
        if currVal < nextVal:
            res -= currVal
        else:
            res += currVal
    return res

def sort(names):
    # print sorted(names, key = lambda x : nameSplit(x)[0])
    print sorted(names, key = lambda x : (x.split(" ")[0], romanToInt(x.split(" ")[1])))
    print sorted(names, key = lambda x : x.split(" ")[0])

sort(names)
