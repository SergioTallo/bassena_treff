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


def art_4300():
    artikel_4300_0 = []
    artikel_4300_5 = []
    artikel_4300_10 = []
    artikel_4300_13 = []
    artikel_4300_20 = []

    for row in bassenaoriginal:
        pattern = '4300'
        matchobject = re.search(pattern, row[27])
        if matchobject:
            if row[16] == '0':
                artikel_4300_0.append(float(row[22].replace(',', '.')))
            elif row[16] == '5':
                artikel_4300_5.append(float(row[22].replace(',', '.')))
            elif row[16] == '10':
                artikel_4300_10.append(float(row[22].replace(',', '.')))
            elif row[16] == '13':
                artikel_4300_13.append(float(row[22].replace(',', '.')))
            elif row[16] == '20':
                artikel_4300_20.append(float(row[22].replace(',', '.')))

    artikel_4300 = ['4300', str(round(
        sum(artikel_4300_0) + sum(artikel_4300_5) + sum(artikel_4300_10) + sum(artikel_4300_13) + sum(artikel_4300_20),
        2)),
                    str(round(sum(artikel_4300_0), 2)), str(round(sum(artikel_4300_5), 2)),
                    str(round(sum(artikel_4300_10), 2)),
                    str(round(sum(artikel_4300_13), 2)), str(round(sum(artikel_4300_20), 2))]

    final_table.append(artikel_4300)


def art_4400():
    artikel_4400_0 = []
    artikel_4400_5 = []
    artikel_4400_10 = []
    artikel_4400_13 = []
    artikel_4400_20 = []

    for row in bassenaoriginal:
        pattern = '4400'
        matchobject = re.search(pattern, row[27])
        if matchobject:
            if row[16] == '0':
                artikel_4400_0.append(float(row[22].replace(',', '.')))
            elif row[16] == '5':
                artikel_4400_5.append(float(row[22].replace(',', '.')))
            elif row[16] == '10':
                artikel_4400_10.append(float(row[22].replace(',', '.')))
            elif row[16] == '13':
                artikel_4400_13.append(float(row[22].replace(',', '.')))
            elif row[16] == '20':
                artikel_4400_20.append(float(row[22].replace(',', '.')))

    artikel_4400 = ['4400', str(round(
        sum(artikel_4400_0) + sum(artikel_4400_5) + sum(artikel_4400_10) + sum(artikel_4400_13) + sum(artikel_4400_20),
        2)),
                    str(round(sum(artikel_4400_0), 2)), str(round(sum(artikel_4400_5), 2)),
                    str(round(sum(artikel_4400_10), 2)),
                    str(round(sum(artikel_4400_13), 2)), str(round(sum(artikel_4400_20), 2))]

    final_table.append(artikel_4400)


def art_4310():
    artikel_4310_0 = []
    artikel_4310_5 = []
    artikel_4310_10 = []
    artikel_4310_13 = []
    artikel_4310_20 = []

    for row in bassenaoriginal:
        pattern = '4310'
        matchobject = re.search(pattern, row[27])
        if matchobject:
            if row[16] == '0':
                artikel_4310_0.append(float(row[22].replace(',', '.')))
            elif row[16] == '5':
                artikel_4310_5.append(float(row[22].replace(',', '.')))
            elif row[16] == '10':
                artikel_4310_10.append(float(row[22].replace(',', '.')))
            elif row[16] == '13':
                artikel_4310_13.append(float(row[22].replace(',', '.')))
            elif row[16] == '20':
                artikel_4310_20.append(float(row[22].replace(',', '.')))

    artikel_4310 = ['4310', str(round(
        sum(artikel_4310_0) + sum(artikel_4310_5) + sum(artikel_4310_10) + sum(artikel_4310_13) + sum(artikel_4310_20),
        2)),
                    str(round(sum(artikel_4310_0), 2)), str(round(sum(artikel_4310_5), 2)),
                    str(round(sum(artikel_4310_10), 2)),
                    str(round(sum(artikel_4310_13), 2)), str(round(sum(artikel_4310_20), 2))]

    final_table.append(artikel_4310)


