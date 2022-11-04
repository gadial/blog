from typing_extensions import runtime
import yaml,csv

stories = []
keywords = []
authors = []
with open("sipuron.csv", encoding="utf8") as csvfile:
    datareader = csv.reader(csvfile, delimiter=",", quotechar='"')
    for row_index, row in enumerate(datareader):
        if row_index == 0:
            continue
        if row[2] == '':
            keyword = ''
        else:
            keyword = row[2].split(" ")[1]
        stories.append({
            'time': row[0], 
            'author': row[1], 
            'keyword': keyword, 
            'story': row[3],
            'length': len(row[3])
            })
        if not row[1] in authors:
            authors.append(row[1])
        if not keyword in keywords:
            keywords.append(keyword)

result = {
    'year_2022': {
        'stories': stories,
        'keywords': keywords,
        'authors': authors
    }
}
with open("sipuron2022.yml", 'w', encoding="utf8") as yamlfile:
    yaml.dump(result, yamlfile, allow_unicode=True)