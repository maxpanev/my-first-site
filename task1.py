import requests
import pprint


url = 'https://api.github.com/search/repositories'

params = {
    'q': 'html'
}

# Отправляем GET-запрос
response = requests.get(url, params=params)

# Выводим статус-код ответа
print(response.status_code)

# Выводим содержимое ответа в формате JSON
pprint.pprint(response.json())