def art_4303():
    artikel_4303_0 = []
    artikel_4303_5 = []
    artikel_4303_10 = []
    artikel_4303_13 = []
    artikel_4303_20 = []

    for row in bassenaoriginal:
        pattern = '4303'
        matchobject = re.search(pattern, row[27])
        if matchobject:
            if row[16] == '0':
                artikel_4303_0.append(float(row[22].replace(',', '.')))
            elif row[16] == '5':
                artikel_4303_5.append(float(row[22].replace(',', '.')))
            elif row[16] == '10':
                artikel_4303_10.append(float(row[22].replace(',', '.')))
            elif row[16] == '13':
                artikel_4303_13.append(float(row[22].replace(',', '.')))
            elif row[16] == '20':
                artikel_4303_20.append(float(row[22].replace(',', '.')))

    artikel_4303 = ['4303', str(round(
        sum(artikel_4303_0) + sum(artikel_4303_5) + sum(artikel_4303_10) + sum(artikel_4303_13) + sum(artikel_4303_20),
        2)),
                    str(round(sum(artikel_4303_0), 2)), str(round(sum(artikel_4303_5), 2)),
                    str(round(sum(artikel_4303_10), 2)),
                    str(round(sum(artikel_4303_13), 2)), str(round(sum(artikel_4303_20), 2))]

    final_table.append(artikel_4303)


def art_4304():
    artikel_4304_0 = []
    artikel_4304_5 = []
    artikel_4304_10 = []
    artikel_4304_13 = []
    artikel_4304_20 = []

    for row in bassenaoriginal:
        pattern = '4304'
        matchobject = re.search(pattern, row[27])
        if matchobject:
            if row[16] == '0':
                artikel_4304_0.append(float(row[22].replace(',', '.')))
            elif row[16] == '5':
                artikel_4304_5.append(float(row[22].replace(',', '.')))
            elif row[16] == '10':
                artikel_4304_10.append(float(row[22].replace(',', '.')))
            elif row[16] == '13':
                artikel_4304_13.append(float(row[22].replace(',', '.')))
            elif row[16] == '20':
                artikel_4304_20.append(float(row[22].replace(',', '.')))

    artikel_4304 = ['4304', str(round(
        sum(artikel_4304_0) + sum(artikel_4304_5) + sum(artikel_4304_10) + sum(artikel_4304_13) + sum(artikel_4304_20),
        2)),
                    str(round(sum(artikel_4304_0), 2)), str(round(sum(artikel_4304_5), 2)),
                    str(round(sum(artikel_4304_10), 2)),
                    str(round(sum(artikel_4304_13), 2)), str(round(sum(artikel_4304_20), 2))]

    final_table.append(artikel_4304)


def art_4305():
    artikel_4305_0 = []
    artikel_4305_5 = []
    artikel_4305_10 = []
    artikel_4305_13 = []
    artikel_4305_20 = []

    for row in bassenaoriginal:
        pattern = '4305'
        matchobject = re.search(pattern, row[27])
        if matchobject:
            if row[16] == '0':
                artikel_4305_0.append(float(row[22].replace(',', '.')))
            elif row[16] == '5':
                artikel_4305_5.append(float(row[22].replace(',', '.')))
            elif row[16] == '10':
                artikel_4305_10.append(float(row[22].replace(',', '.')))
            elif row[16] == '13':
                artikel_4305_13.append(float(row[22].replace(',', '.')))
            elif row[16] == '20':
                artikel_4305_20.append(float(row[22].replace(',', '.')))

    artikel_4305 = ['4305', str(round(
        sum(artikel_4305_0) + sum(artikel_4305_5) + sum(artikel_4305_10) + sum(artikel_4305_13) + sum(artikel_4305_20),
        2)),
                    str(round(sum(artikel_4305_0), 2)), str(round(sum(artikel_4305_5), 2)),
                    str(round(sum(artikel_4305_10), 2)),
                    str(round(sum(artikel_4305_13), 2)), str(round(sum(artikel_4305_20), 2))]

    final_table.append(artikel_4305)


