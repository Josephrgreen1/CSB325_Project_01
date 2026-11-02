# Outline for a single stock purchase.
class StockPurchase:

    # Constructs a stock purchase object that stores the stock symbol and the cost per share.
    def __init__(self, stock_symbol, cost_per_share):

        # The symbol of the stock being purchased.
        self.stock_symbol = stock_symbol

        # The cost per share of the stock being purchased.
        self.cost_per_share = cost_per_share
