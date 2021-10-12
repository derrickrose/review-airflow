from pdpyras import APISession

api_token = 'e+aZmphs-KAnCkcGy9Xg'
session = APISession(api_token)

for service in session.iter_all('services'):
    print(service['id'])
    print(repr(service))

for user in session.iter_all('users'):
    print(user['id'], user['email'], user['name'])
