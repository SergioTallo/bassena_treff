from numpy import sort
import csv
import re
import statistics
import math
import matplotlib.pyplot as plt
import datetime


# Read the csv file with the original data and store it in a list
def read_original_csv(filename):
    read_bf = []
    with open(filename, newline='', encoding='ISO-8859-1') as bf:
        csvreader = csv.reader(bf, delimiter=";")
        for row in csvreader:
            read_bf.append(row)

    return read_bf


# Search in the List (created from the csv) for an specific article
def search_articles(article, list_element):
    article_list = []

    for row in list_element:
        matchobject = re.search(article, row[4])
        if matchobject:
            article_list.append(row)

    return article_list


# Search in the List (created from the csv) for an specific time
# (example: 08 for 08:00 - 09:00)
def search_time(time, list_element):
    hour_list = []
    pattern = time + ":\d\d"
    for row in list_element:
        matchobject = re.search(pattern, row[1])
        if matchobject:
            hour_list.append(row)
    return hour_list


# Search in the List (created from the csv) for an day of the week
def search_weekday(weekday, list_element):
    weekday_list = []

    for row in list_element:

        date = row[0]

        if date != 'Datum':
            day, month, year = date.split('.')
            day_name = datetime.date(int('20' + year), int(month), int(day))

            if day_name.strftime("%A") == weekday:
                weekday_list.append(row)

    return weekday_list


# Calculate the statistic of number of articles of one kind sold in one day
def calculate_articles_one_kind(article, original_list):
    counter = 0
    datum = ""
    counter_list = []

    # Count how many articles of this kind (article) is sold in one day, every day
    # Store this information in a list of integers
    for row in search_articles(article, original_list):
        if row[0] == datum:
            counter += float(row[3].replace(',', '.'))
        if row[0] != datum:
            counter_list.append(int(counter))
            counter = float(row[3].replace(',', '.'))
            datum = row[0]

    element_list = []
    number = 0
    counter = 0

    # Count how many days the same amount of articles of this kind are sold
    # Store this information in a list of tuples (number of articles, number of days)
    for element in sort(counter_list):
        if element == number:
            counter += 1
        if element != number:
            element_list.append((number, counter))
            counter = 1
            number = element

    tup = list(zip(*element_list))
    # mode = statistics.mode(counter_list)
    # print(f"mode: {mode}")

    # Print the graph y = number of days that this amount of articles
    # are sold, x = amount of articles of this kind sold in one day
    print_graph(tup, article)


# Print the graph of the statistic of number of articles of one kindsold in one day
def print_graph(tup, artikel):
    # x axis values
    x = tup[0]
    # corresponding y axis values
    y = tup[1]

    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('Verkaufte artikel pro tag')
    # naming the y axis
    plt.ylabel('Number of days')

    # giving a title to my graph
    plt.title(artikel)

    # function to show the plot
    plt.show()


# Calculate total brutto sold in an hour
def calculate_hour(time, original_list):
    datum = ""
    temp_list = []
    days = []

    for row in search_time(time, original_list):
        if row[0] == datum:
            temp_list.append(float(row[23].replace(',', '.')))
        else:
            if len(temp_list) > 0:
                if math.ceil(sum(temp_list)) > (3 * statistics.mean(temp_list)):
                    days.append(round(sum(temp_list), 2))
                temp_list = [(float(row[23].replace(',', '.')))]
            datum = row[0]

    counter = list(i for i in range(1, len(days) + 1))
    print_graph2(days, counter, time)


# Print the graph of the brutto sold in an hour
def print_graph2(money, days, time):
    # x axis values
    x = days
    # corresponding y axis values
    y = money

    hour = int(time)
    hour_more = hour + 1

    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('Days')
    # naming the y axis
    plt.ylabel('€')

    # giving a title to my graph
    print("\n")
    print("-------------------------------------------------------------------")
    print("\n")
    print('Brutto Umsatz von ' + str(time) + ':00 bis ' + str(hour_more) + ':00')

    # function to show the plot
    plt.show()

    if len(money) != 0:
        print(f"Durchschnitt Value: {round(statistics.mean(money), 2)} €")
        print(f"Median Value: {round(statistics.median(sort(money)), 2)} €")


