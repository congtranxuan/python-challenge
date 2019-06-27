def split_str(list,a):
    separate=[]
    inter = []
    b = 0
    j = 0
    for i in range(len(list)):
        if list[i] == a: 
            result = ""
            for k in inter:
                result += str(k)
            separate.append(result)
            inter = []
            continue
        else: inter.append(list[i])
        if i == (len(list)-1):
            result = ""
            for k in inter:
                result += str(k)
            separate.append(result)
    return separate


names = "Phuong Mai"
name = [letter for letter in names]
print(name)
c = []
c = split_str(name," ")
print(c)