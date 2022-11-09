import requests

#places = ['Лондон', 'svo', 'Череповец']
places = ['Иваново', 'Ярославль', 'Владимир']

parameters = {'n':'', 'T':'', 'q':'', 'm':'', 'lang':'ru'}

for element in places:
  weather = requests.get(f"https://wttr.in/{element}", params = parameters)
  weather.raise_for_status()
  print(weather.text)