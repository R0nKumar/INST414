import requests
import numpy as np

key = "DLYN3QCWIIA1I2EN"
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=' + key

r = requests.get(url)
data = r.json()['Time Series (5min)']

down = []
up = []

for entry in data:
	stock = data[entry]

	change = float(stock['4. close']) - float(stock['1. open'])
	volume = float(stock['5. volume'])

	if volume > 500000:
		if change < 0:
			down.append(volume)
		elif change > 0:
			up.append(volume)


downAvg = str(sum(down) / len(down))
upAvg = str(sum(up) / len(up))



print(str(len(up)) + " stocks went up at an average volume of " + upAvg)
print(str(len(down)) + " stocks went down at an average volume of " + downAvg)











