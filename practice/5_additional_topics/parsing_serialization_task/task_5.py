import os
import json
import pprint
from lxml import etree
from bs4 import BeautifulSoup
rootdir = '/Users/jjarosz/Downloads/PYTHON-BASIC-master/practice/5_additional_topics/parsing_serialization_task/source_data'


def get_cities_attributes(path):
    city_names = [f for f in os.listdir(path) if not f.startswith('.')]
    keys = ['temp', 'wind_speed']
    cities = {}
    i = 0

    for dirpath, dirnames, filenames in os.walk(rootdir):
        for file in filenames:
            hourly_temperature = []
            hourly_wind = []

            if file.endswith('.json'):
                source = open(os.path.join(dirpath, file))
                weather = json.load(source)
                source.close()

                for day in weather["hourly"]:
                    for key in keys:
                        if key == 'temp':
                            hourly_temperature.append(day[key])
                        else:
                            hourly_wind.append(day[key])

                cities[city_names[i]] = [
                    min(hourly_temperature), min(hourly_wind),
                    max(hourly_temperature), max(hourly_wind),
                    round(sum(hourly_temperature) / len(hourly_temperature), 2),
                    round(sum(hourly_wind) / len(hourly_wind), 2)
                ]
                i += 1
    return {"cities_attributes":cities}


def add_summary_stats(dict): #in case of equals gropus(we have same number of hours in each day), mean of mean from each day equals to general mean
    summary_cities = {}
    hottest = {}
    windest = {}
    sum_mean_temp = 0
    sum_mean_wind = 0
    for city in dict["cities_attributes"]:
        sum_mean_temp += dict["cities_attributes"][city][4]
        sum_mean_wind += dict["cities_attributes"][city][5]
        hottest[city] = dict["cities_attributes"][city][4]
        windest[city] = dict["cities_attributes"][city][5]
    summary_cities['mean_temp'] = round(sum_mean_temp / len(dict), 2)
    summary_cities['mean_wind'] = round(sum_mean_wind / len(dict), 2)
    summary_cities['hottest_city'] = max(hottest, key=hottest.get)
    summary_cities['coldest_city'] = min(hottest, key=hottest.get)
    summary_cities['windest_city'] = max(windest, key=windest.get)
    dict['summary'] = summary_cities
    return dict

def create_xml(dict):
    att_keys = ['min_temp', 'min_wind', 'max_temp', 'max_wind', 'mean_temp', 'mean_wind']

    root = etree.Element("weather")
    root.set('Country', 'Spain')
    root.set('date', '2021-09-25')

    e1 = etree.Element('summary')
    for key in dict['summary']:
        e1.set(key, str(dict['summary'][key]))
        root.append(e1)

    e2 = etree.Element('cities')
    for key in dict['cities_attributes']:
        s = etree.SubElement(e2, str(key).replace(' ', '_'))
        for i in range(len(att_keys)):
            s.set(att_keys[i], str(dict['cities_attributes'][key][i]))
    root.append(e2)

    tree = etree.ElementTree(root)

    with open("generated.xml", "wb") as files:
        tree.write(files)

create_xml(add_summary_stats(get_cities_attributes(rootdir)))

#just for check
bs = BeautifulSoup(open('generated.xml'), 'xml')
pretty_xml = bs.prettify()
print(pretty_xml)
