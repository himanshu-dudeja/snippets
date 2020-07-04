import requests


def basic_request():
    r = requests.get('https://xkcd.com/353/')
    print(r)
    print(dir(r))
    print(help(r))
    print(r.text)


def saving_image_with_request():
    r = requests.get('https://imgs.xkcd.com/comics/python.png')
    with open('image.png', 'wb') as f:
        f.write(r.content)
    print(r.status_code)
    print(r.ok)
    print(r.headers)


def trying_with_httpbin_get():
    payload = {'page': 2, 'count': 25}
    r = requests.get('https://httpbin.org/get', params=payload)
    print(r.url)
    print(r.text)


def trying_with_httpbin_post():
    payload = {'username': "ABC", 'password': "PQR"}
    r = requests.post('https://httpbin.org/post', data=payload)
    # print(r.url)
    # print(r.text)
    # print(r.json())
    r_dict = r.json()
    print(r_dict['form'])


def trying_with_httpbin_basic_auth():
    r = requests.get('https://httpbin.org/basic-auth/ABC/PQR',
                     auth=('ABC', 'PQR'))
    print(r.text)
    print(r.status_code)


def trying_with_httpbin_timeout():
    r = requests.get('https://httpbin.org/delay/6', timeout=3)
    print(r)


if __name__ == '__main__':
    # basic_request()
    # saving_image_with_request()
    # trying_with_httpbin_get()
    # trying_with_httpbin_post()
    # trying_with_httpbin_basic_auth()
    # trying_with_httpbin_timeout()
