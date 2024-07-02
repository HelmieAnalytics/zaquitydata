# zaquity

This package provides utility functions for working with stock price series data of 350 securities trading on the Johannesburg Stock Exchange (XJSE) , including processing stock tickers, fetching historical data, cleaning outliers, and saving the price data in ohlcv format as a dataset in csv files to a folder on your local disc drive.

Note:

1. The package is currently under development and not available for installation on PyPI.
    
2. An MarketStack API is required to retrieve stock tickers which the user can obtain by signing up for an account from the following link https://marketstack.com/

## Modules

`jse_tickers`: Retrieves stock tickers from the MarketStack API.

`jse_data`: Fetches historical stock data using the YahooQuery library.

`jse_process_data`: Processes stock CSV files to remove outliers.

## Implementation

### 1. Import the desired module(s) from the package.

```
import zaquity
from zaquity import jse_tickers
from zaquity import jse_data
from zaquity import jse_process_data
```
   
### 2. Use the provided functions to perform specific tasks related to stock data.

`.get.tickers` function:
```
tickers = jse_tickers.get_tickers("your_api_key_here")
```
`.get.data` function:
```
jse_data.get_data(['AAPL', 'MSFT'], '2022-01-01', '2022-12-31', '/path/to/output_folder')
```
`.clean` function:
```
jse_process_data.clean('/path/to/csv_folder')
```

## Example usage

```
#Import functions
import pandas as pd
import zaquity
from zaquity import jse_tickers as jt
from zaquity import jse_data as jd
from zaquity import process_data as jpd

#Set variables
my_access_key = '<your_Marketstack_API_Key>'

symbols = tickers

start = '2000-01-27'
end = '2024-06-29'

output_folder_path = '/content/jsestocks'

#Call functions

tickers = jt.get_tickers(my_access_key)

jd.get_data(symbols, start, end, output_folder_path)

#Saving the data for each stock to disc
jpd.clean('/content/jsestocks')

# The ohlc price data can now be read from disc to a pandas dataframe 

df = pd.read_csv('/content/jsestocks/NPN.JO.csv') 

Passing the `df` variabl or `print(df)` function will display the ohlc price data of Naspers' share prices from 27 January 2000 to 29 June 2024 in a pandas datafrme. 

```

version:"0.1.0"
author:"Helmie Analytics"
email:"francoishemie@outlook.com"
