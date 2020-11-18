import random
# 读取文件内容
print("----------开始文件读取------------")
with open('future.txt', 'r') as f1:
    list1 = f1.readlines()
# 生成新的文件
newFile = open('new.json', 'w')
newFile.write('[\n')
# 处理文件内容
timeList = []
for line in list1:
    line = line.strip('\n')
    i = 0
    while i > -1:
        index1 = line.find('[', i)
        if index1 == -1:
            break
        else:
            index2 = line.find(']', i)
            point = line[index1 + 1 : index2]
            pointList = point.split(':')
            time = round(int(pointList[0]) * 60 + float(pointList[1]), 2)
            timeList.append(time)
            i += 10
# 反向排序
timeList.reverse()
# 写入文件
lastIndex = 1
lastPosition = 3
lastTime = 0
interval = 1
for time in timeList:
    if lastTime >= interval:
        newFile.write(',\n')
    if time - lastTime < 0.4:
        position = lastPosition
        index = lastIndex
    else:
        position = random.randint(1, 5)
        index = random.randint(1, 5)
    lastTime = time
    lastPosition = position
    lastIndex = index
    if time < interval:
        continue
    newFile.write('\t{\n')
    newFile.write('\t\t"time": '+ str(round(time - interval, 2)) +',\n')
    newFile.write('\t\t"index": '+ str(index) +',\n')
    newFile.write('\t\t"position": '+ str(position) +'\n')
    newFile.write('\t}')
newFile.write('\n]')
print('写入完成')

