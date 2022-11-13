#JSON decoder allows us to parse the JSON response into python objects
#JSON stands for javascript object notation
#JSON is a easy adn light format between the server and a client
import requests
r=requests.get('https://api.github.com/events')
events=r.json()
print(events[0])
# #{'id': '22330692244', 'type': 'PushEvent', 'actor': {'id': 19240506, 'login': 'Hertox82', 'display_login': 'Hertox82', 'gravatar_id': '', 'url': 'https://api.github.com/users/Hertox82', 'avatar_url': 'https://avatars.githubusercontent.com/u/19240506?'}, 'repo': {'id': 112625900, 'name': 'Hertox82/lt-codemirror', 'url': 'https://api.github.com/repos/Hertox82/lt-codemirror'}, 'payload': {'push_id': 10158494616, 'size': 2, 'distinct_size': 2, 'ref': 'refs/heads/10.x', 'head': 'd0603570a43e4e4bcc2ede5135f8bff6553051b1', 'before': '57b5c6fa9f55fc6f1abe20fda733c52798f183dc', 'commits': [{'sha': '779b7e29901282118981c31dfb56d9e99a1fa99d', 'author': {'email': 'hernan@lastrega.com', 'name': 'Hernan Ariel De Luca'}, 'message': '10.0.0', 'distinct': True, 'url': 'https://api.github.com/repos/Hertox82/lt-codemirror/commits/779b7e29901282118981c31dfb56d9e99a1fa99d'}, {'sha': 'd0603570a43e4e4bcc2ede5135f8bff6553051b1', 'author': {'email': 'hernan@lastrega.com', 'name': 'Hernan Ariel De Luca'}, 'message': 'modify readme file', 'distinct': True, 'url': 'https://api.github.com/repos/Hertox82/lt-codemirror/commits/d0603570a43e4e4bcc2ede5135f8bff6553051b1'}]}, 'public': True, 'created_at': '2022-06-14T14:18:34Z'}

# print(events[0]['type'])
# #PullRequestReviewEvent

# print(events[0]['id'])
# 22330737886

