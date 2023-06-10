# README

This script retrieves historical tick data for a specific stock from the Interactive Brokers (IB) Gateway or TWS application and saves it to a CSV file. The script utilizes the `pandas` and `ib_insync` libraries for data manipulation and interaction with the IB API.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed on your system.
- The `pandas` library installed. You can install it using `pip install pandas`.
- The `ib_insync` library installed. You can install it using `pip install ib_insync`.
- Access to the IB Gateway or TWS application. If you don't have it, you can download it from the Interactive Brokers website.

## Usage

1. Import the necessary libraries:
```python
import pandas as pd
from ib_insync import IB, util, Stock
```

2. Create an instance of the `IB` class:
```python
ib = IB()
```

3. Connect to the IB Gateway or TWS application by specifying the host, port, and client ID:
```python
ib.connect('localhost', port, clientId=1)
```
Replace `port` with the appropriate port number for your setup.

4. Define the stock contract for which you want to retrieve historical tick data:
```python
contract = Stock('AAPL', 'SMART', 'USD')
```
Adjust the parameters according to your desired stock.

5. Request historical tick data using the `reqHistoricalTicks` function:
```python
ticks = ib.reqHistoricalTicks(contract, startDateTime='20230609 00:00:00', endDateTime='20230609 23:59:59',
                              numberOfTicks=1000, whatToShow='TRADES', useRth=True)
```
Customize the parameters as needed. This example retrieves 1000 trade ticks for AAPL stock on June 9, 2023.

6. Convert the tick data to a pandas DataFrame:
```python
df = util.df(ticks)
```

7. Save the tick data to a CSV file:
```python
df.to_csv('tick_data.csv', index=False)
```
Specify the desired filename for the CSV file.

8. Disconnect from the IB Gateway or TWS application:
```python
ib.disconnect()
```

## Note

- Ensure that the IB Gateway or TWS application is running and logged in with appropriate credentials before running the script.
- Adjust the host, port, stock contract, date range, and other parameters according to your requirements.
- The script retrieves tick data for a single stock and a specific date range. You can modify it to fetch data for multiple stocks or different time periods.

Feel free to reach out if you have any questions or encounter any issues. Happy data retrieval!
