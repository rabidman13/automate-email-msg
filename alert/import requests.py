import requests

resp = requests.post('https://textbelt.com/text', {
  'phone': '09432665609',
  'message': 'Hello world',
  'key': 'textbelt',
})
print(resp.json())