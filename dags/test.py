from pdpyras import APISession

api_token = 'e+aZmphs-KAnCkcGy9Xg'
session = APISession(api_token)
print("---------- services")
for service in session.iter_all('services'):
    print(service['id'])
    print(repr(service))
print("---------- users")
for user in session.iter_all('users'):
    print(user['id'], user['email'], user['name'])
print("---------- teams")
for team in session.iter_all('teams'):
    print(team['id'])
    print(repr(team))

payload = {
    "type": "incident",
    "severity": "critical",
    "From": "frelininfo@yahoo.fr",
    "title": "This is a merge test",
    "environment": "PROD",
    "dag": "IWD",
    "failed_task": "unzip",
    "link": "www.mail.yahoo.fr"
}
# pd_incident = session.rpost("incidents", json=
import pdpyras

print(repr(session))
session = pdpyras.EventsAPISession('2e7bfe5423e34707d168415a29fbe734')
session.trigger(
    summary=payload['title'],
    severity='critical',
    source="datadog",
    payload=payload,
    custom_details=payload,
    dedup_key="1313",


)
