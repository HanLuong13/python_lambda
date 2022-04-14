import csv
import json
import statistics
from functools import reduce

# data = list()
# with open('911_Calls_for_Service_(Last_30_Days).csv', 'r', 'newline='',encoding='utf-8-sig') as 

file = open('911_Calls_for_Service_(Last_30_Days).csv')
calls_dictionary = csv.DictReader(file)
data = list(calls_dictionary)

cleanList = filter(lambda oneDict: False if (oneDict['zip_code'] == '0') or (oneDict['neighborhood'] == '') else True, data)
cleanList = list(cleanList)

for i in range(0, len(cleanList)):
    if (cleanList[i]['dispatchtime'] == ''):
        cleanList[i]['dispatchtime'] = 0
    else:
        cleanList[i]['dispatchtime'] = float(cleanList[i]['dispatchtime'])
    
    if (cleanList[i]['totalresponsetime'] == ''):
        cleanList[i]['totalresponsetime'] = 0
    else:
        cleanList[i]['totalresponsetime'] = float(cleanList[i]['totalresponsetime'])

    if (cleanList[i]['totaltime'] == ''):
        cleanList[i]['totaltime'] = 0
    else:
        cleanList[i]['totaltime'] = float(cleanList[i]['totaltime'])

dispatchtimeList = list(map(lambda x: x['dispatchtime'], cleanList))
totalresponsetimeList = list(map(lambda x: x['totalresponsetime'], cleanList))
totaltimeList = list(map(lambda x: x['totaltime'], cleanList))

print(statistics.mean(dispatchtimeList))
print(statistics.mean(totalresponsetimeList))
print(statistics.mean(totaltimeList))


dispatchtimeTot = reduce(lambda num1, num2: num1 + num2, dispatchtimeList, 0)
dispatchtimeAver = dispatchtimeTot/len(dispatchtimeList)
print(dispatchtimeAver)


totalresponsetimeTot = reduce(lambda num1, num2: num1 + num2, totalresponsetimeList, 0)
totalresponsetimeAver = totalresponsetimeTot/len(totalresponsetimeList)
print(totalresponsetimeAver)

totaltimeTot = reduce(lambda num1, num2: num1 + num2, totaltimeList, 0)
totaltimeListAver = totaltimeTot/len(totaltimeList)
print(totaltimeListAver)

#Part 2

towns = list(map(lambda x: x['neighborhood'], cleanList))

#changing to sets so it's unique, and then changing back to list
neighborhoods = list(set(towns))

# print(neighborhoods)

#doing it for 2 neighborhood to understand what to loop

# #Weatherby
# WeatherbyIncidents = list(filter(lambda x: x['neighborhood'] == 'Weatherby', cleanList))
# #Hawthorne
# HawthorneParkIncidents = list(filter(lambda x: x['neighborhood'] == 'Hawthorne', cleanList))

neighborhoodsDict = {}
for neighborhood in neighborhoods:
    neighborhoodsDict[neighborhood] = list(filter(lambda x: x['neighborhood'] == neighborhood, cleanList))

# for i in neighborhoodsDict:
#     print(i)

print(type(neighborhoodsDict))


for neighborhoodsList in neighborhoodsDict.keys():
    nh_dispatchtimeList = list(map(lambda x: x['dispatchtime'], neighborhoodsList))
    nh_totalresponsetimeList = list(map(lambda x: x['totalresponsetime'], neighborhoodsList))
    nh_totaltimeList = list(map(lambda x: x['totaltime'], neighborhoodsList))

    nh_dispatchtimeTot = reduce(lambda num1, num2: num1 + num2, nh_dispatchtimeList, 0)
    nh_dispatchAver = nh_dispatchtimeTot/len(nh_dispatchtimeList)

    nh_totalresponsetimeTot = reduce(lambda num1, num2: num1 + num2, nh_totalresponsetimeList, 0)
    nh_totalresponsetimeAver = nh_totalresponsetimeTot/len(nh_totalresponsetimeList)

    nh_totaltimeTot = reduce(lambda num1, num2: num1 + num2, nh_totaltimeList, 0)
    nh_totaltimeListAver = nh_totaltimeTot/len(nh_totaltimeList)

    print(f'neighbor:{neighborhood} dispatch average time: {nh_dispatchAver}')