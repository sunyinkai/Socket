data=b'userName:YinkaiSun\nPasswd:123456\n'
print(str(((str(data).split(':'))[1])))
print(((str(data).split(':'))[1]).split('\\n'))

name= (str(((str(data).split(':'))[1])).split('\\n'))[0]
passwd = (str(((str(data).split(':'))[2])).split('\\n'))[0]
print(type(name),type(passwd))
print(name, passwd)
