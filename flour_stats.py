import csv
import re
import statistics
import datetime
from datetime import datetime

import pandas as pd
from matplotlib import pyplot as plt


class flour_stats:

    def __init__(self, filename):
        self.csvlist = read_original_csv(filename)
        self.totaldaymean, self.totaldaymedian = calculate_total_day_mean_median(self.csvlist)
        self.first_day, self.last_day = get_first_and_last_day(self.csvlist)

    # Calculate total brutto sold in a specific weekday and show in a graph
    def calculate_weekday(self, weekday, detail=True, total_mean=False, weather=True, customers=True) -> None:
        days, outliers, mean, median = search_outliers(
            days=search_rows(list_element=self, string=weekday, search_type='weekday'))
        title = 'Brutto Umsatz at ' + weekday

        if total_mean is True:
            print_graph_weekday(days, outliers, mean, median, title, self.totaldaymean, self.totaldaymedian, detail,
                                weather, customers)
        else:
            print_graph_weekday(days, outliers, mean, median, title, mean, median, detail, weather, customers)

    # Calculate total brutto sold in an specific hour and show in a graph
    def calculate_hour(self, time, detail=True, weather=True, customers=True) -> None:
        hour = int(time)
        hour_more = hour + 1

        days, outliers, mean, median = search_outliers(
            days=search_rows(list_element=self, string=time, search_type='time'))
        title = 'Brutto Umsatz von ' + str(time) + ':00 bis ' + str(hour_more) + ':00'

        print_graph_weekday(days, outliers, mean, median, title, mean, median, detail, weather, customers)

    # Calculate total brutto sold in a specific hour in a specific weekday and show in a graph
    def calculate_hour_day(self, weekday, time, detail=True, weather=True, customers=True) -> None:
        hour = int(time)
        hour_more = hour + 1

        self.csvlist = search_weekday(weekday=weekday, list_element=self.csvlist)

        days, outliers, mean, median = search_outliers(
            days=search_rows(self, string=time, search_type='time'))

        title = 'Brutto Umsatz am ' + weekday + ' von ' + str(time) + ':00 bis ' + str(hour_more) + ':00'
        print_graph_weekday(days, outliers, mean, median, title, mean, median, detail, weather, customers)


def get_first_and_last_day(csvlist) -> tuple:
    first_day = csvlist[1][0]
    last_day = csvlist[-1][0]

    return first_day, last_day


def calculate_total_day_mean_median(csvlist) -> tuple:
    datum = ""
    temp_list = []
    days = []

    for row in csvlist:
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


def search_rows(list_element, string, search_type) -> list:
    datum = "00.00.00"
    temp_list = []
    days = []

    weather = get_weather_data(list_element.first_day, list_element.last_day)
    shoppingcart = check_shopping_cart(list_element.csvlist)

    if search_type == "weekday":
        for row in search_weekday(string, list_element.csvlist):

            weather = check_weather_day(weather, datum)

            if row[0] == datum:
                temp_list.append(float(row[23].replace(',', '.')))
            else:
                if len(temp_list) == 0:
                    temp_list = [(float(row[23].replace(',', '.')))]
                    datum = row[0]
                else:
                    day, month, year = datum.split('.')
                    day_name = str('20' + year + '.' + month + '.' + day)

                    days.append((round(sum(temp_list), 2), datum, weather[day_name], shoppingcart[day_name]))

                    temp_list = [(float(row[23].replace(',', '.')))]
                    datum = row[0]

        if len(temp_list) > 0:
            day, month, year = datum.split('.')
            day_name = str('20' + year + '.' + month + '.' + day)

            days.append((round(sum(temp_list), 2), datum, weather[day_name], shoppingcart[day_name]))

    elif search_type == "time":
        for row in search_time(string, list_element.csvlist):

            check_weather_day(weather, datum)

            if row[0] == datum:
                temp_list.append(float(row[23].replace(',', '.')))
            else:
                if len(temp_list) == 0:
                    temp_list = [(float(row[23].replace(',', '.')))]
                    datum = row[0]
                else:
                    day, month, year = datum.split('.')
                    day_name = str('20' + year + '.' + month + '.' + day)

                    days.append((round(sum(temp_list), 2), datum, weather[day_name], shoppingcart[day_name]))

                    temp_list = [(float(row[23].replace(',', '.')))]
                    datum = row[0]

        if len(temp_list) > 0:
            day, month, year = datum.split('.')
            day_name = str('20' + year + '.' + month + '.' + day)

            days.append((round(sum(temp_list), 2), datum, weather[day_name], shoppingcart[day_name]))

    return days


