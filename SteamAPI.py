import requests
import time

response = requests.get("https://steamspy.com/api.php?request=all")
data = response.json()
appid_list = list(data.keys())

name_list = []
header_list = []
tags_list = []
delay_time = 1.5
for appid in appid_list:
    time.sleep(delay_time)
    response = requests.get("https://store.steampowered.com/api/appdetails?appids=" + appid_list[appid])
    print(response.status_code)
    details = response.json()
    for app in details.values():
        if app.get("success"):
            name = app["data"].get("name")
            header_image = app["data"].get("header_image")
            tags = app["data"].get("categories")
            if name:
                name_list.append(name)
            if header_image:
                header_list.append(header_image)
            if tags:
                tags_list.append(tags)


print(name_list)
print(header_list)
print(tags_list)
