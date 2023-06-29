#　缓冲区示例

# fd = open('test','w',0) #　无缓冲 (不允许)
# fd = open('test','w',1) #　行缓冲
# fd = open('test','w',12) #　指名缓冲区大小(不识别)
fd = open('test','w') # 系统默认缓冲区的大小

while True:
    s = input(">>")
    fd.write(s)
    fd.flush() #　立即刷新缓冲,将内容写入磁盘

fd.close()

