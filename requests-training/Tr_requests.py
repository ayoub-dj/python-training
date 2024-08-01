import requests
from requests.auth import HTTPBasicAuth, AuthBase

url = 'http://127.0.0.1:8000/'
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/128.0 Mobile/15E148 Safari/605.1.15',
    'Content-Type': 'application/json'
}
payload  = {'name': "The last python request"}
proxy = {'http': '102.130.125.86', 'https': '102.130.125.86'}

# GET
r_get = requests.get(url, headers=headers, auth=HTTPBasicAuth("maria", 'x'))
r_get_encoding = r_get.encoding
r_get_status_code = r_get.status_code
r_get_text = r_get.text
r_get_headers = headers['User-Agent']

# Post
r_post = requests.post(f'{url}', headers=headers, json={'name': "The clear vision"}, auth=('maria', 'x'))
r_post_body = r_post.request.body
r_post_url = r_post.request.url
r_post_request = r_post.request

# Put
r_put = requests.put(f'{url}book/1/', headers=headers, json={'name': 'I love you baby [Updated]'})

# Delete
r_delete =  requests.delete(f'{url}book/1/', headers=headers)

# Authentication Using Token
class TokenAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, request):
        request.headers['Authorization'] = f"Bearer {self.token}"

        return request
    
TOKEN = "YOUR_GITHUB_TOKEN"

# If you want to disable SSL certificate verification
# verify=False
# r_get_with_token = requests.request(
#     'GET', 'https://api.github.com/user',
#     auth=TokenAuth(TOKEN),
#     verify=False
#     )

# timeout
# r_one = requests.get(url, timeout=(3.05, 5))


# => 3.05
# => The amount of time the client will wait while trying to establish a
#     connection to the server

#     if the connection is not established within this period, a requests.exceptions.ConnectTimeout exception is raised
# """
# """
# => 5 
#     => The amount of time the client will wait to receive data from the server
#     after the connection has been established

#     If the server does not send any data within this period, a requests.exceptions.ReadTimeout exception is raised.



# Authentication Using session and cookies
SESSION_ID = "cuef7vngççkjkje4iebx2tghj5eq1cbh"
r_with_cookie = requests.get("http://127.0.0.1:8000/", cookies={"sessionid": SESSION_ID})


with requests.Session() as session:
    session.cookies.set('sessionid', SESSION_ID)

    books = session.get("http://127.0.0.1:8000/")
    second_book = session.get("http://127.0.0.1:8000/book/2")

