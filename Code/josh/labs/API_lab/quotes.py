import requests

url = 'https://favqs.com/api/qotd'
headers = {'Content-Type': 'application/json'}


# V1
def get_quote():
  try:
    response = requests.get(url, headers=headers)
    json = response.json()
    print(json)
  except requests.exceptions.RequestException as e:  # This syntax will catch all errors from a bad response
      raise SystemExit(e)

# V2 



#get_quote()