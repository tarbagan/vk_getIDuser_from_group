from urllib.request import urlopen
import json
import math
import time

token = "TOKEN"
group_id = "ID GROUP"

def count_user():
    url = "https://api.vk.com/method/groups.getById.json?group_ids=" + group_id + "&fields=members_count&access_token=" + token + "&v=5.52"
    response = urlopen(url)
    data = response.read()
    jsn = json.loads(data)
    print ("Подключаем группу - " + jsn["response"][0]["name"])
    print( "Подписчиков группы:  - " + str(jsn["response"][0]["members_count"]))
    print ("*******************************")
    count_group = jsn["response"][0]["members_count"]
    return count_group

def pagination():
    tmpus = count_user()
    url_page = set()
    for x in range(0, tmpus, 999):
        url_page.add("https://api.vk.com/method/groups.getMembers.json?group_id=" + group_id + "&access_token=" + token + "&offset=" + str(x) + "&v=5.52")
    return url_page

def get_user_id():
    id = set()
    for url_pag in pagination():
        respag = urlopen(url_pag)
        time.sleep(1)
        data_pag = respag.read()
        jsn_pag = json.loads(data_pag)
        list = (jsn_pag["response"]["items"])
        for id_t in list:
            print( "Получаю данные - " + str(id_t))
            id.add(id_t)
    print ("*****************")
    print( "Получено ID: " + str(len(id)) )
    return id
