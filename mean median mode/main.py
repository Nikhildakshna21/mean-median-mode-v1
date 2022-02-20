from mean import mean
from median import median
from mode import mode
import csv

with open('heightWeight.csv') as f:
    data = csv.reader(f)
    file_data = list(data)
    file_data.pop(0)
    col = []
    for a in file_data:
        col.append(float(a[2]))

    
print('mean -> {0}'.format(mean(col)))
print('median -> {0}'.format(median(col)))
print('mode -> {0}'.format(mode(col)))
