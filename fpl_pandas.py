#Import
import openpyxl
import requests
import pandas as pd

#Function to generate url endpoint for api
def GetEndpoints():
    apis = []
    baseEndpoint = "https://fantasy.premierleague.com/api/leagues-h2h-matches/league/556449/"    
    for i in range(1, 7):
        if i == 1 :
          print(baseEndpoint)
          apis.append(baseEndpoint)
        else:
            apiEndpoint = baseEndpoint + "?page=" + str(i)
            print(apiEndpoint)
            apis.append(apiEndpoint)
    return apis

#Get all response jsons and append to one whole json
def GetAndAppendAllToOneJson():
    global combinedJson
    #if it doesn't work, comment out these two lines below.
    combinedJson = {}
    combinedJson['Results'] = ''
    apis = GetEndpoints()
    for api in apis:
        response = GetAPIResponse(api)
        resultsjson = response['results']
        combinedJson.append(resultsjson)
    return combinedJson


#Function to get responses from API
def GetAPIResponse(APIEndpointURL):
    response = requests.get(APIEndpointURL).json()
    return response
    
#Convert API response to JSON
def ConvertToJson(data):
    response = data.json()

#######Everything above this line reads teh apis and appends them alotogether#######
#######Below is an example of me writing to pandas df using just 1 API URL. This works but i dont know how o write the appended apis to pandas.
#Create Dataframe
r = requests.get("https://fantasy.premierleague.com/api/leagues-h2h-matches/league/556449/")

json = r.json()

#appendedapis.keys()
json.keys()
#APIEndpointURL.keys()
results_df = pd.DataFrame(json['results'])
#results_df = pd.DataFrame(appendeapi['results'])

print(results_df)

#try this out 
finalJson = GetAndAppendAllToOneJson()
print(finalJson)
results_df2 = pd.DataFrame(finalJson)
print(results_df2)
