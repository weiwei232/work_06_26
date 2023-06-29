#　二进制文件写操作

#　以二进制方式打开
fd = open('test','wb')

fd.write(b"hello world") #　必须写入字节串


fd.close()