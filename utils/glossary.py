import csv


def load(path):
    items = []
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            items.append([unicode(cell, 'utf-8') for cell in row])
    return items
