import requests

url = 'https://icanhazdadjoke.com/'
headers = {'Accept': 'application/json'}

def get_joke():
  try:
    response = requests.get(url, headers=headers)
    json = response.json()
    print(json['joke'])
  except requests.exceptions.RequestException as e:  # This syntax will catch all errors from a bad response
      raise SystemExit(e)

get_joke()