# Print the graph with weekday stats
def print_graph_weekday(money, outliers, mean, median, title, mean_day, median_day, detail, weather, customers):
    days = list(i for i in range(1, len(money) + 1))

    # x axis values: Days
    x = days
    # corresponding y axis values: Money in €
    y = [day[0] for day in money]
    # corresponding y axis (alternative) values: Rain in cm3
    u = [day[2][1] for day in money]
    # corresponding y axis (alternative) values: Average Temperature in °C
    v = [day[2][0] for day in money]
    # corresponding y axis (alternative) values: Average Temperature in °C
    t = [day[3] for day in money]

    r = [day[1] for day in money]

    plt.rcParams["figure.figsize"] = (10, 10)

    # plotting the main (x, y) points
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
    print("-----------------------------------------------------")
    print("\n")
    print(title)
    print("\n")

    # function to show the plot
    plt.show()

    print("\n")

    if len(money) != 0:
        print(f"Durchschnitt Value: {mean} €")
        print(f"Median Value: {median} €")

    if weather is True:
        print("\n")
        print("Money and Rain comparison")
        print("\n")

        fig, ax1 = plt.subplots()

        ax2 = ax1.twinx()
        ax1.plot(x, y, 'g-')
        ax2.plot(x, u, 'b-')

        ax1.set_xlabel('Days')
        ax1.set_ylabel('Money(€)', color='g')
        ax2.set_ylabel('Rain(cm3)', color='b')

        plt.show()

    if customers is True:
        print("\n")
        print("Money and customers comparison")
        print("\n")

        fig, ax1 = plt.subplots()

        ax2 = ax1.twinx()
        ax1.plot(x, y, 'g-')
        ax2.plot(x, t, 'b-')

        ax1.set_xlabel('Days')
        ax1.set_ylabel('Money(€)', color='g')
        ax2.set_ylabel('Number of customers', color='b')

        plt.show()

    if detail is True:

        print("\n")
        print("Detail: ")
        print("\n")

        data = {'Day': [str(day[1]) for day in money], 'Brutto Umsatz': [(str(day[0]) + ' €') for day in money] , 'Rain': [str(day[2][1]) for day in money], 'Temperature': [(str(day[2][0]) + ' °') for day in money], 'Average Korb': [(str(day[3][0]) + ' €') for day in money], 'Anzahl Korb': [str(day[3][1]) for day in money]}

        df = pd.DataFrame (data)

        if len(days) != 0:
            print(df)

        if len(outliers) > 0:
            print("\n")
            print(f"Outliers: ")
            print("\n")
            for out in outliers:
                print(f"{out[1]}: {out[0]} €")

        print("\n")


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
            day_name = datetime(int('20' + year), int(month), int(day))

            if day_name.strftime("%A") == weekday:
                weekday_list.append(row)

    return weekday_list


def read_original_csv(filename) -> list:
    read_bf = []
    try:
        with open(filename, newline='', encoding='ISO-8859-1') as bf:
            csvreader = csv.reader(bf, delimiter=";")
            for row in csvreader:
                read_bf.append(row)

        return read_bf

    except FileNotFoundError as e:
        print("File not found")
        print(e)


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


def get_weather_data(start, end) -> dict:
    from meteostat import Point, Daily

    # Set time period
    day, month, year = start.split('.')
    start = datetime(int('20' + year), int(month), int(day))

    day, month, year = end.split('.')
    end = datetime(int('20' + year), int(month), int(day))

    # Create Point for Vienna, AT
    vienna = Point(48.2082, 16.3738)

    # Get daily data
    data = Daily(vienna, start, end)
    data = data.fetch()

    days = {}

    for row in data.iterrows():
        day, hour = ((str(row[0])).replace('-', '.')).split(' ')
        days[day] = (row[1][0], row[1][3])

    return days


def check_weather_day(weather_dict, datum) -> dict:
    day, month, year = datum.split('.')
    day_name = str('20' + year + '.' + month + '.' + day)

    if day_name not in weather_dict:
        weather_dict[day_name] = ('nan', 'nan')

    return weather_dict


def check_shopping_cart(csvlist) -> dict:
    datum = "00.00.00"
    bills = {}
    temp_list = []
    shop_list = []
    bill_nr = ''

    for row in csvlist:
        if row[0] != 'Datum':
            if row[0] == datum:
                if row[2] == bill_nr:
                    temp_list.append(float(row[23].replace(',', '.')))
                else:
                    if sum(temp_list) > 0:
                        shop_list.append(round(sum(temp_list), 2))

                    temp_list = [(float(row[23].replace(',', '.')))]
                    bill_nr = row[2]

            else:
                if len(temp_list) == 0:
                    temp_list = [(float(row[23].replace(',', '.')))]
                    datum = row[0]
                    bill_nr = row[2]
                else:

                    if sum(temp_list) > 0:
                        shop_list.append(round(sum(temp_list), 2))

                    day, month, year = datum.split('.')
                    day_name = str('20' + year + '.' + month + '.' + day)
                    bills[day_name] = (round(statistics.mean(shop_list), 2), len(shop_list))

                    shop_list = []
                    temp_list = [(float(row[23].replace(',', '.')))]
                    datum = row[0]
                    bill_nr = row[2]

    if len(temp_list) > 0:
        if sum(temp_list) > 0:
            day, month, year = datum.split('.')
            day_name = str('20' + year + '.' + month + '.' + day)
            shop_list.append(round(sum(temp_list), 2))
            bills[day_name] = (round(statistics.mean(shop_list), 2), len(shop_list))

    return bills
