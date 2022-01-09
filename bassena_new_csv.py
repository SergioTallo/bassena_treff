import csv
import re
import sys
import datetime


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
            try:
                if row[16] == '0':
                    artikel_0.append(float(row[23].replace(',', '.')))
                elif row[16] == '5':
                    artikel_5.append(float(row[23].replace(',', '.')))
                elif row[16] == '10':
                    artikel_10.append(float(row[23].replace(',', '.')))
                elif row[16] == '13':
                    artikel_13.append(float(row[23].replace(',', '.')))
                elif row[16] == '20':
                    artikel_20.append(float(row[23].replace(',', '.')))

                cost.append(float(row[3].replace(',', '.')) * float(row[9].replace(',', '.')))

            except ValueError as e:
                print("Problem in replace , and .")
                print(row[1] + " " + row[2] + " " + row[22] + " " + row[3] + " " + row[9])

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

    '''deckung_str = str(deckung)
    prozent_str = str(prozent)

    artikel = [kostenstelle_dict[kostenstelle], total_str.replace('.', ','), artikel_0_strg.replace('.', ','),
               artikel_5_strg.replace('.', ','), artikel_10_strg.replace('.', ','), artikel_13_strg.replace('.', ','),
               artikel_20_strg.replace('.', ','), total_cost_str.replace('.', ','), deckung_str.replace('.', ','),
               prozent_str.replace('.', ',')]'''

    artikel = [kostenstelle_dict[kostenstelle], total_str.replace('.', ','), artikel_0_strg.replace('.', ','),
               artikel_5_strg.replace('.', ','), artikel_10_strg.replace('.', ','), artikel_13_strg.replace('.', ','),
               artikel_20_strg.replace('.', ','), total_cost_str.replace('.', ',')]

    final_table.append(artikel)


kostenstelle_dict = {'4002': '4002 Erlöse Paketshop', '4300': '4300 Lebensmittel 10%', '4301': '4301 Handelswaren 20%',
                     '4302': '4302 Tiemahrung 13%', '4303': '4303 Alkoholfreie Getränke 20%',
                     '4304': '4304 Alkoholische Getränke 20%', '4305': '4305 Heißgetränke 20%',
                     '4307': '4307 Tabakwaren 20%', '4308': '4308 Lebensmittel 20%', '4309': '4309 FFP2 Masken 0%',
                     '4310': '4310 Haldelswaren 10%', '4400': '4400 Kuche'}

bassenaoriginal = read_original_csv(sys.argv[1])

#final_table = [['Kontenstelle', 'total', '0%', '5%', '10%', '13%', '20%', 'EKges', 'Deckungsbeitrag', '%']]
final_table = [['Kontenstelle', 'total', '0%', '5%', '10%', '13%', '20%', 'EKges']]

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

today = datetime.datetime.now()
date_time = today.strftime("%m%d%Y_%H%M%S")

new_csv = "bassena_bericht_" + date_time + ".csv"

write_csv(new_csv)
