import http.client
import json


headers= {
    "x-app-id":"3523fad2",
    "x-app-key":"c3cb9ba83d97755c60ad156f6c5ced80",
}

def nutrionix_calorie(food_name):
    payload={
        "query":food_name
    }
    conn = http.client.HTTPSConnection("trackapi.nutritionix.com")
    conn.request("POST", "/v2/natural/nutrients", json.dumps(payload), headers)
    response = conn.getresponse().read()
    data = json.loads(response)
    return data['foods'][0]["nf_calories"]