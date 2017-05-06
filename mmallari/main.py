#print("Hello World")
#print(11)
#print(1+2+3)

#var1 = "Michael Angelo Mallari"
#print var1

#num1 = 10
#num2 = 5
#total = num1 + num2

#print total

#hostname = "192.168.1.1"
#print ("The hostname is: {} \n".format(hostname))


#hostname1 = "192.168.1.1"
#hostname2 = "192.168.1.2"
#hostname3 = "192.168.1.3"

#print ("Hostname1 : {} \n Hostname2 : {} \n Hostname3 : {}".format(hostname1,hostname2.hostname3))

#import os
#response = os.system("ping -c 1 8.8.8.8")
#print(response)

#import os
#response = os.system("ping -c 1 1.1.1.1")
#print(response)

#var = 1
#if var == 0:
#    print("Var is equal to zero")
#elif var == 1:
#    print("Var is equal to one")
#else:
#    print("Var is unknown")

"""
import os
response = os.system("ping -c 1 8.8.8.8")
response1 = os.system("ping -c 1 8.8.4.4")
response2= os.system("ping -c 1 192.168.1.1")
response2= os.system("ping -c 1 192.168.1.2")

os.system("clear")

if response == 0:
    print("8.8.8.8 : Reachable")
elif response == 256:
    print("8.8.8.8 : Unreachable")
else:
    print("8.8.8.8 : Unknown Result")
    
if response1 == 0:
    print("8.8.4.4 : Reachable")
elif response1 == 256:
    print("8.8.4.4 : Unreachable")
else:
    print("8.8.4.4 : Unknown Result")
    
if response2 == 0:
    print("192.168.1.1 : Reachable")
elif response2 == 256:
    print("192.168.1.1 : Unreachable")
else:
    print("192.168.1.1 : Unknown Result")
    
    
if response2 == 0:
    print("192.168.1.2 : Reachable")
elif response2 == 256:
    print("192.168.1.2 : Unreachable")
else:
    print("192.168.1.2 : Unknown Result")


list1=[1,2,3,4,5,6,7,8,9,10]
print(list1[-1])

for x in list1:
    print(x)

"""

"""
import os
import csv

def ping(ip_address):
    response = os.system("ping -c 1 {}".format(ip_address))
    if response == 0:
        return "Reachable"
    else:
        return "Uneachable"

exampleFile = open('ip_list.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
for x in exampleData:
    print("Hostname: {} IP Address: {} Status: {}".format(x[0],x[1],ping(x[1])))

"""

import pexpect

child = pexpect.spawn("telnet 54.199.207.33 32773")
child.sendline("\r\n")
child.sendline("\r\n")
child.expect(">")
child.sendline("en")
child.sendline("\r\n")
child.sendline("conf t")
child.sendline("\r\n")
child.expect("#")
child.sendline("hostname Router1")
child.sendline("\r\n")
child.expect("#")
child.sendline("end")
child.sendline("\r\n")
child.expect("#")