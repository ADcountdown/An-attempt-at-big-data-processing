#将csv文件转化成一个txt文件 文件内三列数据 src dst src往dst发包的数量

import pandas as pd
ss = pd.read_csv("37.csv", usecols=['Source', 'Destination'])
#ss是一个二维数组的形式 【 【src1 dst】 【src2 dst2】 】
result = {}
for i in ss.values:
    if str(list(i)) not in result:
        result[str(list(i))] = 1
    else:
        result[str(list(i))] += 1
f = open("37.txt","w")
globals = {"nan":0}
for i in result:
    f.write("{0:<}   {1:<}   {2:<}".format(eval(i,globals)[0],eval(i,globals)[1],result[i]))
    f.write("\n")
f.close()
print("done")
