import requests


def currency_rates(num):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    currencies = []
    values = []
    for el in content.split('<ValCurs Date="')[1:]:
        date = el.split('name=Foreign Currency Market>')[0]
        print(date[0:10])
    for el in content.split('<CharCode>')[1:]:
        name = el.split('</CharCode>')[0]
        currencies.append(name)
    for el in content.split('<Value>')[1:]:
        number = el.split('</Value>')[0]
        values.append(number)
    currency = dict(zip(currencies, values))

    return currency.get(num) if num in currency else None
