import csv

input = "potencia.txt"
out = []
with open(input, 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    with open('out.txt', 'w') as o:
        writer = csv.writer(o, delimiter='\t')
        for row in reader:
            writer.writerow([row[0], row[1]])
            writer.writerow([row[0], row[2]])
            writer.writerow([row[0], row[3]])
