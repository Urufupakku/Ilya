import whois11
import re
import csv
domains = []
with open('domain.txt', 'r') as f:
    domains = f.read().splitlines()
with open('output.csv', 'w') as w:
    reader = csv.writer(w, delimiter=';')
    reader.writerow(['IP', 'registar', 'inetnum'])#1 строка - названия столбцов
    for i in domains:
        output = {'IP':i, 'registrar:':'', 'inetnum:':''}#словарь для временного хранения значений хуиз
        olo = whois11.whois(i) 
        red = ['registrar:', 'inetnum:'] #список полей
        for i in red:
            grep = re.search(f"{i}.*", olo)
            if grep != None:
                print(grep.group(0))
                output[i] = grep.group(0)    
        reader.writerow(output.values())

        #все поля и значение должны совпадать по порядку