def art_4301():
    artikel_4301_0 = []
    artikel_4301_5 = []
    artikel_4301_10 = []
    artikel_4301_13 = []
    artikel_4301_20 = []

    for row in bassenaoriginal:
        pattern = '4301'
        matchobject = re.search(pattern, row[27])
        if matchobject:
            if row[16] == '0':
                artikel_4301_0.append(float(row[22].replace(',', '.')))
            elif row[16] == '5':
                artikel_4301_5.append(float(row[22].replace(',', '.')))
            elif row[16] == '10':
                artikel_4301_10.append(float(row[22].replace(',', '.')))
            elif row[16] == '13':
                artikel_4301_13.append(float(row[22].replace(',', '.')))
            elif row[16] == '20':
                artikel_4301_20.append(float(row[22].replace(',', '.')))

    artikel_4301 = ['4301', str(round(
        sum(artikel_4301_0) + sum(artikel_4301_5) + sum(artikel_4301_10) + sum(artikel_4301_13) + sum(artikel_4301_20),
        2)),
                    str(round(sum(artikel_4301_0), 2)), str(round(sum(artikel_4301_5), 2)),
                    str(round(sum(artikel_4301_10), 2)),
                    str(round(sum(artikel_4301_13), 2)), str(round(sum(artikel_4301_20), 2))]

    final_table.append(artikel_4301)


def art_4307():
    artikel_4307_0 = []
    artikel_4307_5 = []
    artikel_4307_10 = []
    artikel_4307_13 = []
    artikel_4307_20 = []

    for row in bassenaoriginal:
        pattern = '4307'
        matchobject = re.search(pattern, row[27])
        if matchobject:
            if row[16] == '0':
                artikel_4307_0.append(float(row[22].replace(',', '.')))
            elif row[16] == '5':
                artikel_4307_5.append(float(row[22].replace(',', '.')))
            elif row[16] == '10':
                artikel_4307_10.append(float(row[22].replace(',', '.')))
            elif row[16] == '13':
                artikel_4307_13.append(float(row[22].replace(',', '.')))
            elif row[16] == '20':
                artikel_4307_20.append(float(row[22].replace(',', '.')))

    artikel_4307 = ['4307', str(round(
        sum(artikel_4307_0) + sum(artikel_4307_5) + sum(artikel_4307_10) + sum(artikel_4307_13) + sum(artikel_4307_20),
        2)),
                    str(round(sum(artikel_4307_0), 2)), str(round(sum(artikel_4307_5), 2)),
                    str(round(sum(artikel_4307_10), 2)),
                    str(round(sum(artikel_4307_13), 2)), str(round(sum(artikel_4307_20), 2))]

    final_table.append(artikel_4307)


def art_4308():
    artikel_4308_0 = []
    artikel_4308_5 = []
    artikel_4308_10 = []
    artikel_4308_13 = []
    artikel_4308_20 = []

    for row in bassenaoriginal:
        pattern = '4308'
        matchobject = re.search(pattern, row[27])
        if matchobject:
            if row[16] == '0':
                artikel_4308_0.append(float(row[22].replace(',', '.')))
            elif row[16] == '5':
                artikel_4308_5.append(float(row[22].replace(',', '.')))
            elif row[16] == '10':
                artikel_4308_10.append(float(row[22].replace(',', '.')))
            elif row[16] == '13':
                artikel_4308_13.append(float(row[22].replace(',', '.')))
            elif row[16] == '20':
                artikel_4308_20.append(float(row[22].replace(',', '.')))

    artikel_4308 = ['4308', str(round(
        sum(artikel_4308_0) + sum(artikel_4308_5) + sum(artikel_4308_10) + sum(artikel_4308_13) + sum(artikel_4308_20),
        2)),
                    str(round(sum(artikel_4308_0), 2)), str(round(sum(artikel_4308_5), 2)),
                    str(round(sum(artikel_4308_10), 2)),
                    str(round(sum(artikel_4308_13), 2)), str(round(sum(artikel_4308_20), 2))]

    final_table.append(artikel_4308)


