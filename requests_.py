import requests

URL = "http://0.0.0.0:8000/api/action/"

input_text = "Потушить пожар. Рядом с реактором №4 произошло возгарание урана в бачке мусора. Сотрудники эвакуированы. Необходимо потушить пожар и провести спасательные операции."
print(f"POST input text: {input_text}")
response = requests.post(URL, json={"description": input_text})
print(response)
json = response.json()
print("Response:", json)

#
# print(f"GET")
# response = requests.get(URL)
# json = response.json()
# print("Response:", json)
#
# print(f"DELETE pk 12")
# response = requests.delete(URL+"12")
# json = response.json()
# print("Response:", json)
#
# print(f"GET")
# response = requests.get(URL)
# json = response.json()
# print("Response:", json)
