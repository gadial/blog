from typing_extensions import runtime
import yaml,csv

result = []
with open("sipuron.csv", encoding="utf8") as csvfile:
    datareader = csv.reader(csvfile, delimiter=",", quotechar='"')
    for row_index, row in enumerate(datareader):
        if row_index == 0:
            continue 
        result.append({'time': row[0], 'author': row[1], 'keyword': row[2], 'story': row[3]})

with open("sipuron.yml", 'w', encoding="utf8") as yamlfile:
    yaml.dump(result, yamlfile, allow_unicode=True)