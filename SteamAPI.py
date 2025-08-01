import requests
import time

response = requests.get("https://steamspy.com/api.php?request=all")
data = response.json()
appid_list = list(data.keys())

x = 0
name_list = []
header_list = []
tags_list = []
while x < len(appid_list):
    time.sleep(2)
    response = requests.get("https://store.steampowered.com/api/appdetails?appids=" + appid_list[x])
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

    x += 1

print(name_list)
print(header_list)
print(tags_list)
