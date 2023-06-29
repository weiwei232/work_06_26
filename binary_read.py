#　二进制文件读操作

#　以二进制方式打开
fd = open('img.jpg','rb')

data = fd.read() #　得到字节串
print(data)


fd.close()