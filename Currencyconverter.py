class CurrencyConverter:
# rough conversions, not exact...
    conversion = {'UK': 0.77,
                  'Germany': 0.86,
                  'Japan': 109.54,
                  'Australia': 1.39,
                  'Canada': 1.29,
                  'Switzerland': 0.93}

    def __init__(self, usd):
        self.usd = usd
#How do I do multiple dictionaries with this problem
    def convert_to_currency(self, currency):
        if currency in self.conversion:
            rate = self.conversion[currency]
            converted_amount = self.usd * rate
            return converted_amount
        else:
            return None

def main():
    usd = float(input("Enter the amount of money in USD: "))
    converter = CurrencyConverter(usd)
    currency = (input("Enter the currency you would like to convert to (UK, Germany, Japan, Australia, Canada, Switzerland): "))
    converted_amount = converter.convert_to_currency(currency)
    if converted_amount:
        print(f"{usd} USD is equal to this amount of money you would have in {currency}: {converted_amount}")
    else:
        print("does not work...sorry")


if __name__ == '__main__':
    main()
	

#tried version 

"""class CurrencyConverter:
    def __initi__(self, money):
        self.money = {1 : "2.4",
                                2 : "4.3"}
        
        self.rate = {1 : "Germany", 
                            2: "China"}
                            
    #def convert(usd, united states):
        
        
    rate = money * rate
    def getConvert(self, rate):
             C= self.money.get(rate)
             c = (money * float(C))
             return C
def main():
    conversion = input("what money would you like to convert")"""  
    















