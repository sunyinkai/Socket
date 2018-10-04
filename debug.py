import sqlite3
msg="userName:YinkaiSun\nPasswd:123456\n"
name=(((msg.split(':'))[1]).split('\n'))[0]
passwd=(((msg.split(':'))[2]).split('\n'))[0]
print "hello,%s,%s"%(name,passwd)