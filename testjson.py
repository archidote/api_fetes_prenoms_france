import requests

def getFeast(monthNumber,dayNumber): 
    monthNumber = str(monthNumber)

    url = "http://localhost/frenchNameDays/frenchNameDaysAPI.json"

    params = dict(

    )

    resp = requests.get(url=url, params=params)
    data = resp.json() # Check the JSON Response Content documentation below

    result = data["feast"]["month"][monthNumber]["day"][dayNumber]["name"]

    # print (type(result))

    # print(data["feast"]["month"]["1"]["day"][1])
    # print(data["feast"]["month"]["1"]["day"][2])
    # print(data["feast"]["month"]["2"]["day"][1])
    # print(data["feast"]["month"]["2"]["day"][2])
    return result

print(getFeast(1,2))