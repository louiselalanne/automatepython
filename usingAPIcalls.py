# free acount in https://openweathermap.org/api

import requests
url = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID':'key que vem no site','q':'Seattle,US'}
response = requests.get(url, params=parameters)
print(response.content)