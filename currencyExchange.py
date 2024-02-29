from requests import get
from pprint import PrettyPrinter

base_url = "http://api.nbp.pl/api/"
format = "?format=json"
currency_rate_url = "exchangerates/tables/"

printer = PrettyPrinter()

def get_exchange_rate_data():
    data = []
    url1 = base_url + currency_rate_url + "A" + format
    url2 = base_url + currency_rate_url + "B" + format
    # url3 = base_url + exchange_rate+"C"+format
    data1 = get(url1).json()
    data2 = get(url2).json()
    # data3=get(url3).json()[0]['rates']
    data = data1 + data2
    #print(url1)
    # printer.pprint(data)
    return data


def print_currency(datas):
    for data in datas:
        print(f'{data["code"]} - {data["currency"]} - {data["mid"]}')

# for currency in data:
#     printer.pprint(currency)

def exchange_rate(currency1, currency2):
    data_list = get_exchange_rate_data()[0]['rates'] + get_exchange_rate_data()[1]['rates']
    for data in data_list:
        if data["code"] == currency1:
            rate1 = data["mid"]
        if data["code"] == currency2:
            rate2 = data["mid"]

    return rate1 / rate2


def convert_currency(amount, currency1, currency2):
    rate = exchange_rate(currency1, currency2)
    return amount * rate


def main():
    data = get_exchange_rate_data()[0]['rates'] + get_exchange_rate_data()[1]['rates']
    time= get_exchange_rate_data()[0]['effectiveDate']
    print("Hello, welcome to currency exchange")
    print("Data effective date: ",time)
    print("Data is taken from NBP (National Bank Of Poland) API")
    print("Please select from the following currencies")
    print("Currency 1 to Currency 2 (e.g. USD to EUR) \n")
    try:
        input_currency = input("Please enter Currency 1 code: ").upper()
        output_currency = input("Please enter Currency 2 code: ").upper()
        amount = float(input("Please enter the amount of money: "))
        if amount < 0:
            raise ValueError
        
        converted_amount = convert_currency(amount, input_currency, output_currency)

        print(f"{amount} {input_currency} is equal to {converted_amount} {output_currency}")
    except UnboundLocalError as e: 
        print("No such currency code")
    except ValueError as e:
        print("Please enter a valid amount")

main()
#printer.pprint(get_exchange_rate_data()[0]['rates'] + get_exchange_rate_data()[1]['rates'])