# client3.py

class Client:
    def __init__(self):
        self.prices = {}

    def getDataPoint(self, stock, bid_price, ask_price):
        # Compute the right stock price using the formula: (bid_price+ask_price) / 2
        price = (bid_price + ask_price) / 2
        return {
            'stock': stock,
            'bid_price': bid_price,
            'ask_price': ask_price,
            'price': price
        }

    def getRatio(self, stock_a, stock_b):
        # Return the ratio of stock price_a to stock price_b
        # Handle the case where price_b could be zero
        if self.prices.get(stock_b, 0) == 0:
            return 0
        return self.prices.get(stock_a, 0) / self.prices.get(stock_b, 0)

    def Main(self, stock_price):
        # Iterate over the data feed and store the datapoints
        for datapoint in stock_price:  
            stock, bid_price, ask_price = datapoint
            data_point = self.getDataPoint(stock, bid_price, ask_price)
            self.prices[stock] = data_point['price']

            # Print the correct ratio
            if stock == 'stock_a':
                ratio = self.getRatio('stock_a', 'stock_b')
                print(f"Ratio: {ratio:.2f}")

if __name__ == "__main__":
    stock_price = [
        ('stock_a', 100, 110),
        ('stock_b', 200, 210),
        ('stock_a', 105, 115),
        ('stock_b', 205, 215),
        ('stock_a', 110, 120),
        ('stock_b', 210, 220),
    ]
    client = Client()
    client.Main(stock_price)
