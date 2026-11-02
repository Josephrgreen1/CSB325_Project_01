from ledger_entry import LedgerEntry
from stock_purchase import StockPurchase


# Manages all stock purchases and sales across different stock symbols.
class StockLedger:

    # Constructs an empty stock ledger.
    def __init__(self):

        # Stores all LedgerEntry objects in a list.
        self.entries = []

        # PROFIT TRACKER ----------------------------------------------------------------------
        self.total_profit = 0



    # Buys a specified number of shares at a given price.
    def buy(self, stock_symbol, shares_bought, price_per_share):

        # Make sure the number of shares is valid.
        if not isinstance(shares_bought, int) or shares_bought <= 0:
            print("Number of shares to buy must be a positive integer.")
            return False

        # Find the ledger entry for this stock.
        entry = self.get_entry(stock_symbol)

        # If the stock is not in the ledger, create a new entry.
        if entry is None:
            entry = LedgerEntry(stock_symbol)
            self.entries.append(entry)

        # Create one StockPurchase object for each share bought.
        for i in range(shares_bought):

            # Create a purchase containing the stock symbol and purchase price.
            new_purchase = StockPurchase(stock_symbol, price_per_share)

            # Add the purchase to the back of this stock's deque.
            entry.add_purchase(new_purchase)




    # Sells shares using FIFO (First In, First Out).
    def sell(self, stock_symbol, shares_sold, price_per_share):

        # Find the ledger entry for this stock.
        entry = self.get_entry(stock_symbol)

        # If the stock does not exist, the sale cannot happen.
        if entry is None:
            print("Stock not found:", stock_symbol)
            return False

        # Make sure the number of shares is a positive integer.
        if not isinstance(shares_sold, int) or shares_sold <= 0:
            print("Number of shares to sell must be a positive integer.")
            return False

        # Get the number of shares currently available.
        available_shares = entry.purchases.size

        # Check whether there are enough shares to sell.
        if shares_sold > available_shares:
            print("Not enough shares available to sell.")
            return False

        # Store the total gain for this sale.
        total_gain_loss = 0

        # Sell the requested number of shares.
        for ie in range(shares_sold):

            # Remove the oldest purchased share from the front.
            purchase = entry.remove_purchase()

            # Calculate the gain for this share.
            gain_loss = price_per_share - purchase.cost_per_share

            # Add it to the total gain or loss.
            total_gain_loss += gain_loss

        # Update the total profit for the ledger.
        self.total_profit += total_gain_loss

        # Print the result of this sale.
        print(stock_symbol, " sale gain/loss: $",
              format(total_gain_loss, ".2f"), sep="")

        return True



    # sell_optimal OPTIMAL SELLING STRATEGY
    # STEP 1:Compare the purchase prices of the share at the front and the share at the back.
    # STEP 2: Sell whichever share has the lower purchase price.

    # EXAMPLE: Front = $50, Back = $30. Sell the $30 share first.

    # This maximizes the immediate gain or minimizes the immediate loss by always selling the cheaper available option.
    # Repeat this process until the requested number of shares has been sold.
    def sell_optimal(self, stock_symbol, shares_sold, price_per_share):

        # Find the stock in our ledger
        entry = self.get_entry(stock_symbol)

        # Make sure the stock exists
        if entry is None:
            print("Stock not found:", stock_symbol)
            return False

        # Make sure the number of shares is valid
        if not isinstance(shares_sold, int) or shares_sold <= 0:
            print("Number of shares to sell must be a positive integer.")
            return False

        # Make sure we have enough shares to sell
        # Use our size counter instead of traversing the deque
        if shares_sold > entry.purchases.size:
            print("Not enough shares available.")
            return False

        # COUNTERS
        current = 0
        total_gain_loss = 0

        # Sell one share at a time
        while current < shares_sold:

            # Get the purchase price at each end
            purchase_price_at_front = entry.purchases.get_front().cost_per_share
            purchase_price_at_back = entry.purchases.get_back().cost_per_share

            # Sell the cheaper share
            if purchase_price_at_back < purchase_price_at_front:
                purchase = entry.purchases.remove_back()
            else:
                purchase = entry.purchases.remove_front()

            # Calculate profit or loss for this share
            gain_loss = price_per_share - purchase.cost_per_share
            total_gain_loss += gain_loss

            # Move to the next share
            current += 1

        # Update the total profit for the ledger
        self.total_profit += total_gain_loss

        # Display our total profit or loss
        print(stock_symbol, " optimal sale gain/loss: $",
              format(total_gain_loss, ".2f"), sep="")

        return True




    # buy_optimal OPTIMAL BUYING STRATEGY:
    # STEP 1: Compare the new share's purchase price to the current front share.
    # STEP 2A: If the new share is cheaper, add it to the front.
    # STEP 2B: Otherwise, add it to the back.
    
    # EXAMPLE: Front = $22, new share = $17.
    # Add $17 to the front so the cheaper share is accessible.
    # If the new share costs $25, add it to the back instead.
    def buy_optimal(self, stock_symbol, shares_bought, price_per_share):

        # Make sure the number of shares is valid
        if not isinstance(shares_bought, int) or shares_bought <= 0:
            print("Number of shares to buy must be a positive integer.")
            return False

        # Find the stock in our ledger
        entry = self.get_entry(stock_symbol)

        # If the stock doesn't exist, create a new ledger entry
        if entry is None:
            entry = LedgerEntry(stock_symbol)
            self.entries.append(entry)

        # Buy one share at a time
        for i in range(shares_bought):

            # Create a new StockPurchase for this share
            new_purchase = StockPurchase(stock_symbol, price_per_share)

            # If the deque is empty, add the first share
            if entry.purchases.is_empty():
                entry.purchases.add_to_front(new_purchase)

            else:
                # Get the purchase price of the current front share
                purchase_price_at_front = entry.purchases.get_front().cost_per_share

                # If the new share is cheaper, add it to the front
                if price_per_share < purchase_price_at_front:
                    entry.purchases.add_to_front(new_purchase)

                # Otherwise, add it to the back
                else:
                    entry.purchases.add_to_back(new_purchase)

        return True


    # Displays the stock ledger and all remaining purchases.
    def display_ledger(self):

        # Print the required ledger heading.
        print("---- Stock Ledger ----")

        # Display each stock's ledger entry.
        for entry in self.entries:
            entry.display_entry()

    # Checks whether a stock symbol exists in the ledger.
    def contains(self, stock_symbol):

        # Returns True if the stock exists, otherwise False.
        return self.get_entry(stock_symbol) is not None

    # Finds and returns the ledger entry for a stock symbol.
    def get_entry(self, stock_symbol):

        # Search through each ledger entry.
        for entry in self.entries:

            # Check whether the stock symbols match.
            if entry.stock_symbol == stock_symbol:
                return entry

        # Return None if no matching stock was found.
        return None
