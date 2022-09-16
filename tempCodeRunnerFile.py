import requests, json, time

url = "http://host1.dreamhack.games:21879"


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
    return print(json.loads(meRequest.text)["money"])
    
    
if __name__ == "__main__":
    session = sessionAcquire()
    couponSubmit(session, 45)