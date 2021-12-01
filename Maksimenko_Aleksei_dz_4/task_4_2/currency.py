import utils


while True:
    information = input("Enter the currency or q for quit: ")
    print(information, utils.currency_rates(information))
    if information == 'q':
        exit('See you')
