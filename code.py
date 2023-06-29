s = input(">>")

#　字符串 --> 字节串
byte = s.encode()
print("bytes:",byte)

#　字节串 --> 字符串
s = byte.decode()
print("str:",s)

#　打印字节串
print("bytes:",b"hello world")

# 通过字节串转换函数转换为字节串
print("int :",bytes('abc',encoding='utf-8'))