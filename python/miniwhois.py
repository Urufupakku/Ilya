import whois11
import re
import csv
array = []
array2 = []
with open('ip.txt', 'r') as f:
    ips = f.read().splitlines()
    with open('miniwhois.csv', 'w') as w:
        reader = csv.writer(w, delimiter=';')
        for i in ips:
            array2=[]
            olo = whois11.whois(i)
            array2.append([i,""])
            grep = re.sub(r'%.*\n', '', olo)
            #grep = re.split(r':', grep)
            array = grep.split('\n')
            for i in array:
                if i != "":
                    a = re.split(r': ', i)
                    array2.append(a)
            for i in array2:
                print(i)
            for i in array2:
                if i[0] != None:
                    w.write(i[0] + ";")
                else:
                    w.write(" "+";")    
            w.write('\n')    
            for i in array2:
                if i[1] != None:
                    w.write(grep + ";")
                else:
                    w.write(" "+";")
            w.write('\n')
            

    