import pandas as pd
from ib_insync import IB, util, Stock

# Create an instance of the IB class
ib = IB()

# Connect to the IB Gateway or TWS application
ib.connect('localhost', add port no, clientId=1)  # Adjust host and port as needed

# Request historical tick data
contract = Stock('AAPL', 'SMART', 'USD')  # Define the stock contract
ticks = ib.reqHistoricalTicks(contract, startDateTime='20230609 00:00:00', endDateTime='20230609 23:59:59',
                              numberOfTicks=1000, whatToShow='TRADES', useRth=True)

# Convert tick data to a DataFrame
df = util.df(ticks)

# Save tick data to CSV
df.to_csv('tick_data.csv', index=False)

# Disconnect from the IB Gateway or TWS application
ib.disconnect()
