import requests

resp = requests.post('https://textbelt.com/text', {
  'phone': '639274439741',
  'message': 'Hello ate baya testing ni unsay bag o nimo number',
  'key': 'textbelt',
})
print(resp.json())