import csv
import re

listOfWords:list[str] = []
with open('/tmp/Docker_Test/fr.txt', encoding='utf8') as txtfile:
    listOfWords = txtfile.readlines()

for i in range(0, len(listOfWords)):
    listOfWords[i] = listOfWords[i].strip('\n').lower()


with open('/tmp/Docker_Test/toCheck.csv', newline='', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        thisPhrase = row['Phrase ou syntagme'].split(" ")
        for i in thisPhrase:
            i = re.sub('(<err>)|(</err>)|[,.!()\d\[\]%]|([a-zA-Z]*\')', '', i)
            if not listOfWords.__contains__(i.lower()) and i != '':
                print(f'erreur sur le mot {i.lower()}')

