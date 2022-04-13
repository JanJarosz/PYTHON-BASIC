import requests
from bs4 import BeautifulSoup
import re
from tabulate import tabulate


url = 'https://finance.yahoo.com/most-active'


def generate_shortdict(address):
    stock_dict = {}

    page = requests.get(address)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="screener-results")
    stocks = results.findAll('tr', class_="simpTblRow")

    for stock in stocks:
        short = stock.find("a", class_="Fw(600) C($linkColor)")
        long = stock.find("td", class_="Va(m) Ta(start) Px(10px) Fz(s)")
        stock_dict[short.text] = [short['href'], long.text]

    return stock_dict

stockdict = generate_shortdict(url)


def generate_CEOrank(dictionary):
    attributes = {}
    root = 'https://finance.yahoo.com'
    for stock in dictionary:
        url = root + dictionary[stock][0][0:len(stock)+7] + '/profile' + dictionary[stock][0][len(stock)+7:]
        page = requests.get(url, headers={'User-Agent': 'PostmanRuntime/7.29.0'})
        soup = BeautifulSoup(page.content, "html.parser")
        year_pattern = re.compile(r'\d\d\d\d|N/A')

        name_country_employees = soup.find('div', class_="asset-profile-container")
        full_name = dictionary[stock][1]
        country_employees = name_country_employees.findAll('p')

        if len(list(country_employees[0])) == 11:
            country = list(country_employees[0])[6]
        else:
            country = list(country_employees[0])[4]

        employees = name_country_employees.findAll('span', class_='Fw(600)')
        employees_2 = employees[2].text

        ceo_born = soup.find('section', class_='Bxz(bb)')
        ceo_born2 = ceo_born.findAll('span')

        for i in range(len(ceo_born2)):
            if "CEO" in ceo_born2[i].text:
                if year_pattern.match(ceo_born2[i+4].text):
                    attributes[stock] = [full_name, stock, country, employees_2, ceo_born2[i - 1].text,
                                         str(ceo_born2[i + 4].text)]
                else:
                    attributes[stock] = [full_name, stock, country, employees_2, ceo_born2[i - 1].text,
                                         str(ceo_born2[i + 3].text)]

    sorted_attributes = dict(sorted(attributes.items(), key=lambda e: e[1][5], reverse=True))
    deleted_NA = [key for key in sorted_attributes if sorted_attributes[key][5] == 'N/A']
    for key in deleted_NA:
        del sorted_attributes[key]

    return dict(list(sorted_attributes.items())[:5])


def print_CEOrank(dict):
    to_sheet = generate_CEOrank(stockdict)
    to_table = []
    for key in to_sheet:
        to_table.append(to_sheet[key])
    headers = ["Name", "Code", "Country", "Employees", "CEO Name", "CEO Year Born"]
    return print(tabulate(to_table, headers, tablefmt='github'))


print('========================================= 5 stocks with most youngest CEOs =======================================')
print_CEOrank(generate_CEOrank(stockdict))
print('')

def generate_changerank(dictionary):
    attributes = {}

    root = 'https://finance.yahoo.com'
    for stock in dictionary:
        url = root + dictionary[stock][0][0:len(stock)+7] + '/key-statistics' + dictionary[stock][0][len(stock)+7:]
        page = requests.get(url, headers={'User-Agent': 'PostmanRuntime/7.29.0'})
        soup = BeautifulSoup(page.content, "html.parser")
        full_name = dictionary[stock][1]

        results_1 = soup.find('div', class_="Fl(end) W(50%) smartphone_W(100%)")
        results_2 = results_1.find('table', class_='W(100%) Bdcl(c)').findAll('td')
        week52_change = results_2[3].text

        total_cash_1 = soup.find(text='Total Cash').parent.parent.parent
        total_cash_2 = total_cash_1.findAll('td')[1]

        total_cash = total_cash_2.text

        if week52_change != 'N/A':
            attributes[stock] = [full_name, stock, float(week52_change.replace('%', '').replace(',', '')), total_cash]

    sort = {k: v for k, v in sorted(attributes.items(), key=lambda v: v[1][2], reverse=True)}

    return dict(list(sort.items())[:10])



def print_changerank(dict):
    to_sheet = generate_changerank(dict)
    to_table = []
    for key in to_sheet:
        to_table.append(to_sheet[key])
    headers = ["Name", "Code", "52-Week Change [%]", "Total Cash"]
    return print(tabulate(to_table, headers, tablefmt='github'))

print('================= 5 stocks with biggest 52-Week Change =================')
print_changerank(stockdict)
print('')

def generate_blackrock_holdersrank(website):
    attributes = {}
    page = requests.get(website, headers={'User-Agent': 'PostmanRuntime/7.29.0'})
    soup = BeautifulSoup(page.content, 'html.parser')
    results1 = soup.find(text='Top Institutional Holders').parent.parent.parent
    results1_rows = results1.findAll('tr', class_='BdT Bdc($seperatorColor) Bgc($hoverBgColor):h Whs(nw) H(36px)')

    results2 = soup.find(text='Top Mutual Fund Holders').parent.parent.parent
    results2_rows = results2.findAll('tr', class_='BdT Bdc($seperatorColor) Bgc($hoverBgColor):h Whs(nw) H(36px)')

    results_merged = results1_rows + results2_rows

    for item in results_merged:
        temp = []
        for i in range(len(item)):
            temp.append(item.findAll('td')[i].text.replace(',', ''))
            attributes[temp[0]] = temp

    for key in attributes:
        attributes[key][1] = float(attributes[key][1])

    sort = {k: v for k, v in sorted(attributes.items(), key=lambda v: v[1][1], reverse=True)}

    return dict(list(sort.items())[:10])



holdersrank = generate_blackrock_holdersrank('https://finance.yahoo.com/quote/BLK/holders?p=BLK')

def print_holdersrank(dict):
    to_sheet = dict
    to_table = []
    for key in to_sheet:
        to_table.append(to_sheet[key])
    headers = ["Name", "Shares", "Date Reported", "%out", "Value"]
    return print(tabulate(to_table, headers, tablefmt='github'))

print('=============================== 10 biggest stockholders of Blackrock, INC =============================')
print_holdersrank(holdersrank)

