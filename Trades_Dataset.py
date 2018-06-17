#Group Success Impossible - Airlines_Dataset - Arkadiusz
#API-Key: 8FE60437-FDD3-4198-8238-599FE867730B
import webget as wg
import pandas as pd

url = 'https://raw.githubusercontent.com/PeterL93/PythonProject/master/trades_march_to_april_2018.csv'
response = wg.download(url)
print(response + 'downloaded')

dataFrame = pd.read_csv('trades_march_to_april_2018.csv', sep=';')
# Adding separator, sep= cause of the clogged dataset with multiple values.
pd.DataFrame(dataFrame)

# Question 1: What is the transaction with the highest volume in the timespan?
maxVolume = max(dataFrame["size"])
print("The transaction with the highest volume is: " + str(maxVolume))
# Answer: 29.37650126 BTC

# Question 2: What is the average number of transactions per hour?
count = {}

for row in dataFrame["time_exchange"]:
    Split1 = row.split(':')
    Split2 = Split1[0].split('T')

    count.setdefault(Split2[1], 0)
    count[Split2[1]] += 1

    add = 0
    sum = 0

    for k, v in count.items(): #Key and value loop
        add += 1
        sum += v

print("The average number of transactions per hour is: " + str(int(sum/add)))
# Answer: 1111 Transactions per hour.

# Question 3: What is the most favorable, BUYING or SELLING?
BuynSell = {}

for idx in dataFrame['taker_side']:
    BuynSell.setdefault(idx, 0)
    BuynSell[idx] += 1


print("The most favorable of BUYING and SELLING is: " + str(max(BuynSell, key=BuynSell.get)) + " with " + str(max(BuynSell.values())))
# Answer: BUYING: 5075

# Question 4: Average sale price for the currencies?
averagePrice = dataFrame["price"].mean()
print("The average transaction price is: ", averagePrice)
# Answer: 6833.970386