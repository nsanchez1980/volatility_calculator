# Volatility Calculator

This script reads all the tickers from different exchanges and calculates the volume and the volatility of the pair using the Yang-Zhang algorithm. By default it uses the last 24 hours data (in 5 minute candles)

Exchanges supported: Binance, Kucoin, OKX and Gate.io

Usage:

python3 read_volatilities.py $exchange $quote_currency

Example:

python3 read_volatilities.py binance BUSD
