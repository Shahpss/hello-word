#!/usr/bin/python
# -*- coding:UTF-8 -*-




#for username

cnt,cnt1 = 0,0
name = []
par =[]

print "User name with atleast one '.' and '_' in it and it must be 8 characters in it"
name = raw_input("User Name:  ")


if(len(name) == 8):
    for spl in name:
        if(spl == '_'):
            cnt += 1
        if(spl == '.'):
            cnt1 += 1


if cnt == 0:
    print "'_' is not there"
    exit(0)

elif cnt1 == 0:
    print "'.' is not there"
    exit(0)     

    if cnt != 0 and cnt1 != 0:
        print "your name successfully inserted"
        par.append(name)
        print par
        cnt,cnt1 = 0,0
        


#for password..........
count1,count2,count3,count4,count5,count6,count7 = 0, 0, 0, 0, 0, 0, 0
password = []
pw = []
password = raw_input("write password: ")

for tpl in password:
    if tpl >='a' and tpl <='z':
        count1 += 1

    if tpl >= 'A' and tpl <= 'Z':
        count2 += 1

    if tpl >= '0' and tpl <= '9':
        count3 += 1

    if tpl == '#' or tpl == '$' or tpl == '%' or tpl == '@' :
        count4 += 1
   

if count1 == 0:
    print "lower case alphabet missing"
    exit(0)

elif count2 == 0:
    print "Upper case alphabet missing"
    exit(0)

elif count3 == 0:
    print "numeric value missing"
    exit(0)

elif count4 == 0:
    print "#, %, @, $  missing"
    exit(0)

        

if count1 != 0 and count2 != 0 and count3 != 0 and count4 != 0 :
    print "your password successfully created"
    pw.append(password)
    count1,count2,count3,count4 = 0, 0, 0, 0


