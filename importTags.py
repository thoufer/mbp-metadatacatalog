from asset.models import TypedTag
import csv

with open("Tags.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='')
    for row in reader:
        tag = TypedTag()
        tag.name = row[0]
        tag.isSubject = row[1]
        tag.save()
