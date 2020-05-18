import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'smoker':0, 'bmi':33.77, 'age':18,'children':1,'sex':1})

print(r.json())
