class CurrencyConverter:

    conversion = {'UK': 0.77,
                          'Germany': 0.86,
                          'Japan': 109.54,
                          'Australia': 1.39,
                          'Canada': 1.29,
                          'Switzerland': 0.93}

    def __init__(self, usd):

        self.usd = usd

    def convert_to_currency(self, i):
        if i in self.conversion:
            rate = self.conversion[i]
            i = self.usd * rate
            return i
        


def main():
    usd = float(input("Enter the amount of money in USD: "))
    converter = CurrencyConverter(usd)
    currency = (input("Enter what country you would like to use to convert USD into (UK, Germany, Japan, Australia, Canada, Switzerland): "))
    converted_amount = converter.convert_to_currency(currency)
    
if __name__ == '__main__':
    main()