# Calculate total brutto sold in an hour in a weekday
def calculate_hour_day(weekday, time, original_list):
    datum = ""
    temp_list = []
    days = []

    for row in search_time(time, search_weekday(weekday, original_list)):
        if row[0] == datum:
            temp_list.append(float(row[23].replace(',', '.')))
        else:
            if len(temp_list) > 0:
                if math.ceil(sum(temp_list)) > (3 * statistics.mean(temp_list)):
                    days.append(round(sum(temp_list), 2))
                temp_list = [(float(row[23].replace(',', '.')))]
            datum = row[0]

    counter = list(i for i in range(1, len(days) + 1))
    print_graph3(days, counter, time, weekday)


# Print the graph of the brutto sold in an hour in a weekday
def print_graph3(money, days, time, weekday):
    # x axis values
    x = days
    # corresponding y axis values
    y = money

    hour = int(time)
    hour_more = hour + 1

    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('Days')
    # naming the y axis
    plt.ylabel('€')

    # giving a title to my graph
    print("\n")
    print("-------------------------------------------------------------------")
    print("\n")
    print('Brutto Umsatz am ' + weekday + ' von ' + str(time) + ':00 bis ' + str(hour_more) + ':00')

    # function to show the plot
    plt.show()

    if len(money) != 0:
        print(f"Durchschnitt Value: {round(statistics.mean(money), 2)} €")
        print(f"Median Value: {round(statistics.median(sort(money)), 2)} €")


# Calculate total brutto sold in a weekday
def calculate_weekday(weekday, original_list):
    datum = ""
    temp_list = []
    days = []
    outliers = []

    for row in search_weekday(weekday, original_list):
        if row[0] == datum:
            temp_list.append(float(row[23].replace(',', '.')))
        if row[0] != datum:
            if len(temp_list) > 0:
                if len(days) > 0:
                    if math.ceil(sum(temp_list)) < (3 * statistics.mean(days)) and math.floor(sum(temp_list)) > (
                            statistics.mean(days) / 3):
                        days.append(round(sum(temp_list), 2))
                    else:
                        outliers.append((round(sum(temp_list), 2), row[0]))
                else:
                    days.append(round(sum(temp_list), 2))
                temp_list = [(float(row[23].replace(',', '.')))]
            datum = row[0]

    counter = list(i for i in range(1, len(days) + 1))
    print_graph4(days, counter, weekday, outliers)


# Print the graph of the brutto sold in a weekday
def print_graph4(money, days, weekday, outliers):
    # x axis values
    x = days
    # corresponding y axis values
    y = money

    # plotting the points
    plt.plot(x, y)

    # plotting the median and mean value
    if len(money) != 0:
        z = [round(statistics.mean(money), 2) for i in range(1, len(days) + 1)]
        plt.plot(x, z)

        w = [round(statistics.median(money), 2) for i in range(1, len(days) + 1)]
        plt.plot(x, w)

    # naming the x axis
    plt.xlabel('Days')

    # naming the y axis
    plt.ylabel('€')

    # giving a title to my graph
    print("\n")
    print("-----------------------------------------------------")
    print("\n")
    print('Brutto Umsatz am ' + weekday)
    # function to show the plot
    plt.show()

    if len(money) != 0:
        print(f"Durchschnitt Value: {round(statistics.mean(money), 2)} €")
        print(f"Median Value: {round(statistics.median(sort(money)), 2)} €")

    if len(outliers) > 0:
        print(f"Outliers{outliers}")


# Check one hour in one day to see why on this time there is outliers
def check_outliers(day, hour, original_list):
    pattern = hour + ":\d\d"
    temp_list = []
    for row in original_list:
        if row[0] == day:
            matchobject = re.search(pattern, row[1])
            if matchobject:
                print(row)
                temp_list.append(float(row[23].replace(',', '.')))
    print(temp_list)
    print(round(sum(temp_list), 2))