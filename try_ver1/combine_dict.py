#func1 将 2.py 处理好的 txt文件转换成字典的形式
# 字典的键是目的地址，值是一个字典，值的字典的键是给目的地址发包的源地址，值是发包数
def func1(name):
    f = open(name,"r")
    lst = f.readlines()
    result = {}
    for i in lst:
        i = i.rstrip("\n")
        lst1 = i.split("   ")
        if lst1[1] not in result.keys():
            result[lst1[1]] = {lst1[0]:int(lst1[2])}
        else:
            result[lst1[1]][lst1[0]] = int(lst1[2])
    return result

#func2 合并 func1 处理好的 两个字典，生成一个新的字典
def func2(dica,dicb):
    dic = {}
    for key in dica:
        if dicb.get(key):
            if type(dica[key]) == int:
                dic[key] = dica[key] + dicb[key]
            else:
                dic[key] = func2(dica[key], dicb[key])
        else:
            dic[key] = dica[key]
    for key in dicb:
        if dica.get(key):
            pass
        else:
            dic[key] = dicb[key]
    return dic


# if __name__ == '__main__':     #将func1处理好的两个字典合并，写进新文件
#     dic1 = func1("25+26.txt")
#     dic2 = func1("27+28.txt")
#     f = open("res1.txt","w")
#     f.writelines(str(func2(dic1,dic2)))
#     f.close()
#     print("done")

if __name__ == '__main__':     #将两个字典合并，生成新文件
    f1 = open("res1.txt","r")
    f2 = open("res2.txt","r")
    dic1 = eval(f1.readline())
    dic2 = eval(f2.readline())
    f1.close()
    f2.close()
    f = open("res.txt", "w")
    f.writelines(str(func2(dic1,dic2)))
    f.close()
    print("done")

# if __name__ == '__main__':         #将单独的一个文件处理成字典
#     dic1 = func1("131100.txt")
#     f = open("add4.txt", "w")
#     f.writelines(str(dic1))
#     f.close()
#     print("done")