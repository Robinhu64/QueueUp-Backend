import requests
import time

response = requests.get("https://steamspy.com/api.php?request=all")
data = response.json()
appid_list = list(data.keys())

x = 0
name_list = []
while x < len(appid_list):
    retry_count = 0

    response = requests.get("https://store.steampowered.com/api/appdetails?appids=" + appid_list[x])
    print(response.status_code)
    while response.status_code == 429:
        wait_time = 2 ** retry_count
        time.sleep(wait_time)
        retry_count += 1
        response = requests.get("https://store.steampowered.com/api/appdetails?appids=" + appid_list[x])
    details = response.json()
    for app in details.values():
        if app.get("success"):
            name = app["data"].get("name")
            if name:
                name_list.append(name)
    x += 1

print(name_list)
