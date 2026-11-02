# CSB325 PROJECT 1: Capital Gains Tracker

# OVERVIEW:
This is a stock purchasing, selling, and tracking tool built using python.

It uses a double linked deque in order to store individual stock purchase nodes, which each act as a single share.

The program ultimately boils down to which selling/buying strategy you want to use:
- buy()
- sell()
- buy_optimal()
- sell_optimal()

Depending on which you choose, they can be one of two strategies:

- The FIFO strategy follows the order in which shares were originally purchased. With All new shares are added to the back of the deque, and shares are always sold from the front. This means the oldest shares are sold first, regardless of their original purchase price.

- the optimal strategy is used to try and maximize profits. When buying shares, the program compares the new share's purchase price to the share at the front of the deque. If the new share is cheaper, it is added to the front. Otherwise, it is added to the back. When selling shares, the program compares the purchase prices at both ends of the deque and sells whichever share was purchased for less. This process repeats until the requested number of shares has been sold.

When testing and comparing both strategies, thes were the results:

FIFO Gain: -$640
Optimal Gain: -$480
Difference: $160

As you can see, the optimal strategy worked much better at reducing losses, resulting in the user getting $160 back in their pockets.

# FILES:
- linked_deque.py: Contains the DLNode and LinkedDeque classes. These manage the individual nodes and allow shares to be added or removed from either end of the deque.

- stock_purchase.py: Contains the StockPurchase class, which stores the stock type and original purchase price of an individual share.

- ledger_entry.py: Contains the LedgerEntry class, which manages all purchased shares belonging to a specific stock type.

- stock_ledger.py: Contains the StockLedger class, which handles buying, selling, tracking profits and losses, and managing multiple stocks.

- main.ipynb: The Jupyter Notebook used to test the program, run the required transaction sequences, and compare FIFO and Optimal results.

- Screenshots: Contains the git branch creation along with the UML diagram for this project.

# HOW TO USE:
- Download the files from Github.

- Open the folder with all the files in VSCode, or any python coding engine.

- Make sure you have python and Jupyter all set up and ready to go.

- Open main.ipynb inside the Code folder.

- Click Run All to execute the notebook.

- You can also tinker around and make additional code sections in main.ipynb in order to test things by calling the buy(), sell(), buy_optimal(), or sell_optimal() methods with your own stock types, share quantities, and prices.