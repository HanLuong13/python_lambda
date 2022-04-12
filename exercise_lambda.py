import csv
from functools import reduce
import json
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#Part 1: Model the Detroit Police Population

#third 
file = open('911_Calls_for_Service_(Last_30_Days).csv')
calls_dictionary = csv.DictReader(file)
calls_list = list(calls_dictionary)

filtered_list = list(filter(lambda row: row['zip_code'] != '0' 
and row['neighborhood'] != '' 
and row['totalresponsetime'] != '' 
and row['dispatchtime'] != '' 
and row['totaltime'] != '' 
, calls_list))

#average total response time
sum_response_time = reduce(lambda time1, time2: time1 + 
float(time2['totalresponsetime']), filtered_list, 0)
avg_total_response_time = sum_response_time/len(filtered_list)
print(avg_total_response_time)

#average dispatch time
sum_avg_time = reduce(lambda time1, time2: time1 + 
float(time2['dispatchtime']), filtered_list, 0)
avg_dispatch_time = sum_avg_time/len(filtered_list)
print(avg_dispatch_time)

# average total time
sum_total_time = reduce(lambda time1, time2: time1 + 
float(time2['totaltime']), filtered_list, 0)
avg_total_time = sum_total_time/len(filtered_list)
print(avg_total_time)

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#Part 2: Model the Neighborhood Samples


neighborhoods = list(map(lambda x: x['neighborhood'], filtered_list))
unique_neighborhoods = []

for line in neighborhoods:
    if not line in unique_neighborhoods:
        unique_neighborhoods.append(line)

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
# Part 3: Create an Output JSON file

#will do with actual list later

json_object = json.dumps(filtered_list)
  

with open("json_list.json", "w") as outfile:
    outfile.write(json_object)