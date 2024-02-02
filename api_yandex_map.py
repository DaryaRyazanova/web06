import requests
import sys


def getImage(ll, spn, l):
    map_request = "http://static-maps.yandex.ru/1.x"
    params = {'ll': ll,
              'spn': spn,
              'l': l}
    response = requests.get(map_request, params)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
    else:
        return response
