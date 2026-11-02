from linked_deque import LinkedDeque


# A ledger entry that stores all purchased shares for one stock symbol.
class LedgerEntry:

    # Constructs a ledger entry for a specific stock.
    def __init__(self, stock_symbol):

        # The stock symbol this ledger entry represents.
        self.stock_symbol = stock_symbol

        # Creates an empty deque to store the stock purchases.
        self.purchases = LinkedDeque()

    # Adds a new stock purchase to the back of the deque.
    def add_purchase(self, new_purchase):
        self.purchases.add_to_back(new_purchase)

    # Removes the oldest stock purchase from the front of the deque.
    def remove_purchase(self):
        return self.purchases.remove_front()

    # Checks if another ledger entry represents the same stock symbol.
    def equals(self, other):
        return self.stock_symbol == other.stock_symbol

    # Displays the stock symbol and groups of shares purchased at the same price.
    def display_entry(self):

        # Print the stock symbol without moving to a new line.
        print(self.stock_symbol + ":", end=" ")

        # Start at the front of the deque.
        current_node = self.purchases.front

        # Keep track of the previous purchase price and number of shares.
        previous_price = None
        share_count = 0

        # Store the formatted groups of shares.
        groups = []

        # Go through each stock purchase in the deque.
        while current_node is not None:

            # Get the StockPurchase object from the current node.
            purchase = current_node.get_data()

            # Get the price paid for this share.
            current_price = purchase.cost_per_share

            # If this share has the same price, increase the count.
            if current_price == previous_price:
                share_count += 1

            else:
                # Save the previous group before starting a new one.
                if share_count > 0:
                    groups.append(
                        str(previous_price) + " (" + str(share_count) + " shares)"
                    )

                # Start a new group with the current purchase price.
                previous_price = current_price
                share_count = 1

            # Move to the next node.
            current_node = current_node.get_next_node()

        # Add the final group after the loop finishes.
        if share_count > 0:
            groups.append(
                str(previous_price) + " (" + str(share_count) + " shares)"
            )

        # Print all groups separated by commas.
        print(", ".join(groups))
