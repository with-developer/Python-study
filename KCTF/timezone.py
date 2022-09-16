import json, requests, re

def encoding1(a,b):
    result=[]
    for a,b in zip(a,b):
        result.append(a^b)
    return result

def encoding2(a,b):
    result = []
    for i in a:
        i+=b
        result.append(i)
    return result

#API Info: https://timeapi.io
response = requests.get("https://timeapi.io/api/TimeZone/zone?timeZone=asia/seoul").text
data = json.loads(response)
now_time = data['currentLocalTime']
now_time = re.sub(r'[^0-9]', '', now_time)

reverse_now_time = now_time[::-1]

now_time_temp = []
for character in now_time:
    now_time_temp.append(ord(character))

reverse_now_time_temp = []
for character in reverse_now_time:
    reverse_now_time_temp.append(ord(character))

encoding_result1 = encoding1(now_time_temp, reverse_now_time_temp)

encoding_result2 = encoding2(encoding_result1, 2)

result = ', '.join(map(str, encoding_result2)) 

print("Password: %s" % result)