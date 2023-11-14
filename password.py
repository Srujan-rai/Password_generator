import random

lower="abcdefghijklmnopqrstuvwxyz"
higher="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="123456789"
symbols="!@$%*;/,._-"
all=lower+higher+numbers+symbols
length=16
password="".join(random.sample(all,length))
print(password)