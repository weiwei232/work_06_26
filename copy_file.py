filename = input("Filename:") #　文件名称

try:
    fr = open(filename,'rb')
except FileNotFoundError as e:
    print(e)
else:
    fw = open('myfile','wb')

    #　循环读取文件内容写入到ｍｙｆｉｌｅ文件
    while True:
        data = fr.read(1024)
        #　读到文件结尾
        if not data:
            break
        fw.write(data)

    fr.close()
    fw.close()