def art_4302():
    artikel_4302_0 = []
    artikel_4302_5 = []
    artikel_4302_10 = []
    artikel_4302_13 = []
    artikel_4302_20 = []

    for row in bassenaoriginal:
        pattern = '4302'
        matchobject = re.search(pattern, row[27])
        if matchobject:
            if row[16] == '0':
                artikel_4302_0.append(float(row[22].replace(',', '.')))
            elif row[16] == '5':
                artikel_4302_5.append(float(row[22].replace(',', '.')))
            elif row[16] == '10':
                artikel_4302_10.append(float(row[22].replace(',', '.')))
            elif row[16] == '13':
                artikel_4302_13.append(float(row[22].replace(',', '.')))
            elif row[16] == '20':
                artikel_4302_20.append(float(row[22].replace(',', '.')))

    artikel_4302 = ['4302', str(round(
        sum(artikel_4302_0) + sum(artikel_4302_5) + sum(artikel_4302_10) + sum(artikel_4302_13) + sum(artikel_4302_20),
        2)),
                    str(round(sum(artikel_4302_0), 2)), str(round(sum(artikel_4302_5), 2)),
                    str(round(sum(artikel_4302_10), 2)),
                    str(round(sum(artikel_4302_13), 2)), str(round(sum(artikel_4302_20), 2))]

    final_table.append(artikel_4302)


def art_4002():
    artikel_4002_0 = []
    artikel_4002_5 = []
    artikel_4002_10 = []
    artikel_4002_13 = []
    artikel_4002_20 = []

    for row in bassenaoriginal:
        pattern = '4002'
        matchobject = re.search(pattern, row[27])
        if matchobject:
            if row[16] == '0':
                artikel_4002_0.append(float(row[22].replace(',', '.')))
            elif row[16] == '5':
                artikel_4002_5.append(float(row[22].replace(',', '.')))
            elif row[16] == '10':
                artikel_4002_10.append(float(row[22].replace(',', '.')))
            elif row[16] == '13':
                artikel_4002_13.append(float(row[22].replace(',', '.')))
            elif row[16] == '20':
                artikel_4002_20.append(float(row[22].replace(',', '.')))

    artikel_4002 = ['4002', str(round(
        sum(artikel_4002_0) + sum(artikel_4002_5) + sum(artikel_4002_10) + sum(artikel_4002_13) + sum(artikel_4002_20),
        2)),
                    str(round(sum(artikel_4002_0), 2)), str(round(sum(artikel_4002_5), 2)),
                    str(round(sum(artikel_4002_10), 2)),
                    str(round(sum(artikel_4002_13), 2)), str(round(sum(artikel_4002_20), 2))]

    final_table.append(artikel_4002)


def art_4309():
    artikel_4309_0 = []
    artikel_4309_5 = []
    artikel_4309_10 = []
    artikel_4309_13 = []
    artikel_4309_20 = []

    for row in bassenaoriginal:
        pattern = '4309'
        matchobject = re.search(pattern, row[27])
        if matchobject:
            if row[16] == '0':
                artikel_4309_0.append(float(row[22].replace(',', '.')))
            elif row[16] == '5':
                artikel_4309_5.append(float(row[22].replace(',', '.')))
            elif row[16] == '10':
                artikel_4309_10.append(float(row[22].replace(',', '.')))
            elif row[16] == '13':
                artikel_4309_13.append(float(row[22].replace(',', '.')))
            elif row[16] == '20':
                artikel_4309_20.append(float(row[22].replace(',', '.')))

    artikel_4309 = ['4309', str(round(
        sum(artikel_4309_0) + sum(artikel_4309_5) + sum(artikel_4309_10) + sum(artikel_4309_13) + sum(artikel_4309_20),
        2)),
                    str(round(sum(artikel_4309_0), 2)), str(round(sum(artikel_4309_5), 2)),
                    str(round(sum(artikel_4309_10), 2)),
                    str(round(sum(artikel_4309_13), 2)), str(round(sum(artikel_4309_20), 2))]

    final_table.append(artikel_4309)


bassenaoriginal = read_original_csv(sys.argv[1])

final_table = [['Kontenstelle', 'total', '0%', '5%', '10%', '13%', '20%']]

art_4002()
art_4300()
art_4301()
art_4302()
art_4303()
art_4304()
art_4305()
art_4307()
art_4308()
art_4309()
art_4310()
art_4400()

new_csv = "final_" + sys.argv[1]

write_csv(new_csv)
