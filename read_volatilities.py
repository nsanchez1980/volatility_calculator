import ccxt,sys, time
from yang_zhang import yang_zhang

if __name__=="__main__":
    samples = 288       #The amount of samples to take into account. 288*5min = 1 day :D
    time_frame = "5m"
    output = []
    volume = 0
    filename = sys.argv[1] + time.strftime("%Y-%m-%d") +".csv"

    #There's no need to enter the API keys for reading data from the exchange, but you can fill in the data if you feel like it.
    if sys.argv[1]=="kucoin":
        exchange_id = "kucoin"                           
        exchange_class = getattr(ccxt, exchange_id)                     
        exchange = exchange_class({   
            "apiKey": "",
            "secret": "",
            "password": "",                                 
            "timeout": 30000,
            "enableRateLimit": True
        })    
    elif sys.argv[1]=="okex5":
        exchange_id = "okex5"                           
        exchange_class = getattr(ccxt, exchange_id)                     
        exchange = exchange_class({   
            "apiKey": "",
            "secret": "",
            "password": "",                                 
            "timeout": 30000,
            "enableRateLimit": True
        })
    elif sys.argv[1]=="binance":
        exchange_id = "binance"                           
        exchange_class = getattr(ccxt, exchange_id)
        exchange = exchange_class({     
            "apiKey": "",
            "secret": "",
            "timeout": 30000,
            "enableRateLimit": True,
        })
    elif sys.argv[1]=="gateio":
        exchange_id = "gateio"                           
        exchange_class = getattr(ccxt, exchange_id)
        exchange = exchange_class({     
            "apiKey": "",
            "secret": "",
            "timeout": 30000,
            "enableRateLimit": True,
        })

    tickers = exchange.fetch_tickers()
    for x in tickers:
        if sys.argv[2] in x:
            try:
                candles = exchange.fetch_ohlcv(x,timeframe=time_frame,limit=samples)
                time.sleep(.5)   #Just for the sake of the API
                volatility = yang_zhang(candles)
                for y in candles:
                    volume += y[4]*y[5]
                result = [x,round(volatility*100,2),int(volume)]
                output.append(result)
                print(result)
            except Exception as e:
                print(e)
            volume = 0
    with open(filename,"w") as output_file:
        output_file.write("Pair,Volatility,Volume")
        for line in output:
            output_file.write(str(line)[1:-1]+"\n")