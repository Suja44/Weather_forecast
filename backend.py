import requests
API_key="e97b23792a8a61ab05e226a7a096f1fe"



def get_data(place,forecast_days):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    req=requests.get(url)
    data=req.json()
    filtered_data=data['list'][0:8*forecast_days]

    return filtered_data

if __name__=="__main__":
    dic=get_data("bangalore",2)
    print(dic)