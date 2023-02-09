class CurrencyConverter:
    # Conversion rates as of 2021
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
            converted_amount = self.usd * rate
            return converted_amount
        else:
            return None

def main():
    usd = float(input("Enter the amount of money in USD: "))
    converter = CurrencyConverter(usd)
    currency = input("Enter what country you would like to use to convert USD into (UK, Germany, Japan, Australia, Canada, Switzerland): ")
    converted_amount = converter.convert_to_currency(currency)
    
# Example usage
if __name__ == '__main__':
    main()












"""class CurrencyConverter:


    def __initi__(self, money):

        self.money = {1 : "2.4",
                                2 : "4.3"}
        
        self.rate = {1 : "Germany", 
                            2: "China"}
                            

    #def convert(usd, united states):
        
        
    rate = money * rate

    def getConvert(self, rate):
             h = self.money.get(rate)
             k = (money * float(h))
             return k







def main():


    conversion = input("what money would you like to convert")  
    







    if name == "__main__":
        main()"""

