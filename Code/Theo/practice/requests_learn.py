import requests

def main():
    url = 'https://httpbin.org/'
    get(url)
    # post(url)
    exit()
    
def get(url):
    url += 'get'
    payload = {
        'page':2,
        'count':25
        }
    r =  requests.get(url,params=payload)
    print(r.url)
    return None

def post(url):
    url += 'post'
    payload = {
        'username' : 'theo',
        'password' : 'hunter2'
    }
    r = requests.post(url,data=payload)
    r_dict = r.json()
    print(r_dict['form'])
    #print(r.text)
    # print(r.json())
    return None

main()