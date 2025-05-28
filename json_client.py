import requests

BASE = 'http://localhost:10005/api'

# 1) GET 요청
resp = requests.get(f'{BASE}/hello')
print(resp.status_code)    # 200
print(resp.json())         # {'message': 'Hello, Flask!'}

# 2) POST 요청: JSON 바디 전송
payload = {'name': 'Kevin', 'age': 90}
resp2 = requests.post(f'{BASE}/echo', json=payload)
print(resp2.status_code)   # 200
print(resp2.json())
