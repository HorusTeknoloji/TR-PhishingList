import json
import sys

with open(sys.argv[1], encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

for datas in data['results']['DomainList']:
    print(datas['FraudDomain'])