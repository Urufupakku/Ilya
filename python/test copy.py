import whois11
import re
import csv

class WHOIS:
    def construction (self, ip:str):
        result = whois11.whois(ip)
        self.fields = "\n" + ip + "\n<=====>\n"
        for i in re.findall(r"\S+?:\s.*", result):
            self.fields += i + "\n"

domains = []
res = []

with open('ip.txt', 'r') as f:
    domains = f.read().splitlines()
    with open('output.csv', 'w') as w:
        for i in domains:
            temp = WHOIS()
            temp.construction(i)
            res.append(temp)  # [2.16.107.114; 1.2.3.4; 1.221.254.82; 101.99.91.189; 103.106.236.83] + результаты всех функций в классе (БОЛЬШОЙ ОБЪЕКТ)
        for i in res:
            w.writelines(i.fields)
                