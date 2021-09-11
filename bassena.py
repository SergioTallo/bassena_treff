import csv
import re
import sys


def read_original_csv(filename):
    read_bf = []
    with open(filename, newline='', encoding='ISO-8859-1') as bf:
        csvreader = csv.reader(bf, delimiter=";")
        for row in csvreader:
            read_bf.append(row)

    return read_bf


def write_csv(filename):
    with open(filename, 'w', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(final_table)


def calculate_row(kostenstelle):
    artikel_0 = []
    artikel_5 = []
    artikel_10 = []
    artikel_13 = []
    artikel_20 = []
    cost = []

    for row in bassenaoriginal:
        matchobject = re.search(kostenstelle, row[27])
        if matchobject:
            if row[16] == '0':
                artikel_0.append(float(row[22].replace(',', '.')))
            elif row[16] == '5':
                artikel_5.append(float(row[22].replace(',', '.')))
            elif row[16] == '10':
                artikel_10.append(float(row[22].replace(',', '.')))
            elif row[16] == '13':
                artikel_13.append(float(row[22].replace(',', '.')))
            elif row[16] == '20':
                artikel_20.append(float(row[22].replace(',', '.')))

            cost.append (float(row[3]) * float(row[9].replace(',', '.')))

    total = round(sum(artikel_0) + sum(artikel_5) + sum(artikel_10) + sum(artikel_13) + sum(artikel_20), 2)
    total_cost = round(sum(cost), 2)
    deckung = round(total - total_cost, 2)
    prozent = round((deckung / total) * 100, 2)
    
    total_str = str(total)
    artikel_0_strg = str(round(sum(artikel_0), 2))
    artikel_5_strg = str(round(sum(artikel_5), 2))
    artikel_10_strg = str(round(sum(artikel_10), 2))
    artikel_13_strg = str(round(sum(artikel_13), 2))
    artikel_20_strg = str(round(sum(artikel_20), 2))
    total_cost_str = str(total_cost)
    deckung_str = str(deckung)
    prozent_str = str(prozent)
    
    artikel = [kostenstelle, total_str.replace('.', ','), artikel_0_strg.replace('.', ','), artikel_5_strg.replace('.', ','),
                    artikel_10_strg.replace('.', ','), artikel_13_strg.replace('.', ','), artikel_20_strg.replace('.', ','), total_cost_str.replace('.', ','), deckung_str.replace('.', ','), prozent_str.replace('.', ',')]

    final_table.append(artikel)

bassenaoriginal = read_original_csv(sys.argv[1])

final_table = [['Kontenstelle', 'total', '0%', '5%', '10%', '13%', '20%', 'EKges', 'Deckungsbeitrag', '%']]

calculate_row('4002')
calculate_row('4300')
calculate_row('4301')
calculate_row('4302')
calculate_row('4303')
calculate_row('4304')
calculate_row('4305')
calculate_row('4307')
calculate_row('4308')
calculate_row('4309')
calculate_row('4310')
calculate_row('4400')

new_csv = "final_" + sys.argv[1]

write_csv(new_csv)
