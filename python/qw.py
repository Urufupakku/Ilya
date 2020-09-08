import whois11
import re
import csv

domains = []
fields = ['registrar'] #список нужныйх полей


with open('domain.txt', 'r') as f: 
    domains = f.read().splitlines() #создаем массив из файла
with open('output.csv', 'w') as w:
    reader = csv.writer(w, delimiter=';')
    reader.writerow(['IP'] + fields)#1 строка - названия столбцов
    _tempDictFields = {}
    for i in domains:
        _tempDictFields = {'IP':i}
        _tempDictFields.update(dict.fromkeys(fields, '')) # формирования словаря для временного хранения значений полей
        olo = whois11.whois(i) 
        for _field in fields:
            grep = re.search(f"{_field}:.*", olo)
            if grep != None:
                print(grep.group(0))
                _tempDictFields[_field] = grep.group(0)    
        reader.writerow(_tempDictFields.values())

        #все поля и значение должны совпадать по порядку
