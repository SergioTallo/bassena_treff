from numpy import sort
import csv
import re
import statistics
import matplotlib.pyplot as plt
import datetime


# Read the csv file with the original data and store it in a list
def read_original_csv(filename) -> list:
    read_bf = []
    with open(filename, newline='', encoding='ISO-8859-1') as bf:
        csvreader = csv.reader(bf, delimiter=";")
        for row in csvreader:
            read_bf.append(row)

    return read_bf


# Search in the List (created from the csv) for an specific article
def search_articles(article, list_element) -> list:
    article_list = []

    for row in list_element:
        matchobject = re.search(article, row[4])
        if matchobject:
            article_list.append(row)

    return article_list


# Search in the List (created from the csv) for an specific time
# (example: 08 for 08:00 - 09:00)
def search_time(time, list_element) -> list:
    hour_list = []
    pattern = time + ":\d\d"
    for row in list_element:
        matchobject = re.search(pattern, row[1])
        if matchobject:
            hour_list.append(row)
    return hour_list


# Search in the List (created from the csv) for an day of the week
def search_weekday(weekday, list_element) -> list:
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
def calculate_articles_one_kind(article, original_list) -> None:
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
def print_graph(tup, article) -> None:
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
    plt.title(article)

    # function to show the plot
    plt.show()


# Calculate total brutto sold in an hour
def calculate_hour(time, original_list, detail=True) -> None:
    hour = int(time)
    hour_more = hour + 1

    days, outliers, mean, median = search_outliers(search_rows(original_list, time, 'time'))
    title = 'Brutto Umsatz von ' + str(time) + ':00 bis ' + str(hour_more) + ':00'

    print_graph4(days, outliers, mean, median, title, mean, median, detail)


# Calculate total brutto sold in a weekday
def calculate_weekday(weekday, original_list, detail=True, total_mean=False) -> None:
    days, outliers, mean, median = search_outliers(
        days=search_rows(list_element=original_list, string=weekday, search_type='weekday'))
    title = 'Brutto Umsatz at ' + weekday

    if total_mean is True:
        total_mean, total_median = calculate_total_day_mean(original_list)
        print_graph4(days, outliers, mean, median, title, total_mean, total_median, detail)
    else:
        print_graph4(days, outliers, mean, median, title, mean, median, detail)


def calculate_total_day_mean(original_list) -> tuple:
    datum = ""
    temp_list = []
    days = []

    for row in original_list:
        if row[23] != 'Gesamt Brutto':
            if row[0] == datum:
                temp_list.append(float(row[23].replace(',', '.')))
            else:
                if len(temp_list) == 0:
                    temp_list = [(float(row[23].replace(',', '.')))]
                    datum = row[0]
                else:
                    days.append(round(sum(temp_list), 2))
                    temp_list = [(float(row[23].replace(',', '.')))]
                    datum = row[0]

    if len(temp_list) > 0:
        days.append(round(sum(temp_list), 2))

    if len(days) > 0:
        return round(statistics.mean(days), 2), round(statistics.median(days), 2)


# Calculate total brutto sold in an hour in a weekday
def calculate_hour_day(weekday, time, original_list, detail=True) -> None:
    hour = int(time)
    hour_more = hour + 1

    days, outliers, mean, median = search_outliers(search_rows(search_weekday(weekday, original_list), time, 'time'))

    title = 'Brutto Umsatz am ' + weekday + ' von ' + str(time) + ':00 bis ' + str(hour_more) + ':00'
    print_graph4(days, outliers, mean, median, title, mean, median, detail)


def search_rows(list_element, string, search_type) -> list:
    datum = ""
    temp_list = []
    days = []

    if search_type == "weekday":
        for row in search_weekday(string, list_element):
            if row[0] == datum:
                temp_list.append(float(row[23].replace(',', '.')))
            else:
                if len(temp_list) == 0:
                    temp_list = [(float(row[23].replace(',', '.')))]
                    datum = row[0]
                else:
                    days.append((round(sum(temp_list), 2), datum))
                    temp_list = [(float(row[23].replace(',', '.')))]
                    datum = row[0]

        if len(temp_list) > 0:
            days.append((round(sum(temp_list), 2), datum))

    elif search_type == "time":
        for row in search_time(string, list_element):
            if row[0] == datum:
                temp_list.append(float(row[23].replace(',', '.')))
            else:
                if len(temp_list) == 0:
                    temp_list = [(float(row[23].replace(',', '.')))]
                    datum = row[0]
                else:
                    days.append((round(sum(temp_list), 2), datum))
                    temp_list = [(float(row[23].replace(',', '.')))]
                    datum = row[0]

        if len(temp_list) > 0:
            days.append((round(sum(temp_list), 2), datum))

    return days


# Search for outliers in the statistic and eliminate them for the graph
def search_outliers(days):
    outliers = []
    new_days = []

    if len(days) > 0:
        days_revenues = [day[0] for day in days]
        mean = round(statistics.mean(days_revenues), 2)
        median = round(statistics.median(days_revenues), 2)

        for day in days:

            if day[0] > round((((mean + median) / 2) * 3), 2) or day[0] < round((((mean + median) / 2) / 3), 2):
                outliers.append(day)
            else:
                new_days.append(day)

        return new_days, outliers, mean, median


# Print the graph of the brutto sold in a weekday
def print_graph4(money, outliers, mean, median, title, mean_day, median_day, detail):
    days = list(i for i in range(1, len(money) + 1))

    # x axis values
    x = days
    # corresponding y axis values
    y = [day[0] for day in money]

    plt.rcParams["figure.figsize"] = (10, 10)

    # plotting the points
    plt.plot(x, y)

    # plotting the median and mean value
    if len(money) != 0:
        z = [mean_day for i in range(1, len(days) + 1)]
        plt.plot(x, z)

        w = [median_day for i in range(1, len(days) + 1)]
        plt.plot(x, w)

    # naming the x axis
    plt.xlabel('Days')

    # naming the y axis
    plt.ylabel('€')

    # giving a title to my graph
    print("\n")
    print("-----------------------------------------------------")
    print("\n")
    print(title)
    # function to show the plot
    plt.show()

    print("\n")

    if len(money) != 0:
        print(f"Durchschnitt Value: {mean} €")
        print(f"Median Value: {median} €")

    if detail is True:

        print("\n")
        print("Detail: ")
        print("\n")

        if len(days) != 0:
            for day in money:
                print(f"{day[0]} € - {day[1]}")

        if len(outliers) > 0:
            print("\n")
            print(f"Outliers: ")
            print("\n")
            for out in outliers:
                print(f"{out[0]} € - {out[1]}")

        print("\n")


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
